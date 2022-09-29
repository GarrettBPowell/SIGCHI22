import csv
import imageManip
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






