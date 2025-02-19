# Author: Julie Bosley
# Updated: 02/08/2025
# Description: Microservice for displaying text to user

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

while True:
    ogTime = os.path.getmtime(displayActLoc)
    while (os.path.getmtime(displayActLoc) <= ogTime):
        time.sleep(1)
        
    # open and read display actions
    with open(displayActLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()  
    
    # Display message
    with open(displayActLoc, "r+") as f:
        # homePage Actions
        if read_data[:4] == "home":
            print(read_data[9::])
            userInput = str(input("Enter 1 or 2: "))
            homepageFile = open(homepageActLoc, 'w')
            homepageFile.write(userInput)
            homepageFile.close()
        # cookbook actions
        elif read_data[:4] == "cook":
            if read_data[5:9] == "disp":
                print(read_data[9::])
                userInput = str(input("Enter the item number: "))
                cookbookFile = open(cookbookActLoc, 'w')
                cookbookFile.write(userInput)
                cookbookFile.close()
            elif read_data[5:9] == "addr":
                if read_data[10:] == "gett":
                    print("Please type the name of your new recipe below")
                    userInput = str(input(": "))
                    addRecipeFile = open(addRecipeActLoc, 'w')
                    addRecipeFile.write(userInput)
                    addRecipeFile.close()
                elif read_data[10:] == "exis":
                    print(userInput + " already exists.")
                    # go back to cookbook
                    cookFile = open(cookbookActLoc, 'w')
                    cookFile.write("start")
                    cookFile.close()
                elif read_data[10:] == "succ":
                    print(userInput+ " was successfully added!")
                    cookFile = open(cookbookActLoc, 'w')
                    cookFile.write("start")
                    cookFile.close()
            elif read_data[5:9] == "dili":
                if read_data[10:14] == "empt":
                    print(read_data[14:])
                    cookFile = open(cookbookActLoc, 'w')
                    cookFile.write("start")
                    cookFile.close()
                if read_data[10:14] == "list":
                    print(read_data[14:])
                    userInput = input("Hit enter to return to cookbook menu.")
                    cookFile = open(cookbookActLoc, 'w')
                    cookFile.write("start")
                    cookFile.close()
            elif read_data[5:9] == "dele":
                if read_data[10:14] == "star" or read_data[10:14] == "conf":
                    print(read_data[14:])
                    userInput = input()
                    deleteFile = open(deleteRecipeLoc, 'w')
                    deleteFile.write(userInput)
                    deleteFile.close()
                elif read_data[10:14] == "succ" or read_data[10:14] == "fail":
                    print(read_data[14:])
                    cookFile = open(cookbookActLoc, 'w')
                    cookFile.write("start")
                    cookFile.close()
        # shopping list actions
        elif read_data[:4] == "shop":
            if read_data[5:9] == "disp":
                print(read_data[9::])
                userInput = str(input("Enter the item number: "))
                shopListFile = open(shopListActLoc, 'w')
                shopListFile.write(userInput)
                shopListFile.close()


# send query back
