import pickle

#Creates recipe input based on user input
def take_recipe():
    name= str(input("Enter the name of the recipe: "))
    cooking_time= int(input("Enter the cooking time: "))
    ingredients= [
        ingredient.strip().capitalize()
        for ingredient in input("Enter the ingredients seperated by comma: ").split(",")
    ]

    difficulty = calc_difficulty(cooking_time, ingredients)
    recipe= {
        "recipe_name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty
    }
    return recipe

#Creates difficulty of the recipe
def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty= "Easy"
    if cooking_time < 10 and len(ingredients) >= 4:
        difficulty= "Medium"
    if cooking_time >= 10 and len(ingredients) < 4:
        difficulty= "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        difficulty= "Hard"
        return difficulty

#User enters name of file
filename = input("Enter the name of the file you want to save to: ")

#Try to open the file, if no file exists create one
try:
    file= open(filename, "rb")
    data= pickle.load(file)
    print("File loaded successfully")
#Error for no file found
except FileNotFoundError:
    print("No files match that name - createing new file")
    data = {"recipe_list": [], "all_ingredients": []}
#General Error
except:
    print("Oops, something went wrong try again")
    data = {"recipe_list": [], "all_ingredients": []}
#Close file
else:
    file.close()
#Extracts data from two variables
finally:
    recipe_list = data["recipe_list"]
    all_ingredients = data["all_ingredients"]

#Ask user how many recipes to enter
n = int(input("How many recipes would you like to enter?: "))

#Add ingreient to all_ingredients for each recipe
for i in range(0, n):
    recipe = take_recipe()
    for element in recipe["ingredients"]:
        if element not in all_ingredients:
            all_ingredients.append(element)
    recipe_list.append(recipe)
    print("Recipe added successfully")


#Create new dictionary with updated data
data = {"recipe_list": recipe_list, "all_ingredients": all_ingredients}

#Opens file and saves data to it
update_file = open(filename, "wb")
pickle.dump(data, update_file)
#Close file
update_file.close()
print("Recipe file has been updated")