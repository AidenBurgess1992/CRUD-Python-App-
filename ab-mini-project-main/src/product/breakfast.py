import os
from src.persistence.core import save


def breakfast_menu(breakfast=[]):
    print("1. Eggs")
    print("2. Pancakes")
    print("3. Waffles")
    print("4. Oatmeal")
    MainChoice = int(input("Choose a breakfast item to order: "))
    if (MainChoice == 2):
        Meal = "pancakes"
    elif (MainChoice == 3):
        meal = "waffles"

    if (MainChoice == 1):
        print("1. Wheat Toast")
        print("2. Sour Dough")
        print("3. Rye Toast")
        print("4. Pancakes")
        Bread = int(input("Choose a type of bread: "))
        if (Bread == 1):
            print("you chose eggs with wheat toast.")
        elif (Bread == 2):
            print("You chose eggs with sour dough.")
        elif (Bread == 3):
            print("You chose eggs with rye toast.")
        elif (Bread == 4):
            print("You chose eggs with pancakes.")
        else:
            print("We have eggs, but not that kind of bread.")
    elif (MainChoice == 2) or (MainChoice == 3):
        print("1. Syrup")
        print("2. Starwberries")
        print("3. Powdered Sugar")
        Topping = int(input("Choose a topping: "))

        if (Topping == 1):
            print("You chose " + meal + " with syrup.")
        elif (Topping == 2):
            print("You chose " + meal + " with strawberries.")
        elif (Topping == 3):
            print("You chose " + meal + " with powdered sugar.")
        else:
            print("We have " + Meal + ", but not that topping.")
    elif (MainChoice == 4):
        print("You chose oatmeal. ")
    else:
        print("We don't serve that breakfast item! ")
