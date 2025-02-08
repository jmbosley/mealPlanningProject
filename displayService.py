import time
import os

# file Paths
cookbookActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/cookbookActions.txt'
displayActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/displayActions.txt'
homepageActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/homePageActions.txt'


# CookBook


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
                print("add Recipe")
        # shopping list actions
        elif read_data[:4] == "shopl":
            print("shopl")


# send query back
