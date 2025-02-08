# Author: Julie Bosley
# Updated: 02/08/2025
# Description: Microservice for adding new recipe

import time
import os
# file Paths
cookbookActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/cookbookActions.txt'
displayActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/displayActions.txt'
homepageActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/homePageActions.txt'

# Cookbook sub pages
addRecipeActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/addRecipeActions.txt'
cookbookFolderLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/Cookbook/'

# Display Text
recipeTitle = "Title: "
divider = "-----------------------"
ingredientTypes = "Produce:\n\n"+divider+"\nMeat:\n\n"+divider+"\nCanned:\n\n"+divider+"\nDairy:\n\n"+divider+"\nOther:\n\n"


while True:
    ogTime = os.path.getmtime(addRecipeActLoc)
    while (os.path.getmtime(addRecipeActLoc) <= ogTime):
        time.sleep(1) 
    with open(addRecipeActLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()
        
# Get Recipe Name and create File
    if read_data == "start":
        dispFile = open(displayActLoc, 'w')
        dispFile.write("cook:addr:gett") # get the title
        dispFile.close()
    else:
        # Does this recipe already exist?
        if os.path.isfile(cookbookFolderLoc + read_data + '.txt'):
            # if not create the recipe
            dispFile = open(displayActLoc, 'w')
            dispFile.write("cook:addr:exis") # file already exists
            dispFile.close()
        else:
            newRecipePath = cookbookFolderLoc + read_data + '.txt'
            newRecipe = open(newRecipePath,"w")
            newRecipe.write(recipeTitle+read_data+'\n'+ingredientTypes) # fill in template
            newRecipe.close()
            editor = "gnome-terminal -e 'gedit "+newRecipePath+"'"
            os.system(editor)
            ogTime = os.path.getmtime(newRecipePath)
            while (os.path.getmtime(newRecipePath) <= ogTime):
                time.sleep(1)
            dispFile = open(displayActLoc, 'w')
            dispFile.write("cook:addr:succ")  # successfully added
            dispFile.close()
