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
# Edit Recipe

# ShoppingList sub pages
dispRecpCartActLoc = './ActionFolder/displayRecipesCartActions.txt'
addRecipCartActLoc = './ActionFolder/addRecipeCartActions.txt'
removeRecipeCartActLoc = './ActionFolder/removeMealActions.txt'
generateListActLoc = './ActionFolder/generateShoppingList.txt'
mealPlanLoc = './ActionFolder/mealPlan.txt'

# wait for que to start
while True:
    ogTime = os.path.getmtime(dispRecpCartActLoc)
    while (os.path.getmtime(dispRecpCartActLoc) <= ogTime):
        time.sleep(1)

    with open(dispRecpCartActLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()

        # Display Home Page
        if read_data == "start":
            # read mealPlan.txt
            with open(mealPlanLoc, "r+") as f:
                read_data = f.read()
                # send mealPlan.txt info to display
                dispFile = open(displayActLoc, 'w')
                dispFile.write("shop:disp:plan" + read_data)
                dispFile.close()