import pickle

#Display recipe
def display_recipe(recipe):
    print("-----")
    print("Recipe: ", recipe["name"])
    print("Cooking Time (min): ", recipe["cooking_time"])
    print("Ingredients: ")
    for ele in recipe["ingredients"]:
        print("- ", ele)
    print("Difficulty: ", recipe["difficulty"])

#Search ingredients
def search_ingredients(data):
    #numbers each element in list
    available_ingredients = enumerate(data["all_ingredients"])
    #Add numbered data into list
    numbered_list= list(available_ingredients)
    print("Available Ingredients: ")

    for ele in numbered_list:
        print(ele[0], ele[1])
    try:
        num= int(input("Enter the number for the ingreients you would like to search: "))
        ingredient_searched = numbered_list[num][1]
        print("Searching for recipes with ", ingredient_searched, "...")
    except ValueError:
        print("Only numbers allowed")
    except:
        print("Number entered does not match ingredients list")
    else:
        for ele in data["recipe_list"]:
            if ingredient_searched in ele["ingredients"]:
                print(ele)
    

filename = input("Enter the name of the file you want to save to: ")

try:
    file = open(filename, "rb")
    data = pickle.load(file)
    print("File loaded successfully")
except FileNotFoundError:
    print("No files match that name - please try again")
except:
    print("Oops, there was an unexpected error")
else:
    file.close()
    search_ingredients(data)