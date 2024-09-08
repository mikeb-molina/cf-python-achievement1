# Empty list for recipes and ingredients
recipes_list= []
ingredients_list=[]

# Function to take user input for recipe
def take_recipe():
    name= str(input("Enter the name of a recipe: "))
    cooking_time= int(input("Enter cooking time in minutes: "))
    ingredients= list(input("Enter the ingredients, seperated by comma: ").split(","))
    recipe ={
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients
    }

    return recipe

# Initial user prompt
n = int(input("How many recipes would you like to enter? "))

# Iterates through number of given recipes
for i in range(n):
    recipe=take_recipe()

    # checks if ingredient should be added to list
    for ingredient in recipe["ingredients"]:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)

    recipes_list.append(recipe)

# Iterates through recipe_list to determine difficulty
for recipe in recipes_list:
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Easy"
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) > 4:
        recipe["difficulty"] = "Medium"
    if recipe["cooking_time"] > 10 and len(recipe["ingredients"]) < 4:
        recipe["difficulty"] = "Intermediate"
    if recipe["cooking_time"] > 10 and len(recipe["ingredients"]) >= 4:
        recipe["difficulty"] = "Hard"

#Iterates through recipe_list to display information
for recipe in recipes_list:
    print("Recipe: ", recipe["name"])
    print("Cooking time (minutes): ", recipe["cooking_time"])
    print("Ingredients: ")
    for ingredient in recipe["ingredients"]:
        print(ingredient)
    print("Difficulty: ", recipe["difficulty"])


#Displays all ingredients in alphabetical order
def all_ingredients():
    print("Ingredients Available accross all recipes")
    print("_______________________")
    ingredients_list.sort()
    for ingredient in ingredients_list:
        print(ingredient)

all_ingredients()
    