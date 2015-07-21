import os
import sys
import csv

rootdir = "/Users/yingzhou/Documents/projects/my.cs/tests/jbite"

fileList = []
for folders, subs, files in os.walk(rootdir):
    if "result" not in folders:
        
        filesInFolder = []       
        filesInFolder.append(folders.replace("/Users/yingzhou/Documents/projects/my.cs/tests/jbite", ""))
        for file in files:
            if "xlsx" in file:
                filesInFolder.append(file)
        fileList.append(filesInFolder)
            

with open('testfiles.csv','wb') as csvfile:
    wr = csv.writer(csvfile, dialect = 'excel')
    for list in fileList:
        wr.writerow(list)
        

    
    


