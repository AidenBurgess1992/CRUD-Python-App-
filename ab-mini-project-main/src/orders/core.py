import os
import sys
from src.persistence.core import save
from src.db.core import connection, query, push_to_db, execute_query, pull_table
import pymysql.cursors
import itertools


sub_menu = """
Please Choose an option:
[0] : Exit
[1] : View All
[2] : Create New Order
[3] : Update Order Status
[4] : Remove Order 
"""

status = ["PREPARING", "READY", "OUT-FOR-DELIVERY", "DELIVERED"]

conn = connection()
select_all_orders = "SELECT * FROM transaction"


def view_all(state):
    os.system("clear")
    idx = 0
    for order in state:
        print(f"[{idx}] - {order['id']} {order['courier_id']} {order['customer_name']} {order['customer_address']} {order['customer_phone']} {order['order_status']}")
        idx += 1


def create_order(state):
    name = input("What is the name of the customer: ")
    phone = float(input("enter phone: "))
    address = input("What is the address of the customer: ")
    courier_id = input("Please select a courier from the list: ")
    order = "preparing"
    products = get_basket_product(state)
    connection = ()
    SQL_statement = ("INSERT INTO transaction (customer_name, customer_phone,customer_address,courier_id, order_status) "  # product_id
                     "VALUES ( %s, %s, %s,%s,%s)")
    val = (name, phone, address, courier_id, "preparing")
    push_to_db(conn, SQL_statement, val)
    result = pull_table(conn, "SELECT LAST_INSERT_ID();")
    print(result)
# For loop over the prducts , insert into the basket function in the SQL database, then creates a row in the basket table for each of the products, it's going to have the product id, then get product id back from prev inseration
    # [0][0] Reason the result that comes back, is a list, of tuples.
    new_tranaction_id = result[0]['LAST_INSERT_ID()']
    for p in products:
        # call create basket items in for a loop
        create_basket_item(new_tranaction_id, p)
    return state


def create_basket_item(transaction_id, product_id):
    SQL = "INSERT INTO basket (transaction_id, product_id) VALUES (%s, %s)"
    val = (transaction_id, product_id)
    push_to_db(conn, SQL, val)


def get_basket_product(state):
    print(state)
    selected_products = []
    print("Enter product ID: ")
    while True:
        product_id = int(input(""))
        if product_id == 0:
            break
        selected_products.append(product_id)
    return selected_products


def update_order(state):
    print('Choose the order you want to update or press 0 to cancel')
    order_id = input('Select the order you want to change: ')
    order_status = input('Enter a new status for this order: ')
    connection = ()
    SQL_statement = (
        "UPDATE transaction SET order_status = %s WHERE id = %s ")
    val = (order_status, order_id)
    push_to_db(conn, SQL_statement, val)


def remove_order(state):
    print('Enter the order you want to remove')
    order_id = input('Enter the index of the product: ')
    connection = ()
    SQL_statement = ("DELETE FROM basket WHERE transaction_id =%s; ")
    val = (order_id)
    push_to_db(conn, SQL_statement, val)
    SQL_statement = ("DELETE FROM transaction WHERE id=%s; ")
    push_to_db(conn, SQL_statement, val)


def order_menu(state):
    while True:
        print(sub_menu)
        sub_option = int(input("Please choose an option: "))

        if sub_option == 0:
            break

        elif sub_option == 1:
            view_all(state)

        elif sub_option == 2:
            view_all(state)
            create_order(state)

        elif sub_option == 3:
            view_all(state)
            update_order(state)

        elif sub_option == 4:
            view_all(state)
            remove_order(state)
