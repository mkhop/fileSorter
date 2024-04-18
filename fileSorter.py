import os, shutil, re

path = r"D:\ALVLS\megaFolder"


# # Removed the IAL_ at the start
# for file in os.listdir(path):
#     file_name = file.split(".")[0]
#     if "IAL_" in file:
#         newFileName = file_name.replace("IAL_", "")
#         shutil.move(f"{path}\{file}", f"{path}\{newFileName}.pdf")

# # Initializing the variable
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

# Adding new features

def monthYear():
    dateFormat = "^[0-9]{2}[0-9]{2}$"
    paperMonth = paperYear = itemsList = []

    for paperType in paperCodes:
        print(f"Now in {path}\{paperType} PDFs")

        for file in os.listdir(f"{path}\{paperType} PDFs"):
            paperDate = file.split("_")[2]

            if re.search(dateFormat, paperDate):
                paperMonth = re.findall(dateFormat, paperDate)[0]

                if os.path.exists(f"{path}\{paperType} PDFs\{paperMonth}"):
                    shutil.move(f"{path}\{paperType} PDFs\{file}", f"{path}\{paperType} PDFs\{paperMonth}")
                    print("Paper Moved")
                else:
                    os.mkdir(f"{path}\{paperType} PDFs\{paperMonth}")
                    shutil.move(f"{path}\{paperType} PDFs\{file}", f"{path}\{paperType} PDFs\{paperMonth}")
                    print("Paper Moved")
            else:
                continue

def otherPapers():
    for file in os.listdir(path):
        if file.endswith(".pdf"):
            os.remove(f"{path}\{file}")

otherPapers()
# monthYear()

