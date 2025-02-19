# Author: Julie Bosley
# Updated: 02/08/2025
# Description: Microservice for homepage functionality

import time
import os
# file Paths
cookbookActLoc = './ActionFolder/cookbookActions.txt'
displayActLoc = './ActionFolder/displayActions.txt'
homepageActLoc = './ActionFolder/homePageActions.txt'
shopListActLoc = './ActionFolder/shoppingListActions.txt'

# Welcome Page
welcomeHeader = "Welcome to the Shopping List Generator!\nThis Program allows you to save your recipes and use them to generate a shopping list without the hassel of having to re-write every single ingredient.\n\n"
prompt = "Which Page would you like to access?\n"
option1 = "1) Cookbook\n"
option2 = "2) Shopping List\n"
homeMessage = welcomeHeader + prompt + option1 + option2

# Display Home Page
dispFile = open(displayActLoc, 'w')
dispFile.write("home:disp" + homeMessage)
dispFile.close()

while True:
    ogTime = os.path.getmtime(homepageActLoc)
    while (os.path.getmtime(homepageActLoc) <= ogTime):
        time.sleep(1)

    with open(homepageActLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()

        # Redirect to Cookbook
        if read_data == "1":
            cookFile = open(cookbookActLoc, 'w')
            cookFile.write("start")
            cookFile.close()
        elif read_data == "2":
            shopFile = open(shopListActLoc, 'w')
            shopFile.write("start")
            shopFile.close()

    # Redirect to Shopping List
