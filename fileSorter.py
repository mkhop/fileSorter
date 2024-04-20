import os, shutil, re

path = r"C:\Users\mkhvi\Downloads\iAL Mathematics (2018)\iAL Mathematics (2018)"

respectiveFileCount = {}
def checkFileCount():
    name = input("File Type: ")
    count = 0

    # Running file until user input is null
    while name.strip() != "":
        for file in os.listdir(path):

            # Checking if file contains user input
            if name in file:
                count += 1


                # If the folder already exists, moving file to the folder
                if os.path.exists(f"{path}/{name}"):
                    shutil.move(f"{path}/{file}", f"{path}/{name}")
                
                # Creating and moving file to newly created folder
                else:
                    os.mkdir(f"{path}/{name}")
                    shutil.move(f"{path}/{file}", f"{path}/{name}")

        respectiveFileCount.update({name: count})
        print(f"Created a {name} folder with {count} files")
        name = input("File Type: ")
        count = 0

         
        

    return respectiveFileCount

    


print(checkFileCount())