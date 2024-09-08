class Recipe:
    all_ingredients = set()

#Initiate recipe object with name, ingredients, cooking time and difficulty
    def __init__(self, name, ingredients, cooking_time):
        self._name = name
        self._ingredients = ingredients
        self._cooking_time= cooking_time
        self._difficulty = None 
        self.update_all_ingredients()

#Return the name of recipe
    def get_name(self):
        return self._name

#Set the name of recipe
    def set_name(self, name):
        self._name = name

#Return the cooking time of recipe
    def get_cooking_time(self):
        return self._cooking_time

#Set cooking time of recipe
    def set_cooking_time(self, cooking_time):
        self._cooking_time = cooking_time

#Return list of ingredients for recipe
    def get_ingredients(self):
        return self._ingredients

#Add ingredients to recipe and update global ingredients list
    def add_ingredients(self, *ingredients):
        self._ingredients.extend(ingredients)
        self.update_all_ingredients()

#Update ingredients of recipe to all_ingredients 
    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self._ingredients)

#Search through recipe list for specific ingredient
    def search_ingredients(self, ingredients):
        return ingredients in self._ingredients

#Get difficulty for recipe, calculate if not already done
    def get_difficulty(self):
        if not self._difficulty:
            self.calculate_difficulty()
        return self._difficulty

#Calculate the difficulty of recipe
    def calculate_difficulty(self, ):
        if self._cooking_time < 10 and len(self._ingredients)< 4:
            self._difficulty = "Easy"
        elif self._cooking_time < 10 and len(self._ingredients)>= 4:
            self._difficulty = "Medium"
        elif self._cooking_time >= 10 and len(self._ingredients)< 4:
            self._difficulty = "Intermediate"
        elif self._cooking_time >= 10 and len(self._ingredients)>= 4:
            self._difficulty = "Hard"

#Return string of recipe, name, ingredients, cooking time, difficulty
    def __str__(self):
        return f"Recipe Name: {self._name}\nIngredients: {','.join(self._ingredients)}\nCooking Time: {self._cooking_time} minutes\nDifficulty: {self.get_difficulty()}\n"

#Search and print recipes that contain a specific ingredient
def recipe_search(data, search_term):
    print(f"Recipes that contain '{search_term}':")
    for recipe in data:
        if recipe.search_ingredients(search_term):
            print(recipe)



#Create Recpie instances
tea = Recipe("Tea", ["Tea Leaves", "Surgar", "Water"], 5)
coffee = Recipe("Coffee", ["Coffee Powder", "Sugar", "Water"], 5)
cake = Recipe("Cake", ["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"], 50)
smoothie = Recipe("Banana Smoothie", ["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"], 5)


#Add recipes to list
recipes_list = [tea, coffee, cake, smoothie]

#Display string for recipe
for recipe in recipes_list:
    print(recipe)

#Search for recipes that contain certain ingredients
for ingredients in ["Water", "Sugar", "Bananas"]:
    recipe_search(recipes_list, ingredients)