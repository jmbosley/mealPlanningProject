import time

def recipe_check(action_path, meal_path):
    """Monitors an action file for a meal to remove and if a meal is found, it will try to remove it from the plan"""

    while True:
        time.sleep(1)  # Check for changes every 1 second

        with open(action_path, 'r') as f:
            recipe = f.read()  # Read in action file
            recipe = recipe[:-1]

        try:
            """Test if content is something other than done, none, or empty"""
            if recipe != 'done' and recipe != 'none' and recipe != '':
                i = 0  # Set test for updates
                meal_array = []  # Set empty meal plan array
                """Read in meal plan and assign to the meal plan array then close file"""
                meal_plan = open(meal_path, 'r')
                for meal in meal_plan:
                    meal_array.append(meal[:-1])
                meal_plan.close()
                """Test the read in recipe against the meal plan array and remove if found"""
                for item in meal_array:
                    if item == recipe:
                        meal_array.remove(recipe)
                        i = 1
                """If recipe was removed, write done to action file and write back new plan"""
                if i == 1:
                    action = open(action_path, 'w')
                    action.write('done\n')
                    action.close()
                    with open(meal_path, 'w') as m:
                        for item in meal_array:
                            m.write(item + "\n")
                elif i == 0:  # If no recipe was removed, write none to action file
                    action = open(action_path, 'w')
                    action.write('none\n')
                    action.close()

        except ValueError:
            """Do nothing on error and try again"""


if __name__ == '__main__':
    recipe_check('./ActionFolder/removeMealActions.txt', './ActionFolder/mealPlan.txt')
