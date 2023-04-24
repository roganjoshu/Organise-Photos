from PIL import Image
import os
from datetime import datetime

def ProcessImages():    
    directoryAsString = input("Enter path to folder: ")
    print("Sorting... this may take a few minutes.")
    OrganisePhotos(directoryAsString)
    
def OrganisePhotos(directoryAsString):
    for fileName in os.listdir(directoryAsString):
        
        if fileName.endswith(".jpg") or fileName.endswith(".mp4"):
            
            #old file path is location appended with name
            oldFilePath = os.path.join(directoryAsString, fileName)
            #Identify new location for file we're assessing
            newFileLocation = os.path.join(directoryAsString, GetCreationDate(oldFilePath))
            
            #If the new location doesn't exist then create the new location
            if not os.path.exists(newFileLocation):
                print("Creating new folder.")
                os.mkdir(newFileLocation)
            #Move the image to the new location
            MoveFileToFolder(oldFilePath, newFileLocation, fileName)
                
def GetCreationDate(p_filePath):
    
    #Retrieve .jpg creation date
    if p_filePath.endswith(".jpg"):
        return GetImageCreationDate(p_filePath)
    
    #Retrieve .mp4 creation date
    elif p_filePath.endswith(".mp4"):
        return GetFilmCreationDate(p_filePath)
        
    
def GetImageCreationDate(p_filePath):
        exifData = Image.open(p_filePath)._getexif()[36867]
        return exifData.split(":")[0] + "-" + exifData.split(":")[1]
    
def GetFilmCreationDate(p_filePath):
    creationDate = os.path.getmtime(p_filePath)
    modified_datetime = datetime.fromtimestamp(creationDate)
    modified_datetime_str = modified_datetime.strftime("%Y-%m-%d")
    return modified_datetime_str.split("-")[0] + "-" + modified_datetime_str.split("-")[1]
        
def MoveFileToFolder(p_oldFilePath, p_newFileLocation, p_fileName):
    newFilePath = os.path.join(p_newFileLocation, p_fileName)
    if os.path.exists(newFilePath):
        print("File exists in location")
    else:
        os.rename(p_oldFilePath, newFilePath)

if __name__ == "__main__":
    ProcessImages()