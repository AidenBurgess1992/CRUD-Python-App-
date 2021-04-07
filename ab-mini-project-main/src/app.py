import os
import sys
from src.product.core import product_menu
from src.product.breakfast import breakfast_menu
from src.couriers.core import courier_menu
from src.couriers.delivery import delivery_menu
from src.orders.core import order_menu
from src.db.core import connection, query, pull_table
from src.persistence.core import read_data, write_data, read_csv_data, write_csv_data, save

conn = connection()

select_all_products = "SELECT * FROM product"
select_all_couriers = "SELECT * FROM courier"
select_all_orders = "SELECT * FROM transaction"
select_all_basket = "SELECT * FROM basket"


def load_state():
    state = {}
    state['products'] = pull_table(conn, select_all_products)
    state['couriers'] = pull_table(conn, select_all_couriers)
    state['orders'] = pull_table(conn, select_all_orders)
    return state


def save_state(state):
    save("./data/products.csv", state['products'])
    save("./data/couriers.csv", state['couriers'])
    save("./data/orders.csv", state['orders'])


main_menu = """
Please choose an option:
[0] : Exit
[1] : 24/7 Food Products
[2] : Couriers
[3] : Customer Orders Menu
[4] : Courier Preferences / Diet Requirments 
[5] : Breakfast Menu
"""


def menu(state):
    while True:
        os.system("clear")
        print(main_menu)
        option = int(input("Please choose an option: "))

        if option == 0:
            break

        if option == 1:
            product_menu(state['products'])

        if option == 2:
            courier_menu(state['couriers'])

        if option == 3:
            order_menu(state['orders'])

        # if option == 4:
            # delivery_menu(delivery)

        # if option == 5:
            # breakfast_menu(breakfast)


state = load_state()
menu(state)
# save(state)
