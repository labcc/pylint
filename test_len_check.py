"""Test script for the use-implicit-booleaness-not-len check."""

fruits = ["orange", "apple"]
vegetables = []

# These should be flagged
if len(fruits):
    print(fruits)

if not len(vegetables):
    print(vegetables)

if len(fruits) > 0:
    print(fruits)

if len(vegetables) == 0:
    print(vegetables)

# These should be the recommended way
if fruits:
    print(fruits)

if not vegetables:
    print(vegetables)
