import GoogleVisionAPI as GV
import imageManip as Imanip
import io
from os import listdir
from os.path import isfile, join
import os
from PIL import Image
####################
# main             #
#########################################
#*THINGS THAT NEED TO GET DONE FOR SETUP#
# Set token Key (no quotes on file path)#
# use the below command to do so        #
# set GOOGLE_APPLICATION_CREDENTIALS=   #
#########################################

runMenu = True
options = ["Labels", "Run All in pictures folder", "Chop Gif (first and middle frame)", "Chop MULTIPLE Gifs into (first and middle frame)", "Split gif into n frames", "Exit"]
while runMenu:
    # menu
    print("\n\n\n*******************************************")
    print("What would you like to run?")
    print("------------------------------")
    for i in range(len(options)):
        print("{}. {}".format(i + 1, options[i]))
    print("*******************************************")

    # input for menu
    print("\n")
    choice = input ("Enter an option: ")
    print("---------------")

    # menu execution 

    # Single file
    if(choice == '1'):
        imageName = input("Enter image/gif name (NEED file extension): ")
        GV.labels(imageName)
        print("\n**********\n for {} complete\n**********\n".format(imageName))

    # All files in folder that produces csv with tags
    elif(choice == '2'):
        csvName = input("Enter a name for CSV output: ")
        GV.folder(csvName)
        print("\n**********\n{}.csv was saved in the CSV folder\n**********\n".format(csvName))

    # Split single gif into first and middle frame
    elif(choice == '3'):
        imageName = input("Enter gif name (no file extension): ")
        fileName = os.path.abspath('resources/input/' + imageName + '.gif')
        Imanip.getFirstAndMiddleFrame(imageName, fileName)
        print("\n**********\nFirst and Middle frames saved in splitGifs folder\n**********\n")

    # Split many gifs into first and middle frame
    elif(choice == '4'):
        for imageName in listdir('resources/input'):
            fileName = os.path.abspath('resources/input/' + imageName)
            Imanip.getFirstAndMiddleFrame(imageName.split('.')[0], fileName)
        print("\n**********\nCheck splitGifs folder for output\n**********\n")

     # Split single gif into n frames
    elif(choice == '5'):
        
        imageName = input("Enter gif name (no file extension): ")
        fileName = os.path.abspath('resources/input/' + imageName + '.gif')
        im = Image.open(fileName)


        maxFrames = im.n_frames
        numFrames = maxFrames
        while(numFrames >= maxFrames):
            numFrames = int(input("Enter the number of frames you want (Max frames is {}): ".format(maxFrames)))
            if(numFrames >= maxFrames):
                print("Input too high. Enter another number")

        Imanip.getXAmountOfFrames(imageName, fileName, numFrames)
        print("\n**********")
        print("{} frames from {}".format(numFrames, imageName))
        print("**********\n")

    # Exit
    elif(choice == str(len(options))):
        runMenu = False

    # Catch all
    else:
        print("\n**********\nOption not available\n**********\n")

