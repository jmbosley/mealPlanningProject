import time
import os

# file Paths
cookbookActLoc = './ActionFolder/cookbookActions.txt'
displayActLoc = './ActionFolder/displayActions.txt'
homepageActLoc = './ActionFolder/homePageActions.txt'
shopListActLoc = './ActionFolder/shoppingListActions.txt'

# Cookbook sub pages
addRecipeActLoc = './ActionFolder/addRecipeActions.txt'
deleteRecipeLoc = './ActionFolder/deleteRecipeActions.txt'
cookbookFolderLoc = './Cookbook/'
editRecipeLoc = './ActionFolder/editRecipeActions.txt'


# Edit Recipe

# ShoppingList sub pages
dispRecpCartActLoc = './ActionFolder/displayRecipesCartActions.txt'
addRecipCartActLoc = './ActionFolder/addRecipeCartActions.txt'
removeRecipeCartActLoc = './ActionFolder/removeMealActions.txt'
generateListActLoc = './ActionFolder/generateShoppingList.txt'
shopListActLoc = './ActionFolder/shoppingListActions.txt'
mealPlanLoc = './ActionFolder/mealPlan.txt'
shoppingListLoc = './ActionFolder/ShoppingList.txt'

while True:
    ogTime = os.path.getmtime(editRecipeLoc)
    while (os.path.getmtime(editRecipeLoc) <= ogTime):
        time.sleep(1)

    with open(editRecipeLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()

    if read_data == "start":
        dispFile = open(displayActLoc, 'w')
        dispFile.write("cook:edit:rece:Which recipe would you like to edit?\n")  # get the title
        dispFile.close()
    else:
        # check if recipe exists
        directory = os.listdir(cookbookFolderLoc)
        if len(directory) == 0:  # directry is empty
            dispFile = open(displayActLoc, 'w')
            dispFile.write(
                "cook:edit:disp:Your cookbook is empty. Please add some recipes using 'Add Recipe' option")  # get the title
            dispFile.close()
        else:
            cookbook = []
            for recipeItem in range(len(directory)):
                recipeName = directory[recipeItem][:-4]
                cookbook.append(recipeName)
            if read_data not in cookbook:
                dispFile = open(displayActLoc, 'w')
                dispFile.write(
                    "cook:edit:disp:The recipe " + read_data + " is not in your Cookbook.\n")  # get the title
                dispFile.close()
            else:
                editor = "gnome-terminal -e 'gedit " + cookbookFolderLoc + read_data + ".txt'"
                os.system(editor)

            dispFile = open(displayActLoc, 'w')
            dispFile.write(
                "cook:edit:disp: Recipe Successfully Updated.\n")
            dispFile.close()