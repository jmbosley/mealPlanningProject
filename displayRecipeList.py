# Author: Julie Bosley
# Updated: 02/08/2025
# Description: Microservice for displaying recipe list

import time
import os

# file Paths
cookbookActLoc = './ActionFolder/cookbookActions.txt'
displayActLoc = './ActionFolder/displayActions.txt'
homepageActLoc = './ActionFolder/homePageActions.txt'

# Cookbook sub pages
addRecipeActLoc = './ActionFolder/addRecipeActions.txt'
displayRecipeListLoc = './ActionFolder/displayRecipeList.txt'
cookbookFolderLoc = './Cookbook/'

#Text
openingText = "The recipes currently in your cookbook are:\n"


while True:
    ogTime = os.path.getmtime(displayRecipeListLoc)
    while (os.path.getmtime(displayRecipeListLoc) <= ogTime):
        time.sleep(1)
    with open(displayRecipeListLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()

# Get Recipe Name and create File
    if read_data == "start":
        directory = os.listdir(cookbookFolderLoc)
        if len(directory) == 0: # directry is empty
            addRecipeFile = open(displayActLoc, 'w')
            addRecipeFile.write("cook:dili:emptYour cookbook is empty. Please add some recipes using 'Add Recipe' option")
            addRecipeFile.close()
        else:
            stringOutput = openingText
            for recipeItem in range(len(directory)):
                stringOutput = stringOutput + directory[recipeItem][:-4] + "\n"
                displayFile = open(displayActLoc, 'w')
                displayFile.write("cook:dili:list"+stringOutput)
                displayFile.close()

