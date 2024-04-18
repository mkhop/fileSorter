import os, shutil

path = r"D:\ALVLS\megaFolder"



for file in os.listdir(path):
    file_name = file.split(".")[0]
    if "IAL_" in file:
        newFileName = file_name.replace("IAL_", "")
        shutil.move(f"{path}\{file}", f"{path}\{newFileName}.pdf")

print("success")