# Author: Julie Bosley
# Updated: 02/08/2025
# Description: Microservice for directing to different shopping list functionality

import time
import os

# file Paths
cookbookActLoc = './ActionFolder/cookbookActions.txt'
displayActLoc = './ActionFolder/displayActions.txt'
homepageActLoc = './ActionFolder/homePageActions.txt'
shopListActLoc = './ActionFolder/shoppingListActions.txt'

# Shoppinglist sub pages
dispRecpCartActLoc = './ActionFolder/displayRecipesCartActions.txt'
addRecipCartActLoc = './ActionFolder/addRecipeCartActions.txt'
removeRecipeCartActLoc = './ActionFolder/removeMealActions.txt'
clearCartActLoc = './ActionFolder/clearCart.txt'
generateListActLoc = './ActionFolder/generateShoppingList.txt'


shoppingListMessage = "Welcome to your Shopping List.\n Actions:\n"
action1 = "1) Display Recipes in Cart\n"
action2 = "2) Add Recipe to Cart\n"
action3 = "3) Remove Recipe from Cart\n"
action4 = "4) Clear Cart\n"
action5 = "5) Generate shopping list\n"
action6 = "6) Go to Home\n"
action7 = "7) Go to Cookbook Editor\n"
shoppingListWelcome = shoppingListMessage + action1 + action2 + action3 + action4 + action5 + action6 + action7

while True:
    ogTime = os.path.getmtime(shopListActLoc)
    while (os.path.getmtime(shopListActLoc) <= ogTime):
        time.sleep(1)

    with open(shopListActLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()

        # Display Home Page
        if read_data == "start":
            dispFile = open(displayActLoc, 'w')
            dispFile.write("shop:disp" + shoppingListWelcome)
            dispFile.close()

        # Selector redirects
        if read_data == "1":  # displays recipes in Cart
            addRecipeFile = open(dispRecpCartActLoc, 'w')
            addRecipeFile.write("start")
            addRecipeFile.close()
        elif read_data == "2":  # add recipe to cart
            addRecipeFile = open(addRecipCartActLoc, 'w')
            addRecipeFile.write("start")
            addRecipeFile.close()
        elif read_data == "3": # Remove Recipe from Cart
            addRecipeFile = open(removeRecipeCartActLoc, 'w')
            addRecipeFile.write("start")
            addRecipeFile.close()
        elif read_data == "4":  # Clears Cart
            addRecipeFile = open(clearCartActLoc, 'w')
            addRecipeFile.write("start")
            addRecipeFile.close()
        elif read_data == "5": # Generates shopping list
            cookFile = open(generateListActLoc, 'w')
            cookFile.write("start")
            cookFile.close()
        elif read_data == "6": # go to home page
            cookFile = open(homepageActLoc, 'w')
            cookFile.write("start")
            cookFile.close()
        elif read_data == "7": # goes to cookbook
            cookFile = open(cookbookActLoc, 'w')
            cookFile.write("start")
            cookFile.close()

    # Redirect to Shopping List
