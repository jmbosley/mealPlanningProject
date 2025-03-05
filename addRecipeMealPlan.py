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


while True:
    ogTime = os.path.getmtime(addRecipCartActLoc)
    while (os.path.getmtime(addRecipCartActLoc) <= ogTime):
        time.sleep(1)

    with open(addRecipCartActLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()

    # Ask user for which recipe they want to add to the meal plan
    if read_data == "addr:star":
        dispFile = open(displayActLoc, 'w')
        dispFile.write("shop:addr:rece:Which recipe would you like to add to the meal plan?\n") # get the title
        dispFile.close()
    elif read_data == "clear:star":
        dispFile = open(displayActLoc, 'w')
        dispFile.write("shop:addr:rece:Are you sure you want to clear your meal plan? (yes/no)\n")  # get the title
        dispFile.close()
    elif read_data == "yes":
        mealPlanClear = open(mealPlanLoc, "w").close
        dispFile = open(displayActLoc, 'w')
        dispFile.write("shop:addr:disp:Your Meal Plan has been cleared.\n")  # get the title
        dispFile.close()
    else:
        recipe = read_data
        # check if recipe exists
        directory = os.listdir(cookbookFolderLoc)
        if len(directory) == 0:  # directry is empty
            dispFile = open(displayActLoc, 'w')
            dispFile.write("shop:addr:disp:Your cookbook is empty. Please add some recipes using 'Add Recipe' option")  # get the title
            dispFile.close()
        else:
            exists = False
            for recipeItem in range(len(directory)):
                recipeName = directory[recipeItem][:-4]
                if recipeName == recipe:
                    exists = True
            if exists:
                # write to meal plan with data
                f = open(mealPlanLoc, "a")
                f.write(recipe + "\n")
                f.close()

                dispFile = open(displayActLoc, 'w')
                dispFile.write(
                    "shop:addr:disp:" + recipe + " was successfully added to meal plan.\n")  # get the title
                dispFile.close()

            else:
                # if not then tell user
                dispFile = open(displayActLoc, 'w')
                dispFile.write(
                    "shop:addr:disp:This recipe does not exist in your cookbook.")  # get the title
                dispFile.close()

