import time
import os

# file Paths
cookbookActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/cookbookActions.txt'
displayActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/displayActions.txt'
homepageActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/homePageActions.txt'


# Cookbook sub pages
addRecipeActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/addRecipeActions.txt'

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
                    print("Your cookbook is empty. Please add some recipes using 'Add Recipe' option")
                    cookFile = open(cookbookActLoc, 'w')
                    cookFile.write("start")
                    cookFile.close()
                if read_data[10:14] == "list":
                    print(read_data[14:])
                    userInput = input("Type anything then hit enter to return to cookbook menu.")
                    cookFile = open(cookbookActLoc, 'w')
                    cookFile.write("start")
                    cookFile.close()

        # shopping list actions
        elif read_data[:4] == "shopl":
            print("shopl")


# send query back
