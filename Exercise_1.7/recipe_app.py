from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func
from sqlalchemy.sql import select 


#Connecting SQLALchemy with databse
engine = create_engine("mysql://cf-python:password@localhost/task_database")

#Create declaritive base
Base = declarative_base()

#Define Recipe model
class Recipe(Base):
    __tablename__ = "Recipes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe ID: {self.id} - {self.name}"

#Create all defined rables in database
Base.metadata.create_all(engine)

#Create Session
Session = sessionmaker(bind=engine)
session = Session()

#Define calculate_difficulty function
def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        return "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        return "Medium"
    elif cooking_time >= 10 and len(ingredients) > 4:
        return "Intermediate"
    else:
        return "Hard"


#Define insert_recipe function
def insert_recipe(name, ingredients, cooking_time):
    #Calculate difficulty of recipe
    difficulty = calculate_difficulty(cooking_time, ingredients)

    #Convert ingredients list to comma seperated string
    ingredients_string = ", ".join(ingredients)

    #Create a new Recipe instance
    new_recipe = Recipe(name=name, ingredients= ingredients_string, cooking_time= cooking_time, difficulty= difficulty)

    #Add new recipe to session
    session.add(new_recipe)

    #Commit changes
    session.commit()
    print("-"*10)
    print("Recipe added successfully!")
    print("-"*10)

#Define create_recipe function
def create_recipe():
    # Collect recipe details
    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time of the recipe (in minutes): "))
    ingredients = input("Enter the ingredients of the recipe (separated by commas): ").split(", ")

    # Insert the recipe into the database
    insert_recipe(name, ingredients, cooking_time)

#Define view_recipes function
def view_recipes():
    recipes = session.query(Recipe).all()
    print("-"*10)
    print("Available Recipes:")
    print("-"*10)
    print()
    if not recipes:
        print("No recipes found")
        return

    for recipe in recipes:
        print("Name:", recipe.name)
        print("Ingredients:", recipe.ingredients)
        print("Cooking Time:", recipe.cooking_time, "minutes")
        print("Difficulty:", recipe.difficulty)
        print("\n")

    


#define search_recipe function
def search_recipe():
    #Retrieve ingredients from Recipes table
    all_ingredients = session.query(func.distinct(Recipe.ingredients)).all()

    #Extract ingredients from fetched results
    all_ingredients = [ingredient[0] for ingredient in all_ingredients]

    #Display all ingredients to user with unique numbering
    print("-"*10)
    print("Available ingredients:")
    print("-"*10)
    ingredient_dict = {}
    count = 1
    for ingredients_str in all_ingredients:
        ingredients_list = ingredients_str.split(", ")
        for ingredient in ingredients_list:
            print(f"{count}. {ingredient}")
            ingredient_dict[count] = ingredient
            count += 1
    
    #Promt user to select ingredient to search for
    ingredient_index = int(input("Enter the number for ingredient you want to search for: "))
    search_ingredient = ingredient_dict.get(ingredient_index)

    #Search for recipes containing ingredient
    search_results = session.query(Recipe).filter(Recipe.ingredients.like(f"%{search_ingredient}%")).all()

    #Display search results to user
    print("-"*10)
    print("Search Results:")
    print("-"*10)
    if search_results:
        for result in search_results:
            print("Name:", result.name)
            print("Ingredients:", result.ingredients)
            print("Cooking Time:", result.cooking_time, "minutes")
            print("Difficulty:", result.difficulty)
            print("-"*10)
    else:
        print("-"*10)
        print("No recipes found containing", search_ingredient)
        print("-"*10)


#Define update_recipe function
def update_recipe():
    #Fetch all recipes from database and list them to user
    recipes= session.query(Recipe).all()
    print("-"*10)
    print("Available Recipes:")
    print("-"*10)
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe.name}")
        print()

    #Prompt user to select recipe to update
    recipe_index = int(input("Enter the number of the recipe you want to update: ")) -1

    #Check if the Recipe exists
    if 0 <= recipe_index < len(recipes):
        recipe = recipes[recipe_index]

        #Prompt user to select column to update
        print("Columns available to update: name, cooking_time, ingredients")
        column = input("Enter the column to be updated: ")


        #Prompt user for the new value
        new_value = input("Enter the new value: ")

        #Convert new value to integer for cooking_time
        if column == 'cooking_time':
            new_value = int(new_value)

        #Update the specified column
        setattr(recipe, column, new_value)

        #Recalculate difficulty if updating cooking_time or ingredients
        if column == 'cooking_time' or column == 'ingredients':
            recipe.difficulty = calculate_difficulty(recipe.cooking_time, recipe.ingredients.split(", "))

        #Commit changes
        session.commit()
        
        print("\nRecipe updated successfully!\n")
    else:
        print("-"*10)
        print("Error: Recipe not found")
        print("-"*10)


#Define delete_recipe function
def delete_recipe():
    #Fetch all recipes and list them to user
    recipes = session.query(Recipe).all()
    print("-"*10)
    print("Available Recipes:")
    print("-"*10)
    for index, recipe in enumerate(recipes, start=1):
        print(f"{index}. {recipe.name}")
        
    #Prompt user to select recipe to delete
    recipe_index = int(input("Enter the number of the recipe you would like to delete: "))

    #Check if recipe exists
    if 0 <= recipe_index < len(recipes):
        recipe = recipes[recipe_index]

        #Delete specific recipe
        session.delete(recipe)

        #Commit changes
        session.commit()
        print("Recipe successfully deleted!\n")
    else:
        print("-"*10)
        print("Error: recipe not found")
        print("-"*10)

#Define main menu function
def main_menu():
    while True:
        print("-"*20)
        print("RECIPE APP")
        print("-"*20)
        print("\nMain Menu: ")
        print("1. Create new Recipe")
        print("2. View all Recipes")
        print("3. Search for Recipe by Ingredient")
        print("4. Update an existing Recipe")
        print("5. Delete a Recipe")
        print("6. Exit\n")

        choice = input("Enter your choice: ")
        print()

        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            search_recipe()
        elif choice == '4':
            update_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("-"*10)
            print("Invalid choice, please try again")
            print("-"*10)

    #Close session before exiting
    session.close()
    print("Session closed.")

#Call main menu function
main_menu()