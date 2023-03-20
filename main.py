from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

import os

#acvalhlalla ID: 1KP9K5aXPOicSUFkd9x97ccnEiwROHvsn

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.


drive = GoogleDrive(gauth)

folder_list = drive.ListFile({'q': "trashed=false"}).GetList()

for folder in folder_list:
    print ('folder title: %s, id: %s' % (folder['title'], folder['id']))

# Open a file
path = r"C:\Users\eryks\AppData\Roaming\Goldberg UplayEmu Saves\13504"
dirs = os.listdir( path )

# This would print all the files and directories
for file in dirs:
   print(file)

print("Number of files: ",file.__len__())

file1 = drive.CreateFile({'title': file[0],'parents': [{'id': '1KP9K5aXPOicSUFkd9x97ccnEiwROHvsn'}]})
print(file[1])
file1.SetContentFile(path+file[0])
file1.Upload()