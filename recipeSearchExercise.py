import requests
from pprint import pprint


# create function to fetch the data from api
def recipie_search(ingredient, amount_ingredient):
    app_id = 'your_app_id'
    app_key = 'your_app_key'
    base_url = 'https://api.edamam.com/api/recipes/v2'
    url = f'{base_url}?type=public&q={ingredient}&app_id={app_id}&app_key={app_key}&ingr={amount_ingredient}'
    result = requests.get(url)
    data = result.json()

    return data['hits']


#  create function which calls the recipe_search and interacts with the user
def run():
    #  interact with the user
    ingredient = input("Enter an ingredient: ")
    amount_ingredient = input("How many ingredients? : ")
    text_file = input("Do you want to save the results into file? y/n ")

    # call the  recipe search and save results to a variable
    results = recipie_search(ingredient, amount_ingredient)

    #  create the txt file
    with open('recipies2.txt', 'wt') as f:
        f.write(f'The recipes with ingredient {ingredient} are shown below:  \n')

        # iterate the results returned create more variables and assign data
        for result in results:
            recipe = result['recipe']
            label = recipe['label']
            ingredients = recipe['ingredientLines']
            text_data = f'Recipe: {label} \n Ingredients: {ingredients}  \n'

            #  if else block statement
            if text_file != 'y':
                #  print the results in the console
                pprint(f'Recipe: {label}')
                pprint('Ingredients: ')
                for ingredient in ingredients:
                    pprint(ingredient)

                print()


            else:
                # print the results to a file only
                f.write(text_data + "\n")


#  call the main function which  gathers user input and calls the recipie_search
run()
