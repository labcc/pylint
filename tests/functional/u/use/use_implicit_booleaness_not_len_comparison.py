# pylint: disable=too-few-public-methods,import-error, missing-docstring, use-yield-from
# pylint: disable=useless-super-delegation,wrong-import-position,invalid-name, wrong-import-order, condition-evals-to-constant

fruits = ["orange", "apple"]
vegetables = []

# Examples 1&2 (currently caught by rule C1802)
if len(fruits):  # [use-implicit-booleaness-not-len]
    print(fruits)

if not len(vegetables):  # [use-implicit-booleaness-not-len]
    print(vegetables)

# Examples 3&4 (not caught by PLC1802 yet)
if len(fruits) > 0:  # [use-implicit-booleaness-not-len]
    print(fruits)

if len(vegetables) == 0:  # [use-implicit-booleaness-not-len]
    print(vegetables)

# Examples 5&6 (recommended formulation)
if fruits:
    print(fruits)

if not vegetables:
    print(vegetables)
