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
    ogTime = os.path.getmtime(generateListActLoc)
    while (os.path.getmtime(generateListActLoc) <= ogTime):
        time.sleep(1)

    with open(generateListActLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()

    # Check if meal plan is empty
    if read_data == "start":
        with open(mealPlanLoc, 'r') as mealPlan:
            firstCharacter = mealPlan.read(1)
            if not firstCharacter:
                # if it is then user is notified
                dispFile = open(displayActLoc, 'w')
                dispFile.write(
                    "shop:addr:disp:Your meal plan is empty, please add some meals to it in order to generate a shopping list.\n")
                dispFile.close()
            else:
                # else if all recipes in meal plan exist in cookbook
                f = open(mealPlanLoc, "r")
                read_data = f.read().splitlines()
                print(read_data)
                f.close()
                directory = os.listdir(cookbookFolderLoc)
                if len(directory) == 0:  # directry is empty
                    dispFile = open(displayActLoc, 'w')
                    dispFile.write(
                        "shop:addr:disp:Your cookbook is empty. Please add some recipes using 'Add Recipe' option")  # get the title
                    dispFile.close()
                else:
                    cookbook = []
                    outMessage = ""
                    shoppingListFile = open(shoppingListLoc, "w").close
                    for recipeItem in range(len(directory)):
                        recipeName = directory[recipeItem][:-4]
                        cookbook.append(recipeName)
                    for recipe in read_data:
                        if recipe not in cookbook:
                            outMessage = outMessage + "The recipe " + recipe + " is not in your Cookbook.\n"
                        else:
                            recipeInstructionsFile = open(cookbookFolderLoc + recipe + ".txt", "r")
                            recipeInstructions = recipeInstructionsFile.read()
                            recipeInstructionsFile.close()

                            shoppingListFile = open(shoppingListLoc, "a")
                            shoppingListFile.write(recipeInstructions+ "\n")
                            shoppingListFile.close()
                    editor = "gnome-terminal -e 'gedit " + shoppingListLoc + "'"
                    os.system(editor)

                    dispFile = open(displayActLoc, 'w')
                    dispFile.write(outMessage + "shop:addr:disp:Shopping List Successfully Generated.\n")
                    dispFile.close()