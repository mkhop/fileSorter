import os, shutil

path = r"D:\ALVLS\megaFolder"


# Removed the IAL_ at the start
for file in os.listdir(path):
    file_name = file.split(".")[0]
    if "IAL_" in file:
        newFileName = file_name.replace("IAL_", "")
        shutil.move(f"{path}\{file}", f"{path}\{newFileName}.pdf")

# Initializing the variables
decisionOne = "WDM11_01"
pureOne = "WMA11_01"
pureTwo = "WMA12_01"
statsOne = "WST11_01"

paperCodes = [decisionOne, pureOne, pureTwo, statsOne]


# Creating folders

def createFolder():
    for paperCode in paperCodes:
        if os.path.exists(f"{path}\{paperCode}"):
            print(f"{paperCode} folder already exists")
        else:
            os.mkdir(f"{path}\{paperCode}")
            print(f"{paperCode} folder created")