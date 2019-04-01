import requests

import ssl
ssl._create_default_https_context = ssl._create_unverified_context

def getRecipeByIngredients(ingredients):
    payload = {
        'fillIngredients': False,
        'ingredients': ingredients,
        'limitLicense': False,
        #'number': 5,
        #'ranking': 1
    }

    api_key = "c7135f2f8bmsh9b6b78982ba931fp135282jsn85ad20e4d037"

    endpoint = "https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/recipes/findByIngredients"


    headers={
        "X-Mashape-Key": "c7135f2f8bmsh9b6b78982ba931fp135282jsn85ad20e4d037",

    }

    r = requests.get(endpoint, params=payload, headers=headers)
    results = r.json()
    i = 0
    for i in range(len(results)):
        title = results[i]['title']
        print(title)


getRecipeByIngredients('burger')
