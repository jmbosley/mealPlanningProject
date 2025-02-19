# Author: Julie Bosley
# Updated: 02/08/2025
# Description: Microservice for deleting recipes

import time
import os

# file Paths
cookbookActLoc = './ActionFolder/cookbookActions.txt'
displayActLoc = './ActionFolder/displayActions.txt'
homepageActLoc = './ActionFolder/homePageActions.txt'

# Cookbook sub pages
addRecipeActLoc = './ActionFolder/addRecipeActions.txt'
displayRecipeListLoc = './ActionFolder/displayRecipeList.txt'
deleteRecipeLoc = './ActionFolder/deleteRecipeActions.txt'

cookbookFolderLoc = './Cookbook/'



while True:
    ogTime = os.path.getmtime(deleteRecipeLoc)
    while (os.path.getmtime(deleteRecipeLoc) <= ogTime):
        time.sleep(1)

    with open(deleteRecipeLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()

# Get Recipe Name and create File
    if read_data == "start":
        dispFile = open(displayActLoc, 'w')
        dispFile.write("cook:dele:star" + "Which Recipe do you wish to delete?\n Type name as it displays in the cookbook then hit enter: ")
        dispFile.close()
    elif read_data != "start" and read_data !="yes" and read_data!="no":
        # ask user if they're sure they want to delete
        recipe = read_data
        dispFile = open(displayActLoc, 'w')
        dispFile.write("cook:dele:conf" + "Are you sure you with to delete " + read_data + "?\n Type (yes/no): ")
        dispFile.close()
    elif read_data == "yes":
        # if confirm, check if recipe exists
        if os.path.isfile(cookbookFolderLoc + recipe + '.txt'):
            os.remove(cookbookFolderLoc + recipe + '.txt')
            dispFile = open(displayActLoc, 'w')
            dispFile.write("cook:dele:succ" + "The recipe " + recipe + " was successfully deleted.")
            dispFile.close()
        else:
            dispFile = open(displayActLoc, 'w')
            dispFile.write("cook:dele:fail" + "The recipe " + recipe + " is already not in the cookbook.")
            dispFile.close()
    elif read_data == "no":
        cookFile = open(cookbookActLoc, 'w')
        cookFile.write("start")
        cookFile.close()