import time
import os
# file Paths
cookbookActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/cookbookActions.txt'
displayActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/displayActions.txt'
homepageActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/homePageActions.txt'

# Cookbook sub pages
addRecipeActLoc = '/home/jmbosley/Documents/mealPlanningProjectV2/ActionFolder/addRecipeActions.txt'

# Display Text
recipeTitle = "Title: "
recipeProduce = "Produce:\n"


while True:
    ogTime = os.path.getmtime(addRecipeActLoc)
    while (os.path.getmtime(addRecipeActLoc) <= ogTime):
        time.sleep(1) 
    with open(addRecipeActLoc, "r+") as f:
        read_data = f.read()
        f.seek(0)
        f.truncate()
        
# Get Recipe Name and create File
    if read_data == "start":
        dispFile = open(displayActLoc, 'w')
        dispFile.write("cook:addr")
        dispFile.close()
    else:
        newRecipe = open(read_data".txt","w")
# Add Produce
# Add Meat
# Add Canned
# Add Dairy
# Add Other

     

     
    
        # Display Home Page
        

        # Redirect to Cookbook
        if read_data == "1":
            print("1) Display Recipe List\n")
        elif read_data == "2":
            print("2) Add Recipe\n")
        elif read_data == "3":
            print("3) Edit Recipe\n")
        elif read_data == "4":
            print("4) Delete Recipe\n")
        elif read_data == "5":
            print("5) Display Recipe\n")
        elif read_data == "6":
            print("6) Go to Home\n")
        elif read_data == "7":
            print("7) Go to Shopping List Editor\n")
