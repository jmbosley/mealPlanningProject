# Author: Julie Bosley
# Updated: 02/08/2025
# Description: Microservice for directing to different cookbook functionality

import time
import os
# file Paths
cookbookActLoc = './ActionFolder/cookbookActions.txt'
displayActLoc = './ActionFolder/displayActions.txt'
homepageActLoc = './ActionFolder/homePageActions.txt'
shopListActLoc = './ActionFolder/shoppingListActions.txt'

# Cookbook sub pages
addRecipeActLoc = './ActionFolder/addRecipeActions.txt'
displayRecipeListLoc = './ActionFolder/displayRecipeList.txt'
deleteRecipeLoc = './ActionFolder/deleteRecipeActions.txt'



cookbookMessage = "Welcome to your Cookbook.\n Actions:\n"
action1 = "1) Display Recipe List\n"
action2 = "2) Add Recipe\n"
action3 = "3) Edit Recipe\n"
action4 = "4) Delete Recipe\n"
action5 = "5) Display Recipe\n"
action6 = "6) Go to Home\n"
action7 = "7) Go to Shopping List Editor\n"
cookbookwelcome = cookbookMessage + action1 + action2 + action3 + action4 + action5 + action6 + action7

while True:
    ogTime = os.path.getmtime(cookbookActLoc)
    while (os.path.getmtime(cookbookActLoc) <= ogTime):
        time.sleep(1)        

    with open(cookbookActLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()  
    
        # Display Home Page
        if read_data == "start":
            dispFile = open(displayActLoc, 'w')
            dispFile.write("cook:disp" + cookbookwelcome)
            dispFile.close()

        # Selector redirects
        if read_data == "1": # displays Recipe List
            addRecipeFile = open(displayRecipeListLoc, 'w')
            addRecipeFile.write("start")
            addRecipeFile.close()
        elif read_data == "2": # add recipe
            addRecipeFile = open(addRecipeActLoc, 'w')
            addRecipeFile.write("start")
            addRecipeFile.close()
        elif read_data == "3":
            print("3) Edit Recipe\n")
        elif read_data == "4": # deletes recipe
            addRecipeFile = open(deleteRecipeLoc, 'w')
            addRecipeFile.write("start")
            addRecipeFile.close()
        elif read_data == "5":
            print("5) Display Recipe\n")
        elif read_data == "6":
            cookFile = open(homepageActLoc, 'w')
            cookFile.write("start")
            cookFile.close()
        elif read_data == "7":
            cookFile = open(shopListActLoc, 'w')
            cookFile.write("start")
            cookFile.close()
            

    # Redirect to Shopping List
