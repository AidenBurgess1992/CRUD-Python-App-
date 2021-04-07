import os
from src.persistence.core import save


def delivery_menu(delivery=[]):
    print("1. David")
    print("2. John")
    print("3. Muhammad")
    print("4. Abraham")
    MainChoice = int(input("Choose a courier for delivery: "))

    if (MainChoice == 1):
        print("1. A Car")
        print("2. Scooter")
        print("3. Bycycle")
        print("4. On foot")
        delivery = int(input(
            "Here at the genration Cafe, we have the planet in mind! Please choose a type of delivery method: "))
        if (delivery == 1):
            print("you chose David for delivery with a car.")
        elif (delivery == 2):
            print("You you chose David for delivery with a scooter. ")
        elif (delivery == 3):
            print("you chose David for delivery with by Bycycle.")
        elif (delivery == 4):
            print("You delivery by foot.")
        else:
            print("We have couriers, but not that kind of couriers, I'm afraid!")

    if (MainChoice == 2):
        print("1. A Car")
        print("2. Scooter")
        print("3. Bycycle")
        print("4. On foot")
        delivery = int(input(
            "Here at the genration Cafe, we have the planet in mind! Please choose a type of delivery method: "))
        if (delivery == 1):
            print("you chose john for delivery with a car.")
        elif (delivery == 2):
            print("You you chose John for delivery with a scooter. ")
        elif (delivery == 3):
            print("you chose John for delivery with by Bycycle.")
        elif (delivery == 4):
            print("You chose delivery by foot.")
        else:
            print("We have couriers, but not that kind of couriers, I'm afraid!")

    if (MainChoice == 3):
        print("1. Halal certifed delivery by Car")
        print("2. Halal certifed delivery by Scooter")
        print("3. Halal certifed delivery by Bycycle")
        print("4. Halal certifed delivery by On foot")
        delivery = int(input("While keeping the planet in mind, We're also aware our customers have diet requirments, we offer a range of Halal & Kosher products. Our friendly drivers Muhammad & Ahbraham will gladly assit you. "))
        if (delivery == 1):
            print("you chose Muhammad for Halal delivery with a car.")
        elif (delivery == 2):
            print("You you chose Muhammad for Halal delivery with a scooter. ")
        elif (delivery == 3):
            print("you chose Muhammad for Halal delivery with by Bycycle.")
        elif (delivery == 4):
            print("You chose Halal delivery by foot.")
        else:
            print("We have couriers, but not that kind of couriers, I'm afraid!")

    if (MainChoice == 4):
        print("1. Kosher certified delviery by Car")
        print("2. Kosher certified delviery by Scooter")
        print("3. Kosher certified delviery by Bycycle")
        print("4. Kosher certified delviery On foot")
        delivery = int(input("While keeping the planet in mind, We're also aware our customers have diet requirments, we offer a range of Halal & Kosher products. Our friendly drivers Muhammad & Ahbraham will gladly assit you. "))
        if (delivery == 1):
            print("you chose john for delivery with a car.")
        elif (delivery == 2):
            print("You you chose John for delivery with a scooter. ")
        elif (delivery == 3):
            print("you chose John for delivery with by Bycycle.")
        elif (delivery == 4):
            print("You chose delivery by foot.")
        else:
            print("We have couriers, but not that kind of couriers, I'm afraid!")
