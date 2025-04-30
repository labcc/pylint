fruits = ["orange", "apple"]
vegetables = []

if len(fruits):  # [use-implicit-booleaness-not-len]
    print(fruits)

if not len(vegetables):  # [use-implicit-booleaness-not-len]
    print(vegetables)

if len(fruits) > 0:  # [use-implicit-booleaness-not-len]
    print(fruits)

if len(vegetables) == 0:  # [use-implicit-booleaness-not-len]
    print(vegetables)
