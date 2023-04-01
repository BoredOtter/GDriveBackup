from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from tkinter import filedialog
from tkinter import *
import os

def listFiles(path):
    numberOfFiles=0
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            #print("    ",entry)  #list of files in directory
            numberOfFiles+=1
    print("Number of files: ",numberOfFiles)
    return numberOfFiles


def createParentFolder(folderName):
    folder_metadata = {'title' : folderName, 'mimeType' : 'application/vnd.google-apps.folder'}
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()
    folderID=folder['id']
    return folderID

def uploadFiles(path,folderID,numberOfFiles):
    dir = os.listdir(path)
    temp = 0
    for file in dir:
        temp+=1
        print("    Uploading ",temp,"/",numberOfFiles," : ",file)
        File = drive.CreateFile({'title': file,'parents': [{'id': folderID}]})
        File.SetContentFile(path+ "\\" + file)
        File.Upload()
    print("Files uploaded!")

#checking for client_secrets
if os.path.exists('client_secrets.json')==False:
    print("No client_secrets.json")
    os._exit(1)
    #GoogleAuth.DEFAULT_SETTINGS['client_config_file'] = path_to_secrets_file

#google authentication
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

#choosing path
root = Tk()
root.withdraw()
paths = []



dirselect = filedialog.Directory(title='Choose folder to Backup')
while True:
    d = dirselect.show()
    if not d: break
    paths.append(d)
        
print("Folders to backup:")
for i in range(paths.__len__()):
    print("    ",i+1,":",paths[i])

for path in paths:

    folderName=os.path.split(path)[1]

    print("Path: ",path)
    print("Folder: ",folderName)

    #files
    numberOfFiles=listFiles(path)

    #crating a folder with the same name as choosen one
    folderID=createParentFolder(folderName)

    #uploading files to drive
    uploadFiles(path,folderID,numberOfFiles)
    
input("Press Enter to continue")
os._exit(0) #is it worth adding for pyinstaller?

