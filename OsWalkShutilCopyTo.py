#Write a program that walks through a folder tree and searches for files with 
#a certain file extension (such as .pdf or .jpg). 
# Copy these files from whatever location they are in to a new folder.


import os, shutil

for folder, subfolders, filenames in os.walk('..\\ATBS'):
    for file in filenames:
        if '.txt' in file:
            if os.path.exists('..\\NewFolder'):
                print(os.path.join(folder,file))
                shutil.copy(os.path.join(folder,file),'..\\NewFolder')
            else:
                os.mkdir('..\\NewFolder')
                shutil.copy(os.path.join(folder,file),'..\\NewFolder')