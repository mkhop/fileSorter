import os, shutil

path = r"D:\ALVLS\megaFolder"


# Removed the IAL_ at the start
for file in os.listdir(path):
    file_name = file.split(".")[0]
    if "IAL_" in file:
        newFileName = file_name.replace("IAL_", "")
        shutil.move(f"{path}\{file}", f"{path}\{newFileName}.pdf")

# Initializing the variables
decisionOne = "WDM11"
pureOne = "WMA11"
pureTwo = "WMA12"
statsOne = "WST01"

paperCodes = [decisionOne, pureOne, pureTwo, statsOne]
# Creating folders
def createFolder():
    for paperCode in paperCodes:
        if os.path.exists(f"{path}\{paperCode}"):
            print(f"{paperCode} folder already exists")
        else:
            os.mkdir(f"{path}\{paperCode}")
            print(f"{paperCode} folder created")

createFolder()

def assigningFolder():
    for file in os.listdir(path):
        fileCode = file.split("_")[0]

        if fileCode in paperCodes:
            shutil.move(f"{path}\{file}", f"{path}\{fileCode} PDFs")
            print(f"{file} moved to {fileCode} folder")
        else:
            print(f"{file} is not in the paperCodes list")
        

assigningFolder()