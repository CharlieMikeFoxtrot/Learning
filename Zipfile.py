#! python3

import zipfile,os


def backuptozip(folder):
    i=1
    while True:
        zipname = os.path.basename(folder) +'_' + str(i)+'.zip'
        if zipname not in os.listdir():
            print(zipname)
            break
        i+=1
    
    print('Creating back up ' + zipname)
    zipbackup = zipfile.ZipFile(zipname, 'w')
    for foldername, subfolders, files in os.walk('.'):
        print('Adding files in %s...' % (foldername))
        for file in files:
            newBase = os.path.basename(folder) + '_'
            if file.startswith(newBase) and file.endswith('.zip'):
                continue
            zipbackup.write(os.path.join(foldername,file))
            print(os.path.join(foldername,file))
#    for x in os.listdir(folder):
#        print(x)
#        if '.zip' in x:
#            continue
#        zipbackup.write(os.path.basename(folder)+'\\'+x, compress_type=zipfile.ZIP_DEFLATED)
    zipbackup.close()