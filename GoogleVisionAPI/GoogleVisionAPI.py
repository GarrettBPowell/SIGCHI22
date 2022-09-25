import csv
from PIL import Image
from os import listdir
from os.path import isfile, join
import io
import os
from google.cloud import vision
#set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\garet\source\repos\GoogleVisionAPI\GoogleVisionAPI\sigchiresearch-a6e68fcc79d4.json


def labels(image):
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath('resources/pictures/' + image)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    # Print labels to console and make list of labels to put in csv
    print('Labels:')
    for label in labels:
        print(label.description)


def folder(csvName):
    client = vision.ImageAnnotatorClient()

    # Make and open CSV file
    csvFile = open('resources/csvs/' + csvName + '.csv', 'w+')
    writer = csv.writer(csvFile)
    writer.writerow(["Name", "Labels"])

    for files in listdir('resources/pictures'):
        # The name of the image file to annotate
        file_name = os.path.abspath('resources/pictures/' + files)

        # Loads the image into memory
        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        # Performs label detection on the image file
        response = client.label_detection(image=image)
        labels = response.label_annotations

        labelList = ["Name: " + files]
        for label in labels:
            #print(label.description)
            labelList.append(label.description)
   
        # write labels to csv
        writer.writerow(labelList)


        print("#######################")
        print("Name: " + files)
        print('Labels:')
        print(labelList)
        print("")
   

    csvFile.close()


# analyze image has to be done before anything can be changed for the gif

def analyseImage(path):
    '''
    Pre-process pass over the image to determine the mode (full or additive).
    Necessary as assessing single frames isn't reliable. Need to know the mode 
    before processing all frames.
    '''
    im = Image.open(path)
    results = {
        'size': im.size,
        'mode': 'full',
    }
    try:
        while True:
            if im.tile:
                tile = im.tile[0]
                update_region = tile[1]
                update_region_dimensions = update_region[2:]
                if update_region_dimensions != im.size:
                    results['mode'] = 'partial'
                    break
            im.seek(im.tell() + 1)
    except EOFError:
        pass
    return results


# Process image
def processImage(path):
    '''
    Iterate the GIF, extracting each frame.
    '''
    mode = analyseImage(path)['mode']
    
    im = Image.open(path)

    i = 0
    p = im.getpalette()
    last_frame = im.convert('RGBA')
    
    try:
        while True:
            print( "saving %s (%s) frame %d, %s %s" % (path, mode, i, im.size, im.tile))
            
            '''
            If the GIF uses local colour tables, each frame will have its own palette.
            If not, we need to apply the global palette to the new frame.
            '''
            if not im.getpalette():
                im.putpalette(p)
            
            new_frame = Image.new('RGBA', im.size)
            
            '''
            Is this file a "partial"-mode GIF where frames update a region of a different size to the entire image?
            If so, we need to construct the new frame by pasting it on top of the preceding frames.
            '''
            if mode == 'partial':
                new_frame.paste(last_frame)
            
            new_frame.paste(im, (0,0), im.convert('RGBA'))
            new_frame.save('%s-%d.png' % (''.join(os.path.basename(path).split('.')[:-1]), i), 'PNG')

            i += 1
            last_frame = new_frame
            im.seek(im.tell() + 1)
    except EOFError:
        pass



####################
# main             #
####################
print("What would you like to run?")
print("1. Labels")
print("2. Run All")
print("3. Chop Gif")

print("\n")
choice = input ("Enter an option: ")

if(choice == '1'):
    imageName = input("Enter image name:")
    labels(imageName)

elif(choice == '2'):
    csvName = input("Enter a name for CSV: ")
    folder(csvName)
elif(choice == '3'):
    imageName = input("Enter image name:")
    file_name = os.path.abspath('resources/pictures/' + imageName)
   
    processImage(file_name)


