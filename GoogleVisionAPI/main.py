import GoogleVisionAPI as GV
import imageAna as IA
import os
####################
# main             #
#########################################
# Set token Key (no quotes on file path)#
# set GOOGLE_APPLICATION_CREDENTIALS=   #
#########################################

# menu
print("What would you like to run?")
print("1. Labels")
print("2. Run All")
print("3. Chop Gif")

# input for menu
print("\n")
choice = input ("Enter an option: ")


# menu execution 
if(choice == '1'):
    imageName = input("Enter image name:")
    GV.labels(imageName)

elif(choice == '2'):
    csvName = input("Enter a name for CSV: ")
    GV.folder(csvName)

elif(choice == '3'):
    imageName = input("Enter image name:")
    file_name = os.path.abspath('resources/pictures/' + imageName)
    IA.getFrames(imageName, file_name, 4)
