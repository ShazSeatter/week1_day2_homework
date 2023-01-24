users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

print(users["Jonathan"]["twitter"])

# 2. Get Erik's hometown

print(users["Erik"]["home_town"])

# 3. Get the list of Erik's lottery numbers

print(users["Erik"].get("lottery_numbers"))

# -------------------------------------------------- 

# 4. Get the species of Avril's pet Monty

print(users["Avril"]["pets"][0]["species"])

# the dictionary is nested in a list, using indexes to access value at species 

# -------------------------------------------------- 
# 5. Get the smallest of Erik's lottery numbers

erik_lotto = users["Erik"].get("lottery_numbers")

print(min(erik_lotto))

# print(min(users["Erik"].get("lottery_numbers")))

# used min() method
# -------------------------------------------------- 

# 6. Return an list of Avril's lottery numbers that are even

# NEED TO RETURN BACK TO THIS !!!!!!! //// 

# even_num = users["Avril"].get("lottery_numbers")

# print(even_num)

# for num in even_num:
#   if num % 2 == 0:

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

erik_lotto.append(7)

print(erik_lotto)

# 8. Change Erik's hometown to Edinburgh

users["Erik"]["home_town"] = "Edinburgh"

print(users["Erik"]["home_town"])

# 9. Add a pet dog to Erik called "fluffy"

dog = { 
  "name" : "fluffy", 
  "species" : "dog",
}

users["Erik"]["pets"].append(dog)

print(users["Erik"]["pets"])

# 10. Add another person to the users dictionary

