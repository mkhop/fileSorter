import os, shutil, re

path = r"C:\Users\mkhvi\Downloads\iAL Mathematics (2018)\iAL Mathematics (2018)"

respectiveFileCount = {}
def checkFileCount():
    name = input("File Type: ")
    count = 0

    while name.strip() != "":
        for file in os.listdir(path):
            if name in file:
                count += 1
        
        respectiveFileCount.update({name: count})

        name = input("File Type: ")
        count = 0
    return respectiveFileCount

    


print(checkFileCount())