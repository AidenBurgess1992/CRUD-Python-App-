import os
import sys
from src.persistence.core import save
from src.db.core import connection, query, push_to_db, execute_query
import pymysql.cursors

sub_menu = """
Please Choose an option:
[0] : Exit
[1] : View All
[2] : Create New
[3] : Update product
[4] : Remove product
"""

conn = connection()
select_all_products = "SELECT * FROM product"


def view_all(products):
    os.system("clear")
    idx = 0
    for product in products:
        print(f"[{idx}] - {product['name']} \t Price: {product['price']}")
        idx += 1


def add_product(products):
    conn = connection()
    new_product = input("What is the name of the new product?: ")
    new_product_price = input("Enter the price of this product: ")
    update = "INSERT INTO product (name, price) VALUES (%s,%s)"
    a = (new_product, new_product_price)
    execute_query(conn, update, a)
    return products


def update_product(products):
    update_index = int(
        input('Enter the index of the product you want to change: '))
    update_price = input('Enter price: ')
    new_product_name = input('Enter a new name for this product: ')
    selected_products = products[update_index]
    conn = connection()
    sql = "UPDATE product SET name = %s, price = %s WHERE id=%s"
    values = (new_product_name, update_price, selected_products["id"])
    push_to_db(conn, sql, values)
    return products


def del_product(products):
    conn = connection()
    del_id = int(
        input('Enter the id of the product you would like to delete: '))
    delete_course = "DELETE FROM product WHERE id=%s;"
    a = (del_id)
    execute_query(conn, delete_course, a)
    return products


def product_menu(products=[]):
    while True:
        print(sub_menu)
        sub_option = int(input("Please choose an option: "))

        if sub_option == 0:
            break

        elif sub_option == 1:
            view_all(products)

        elif sub_option == 2:
            add_product(products)

        elif sub_option == 3:
            print('Choose the product you want to update or press 0 to cancel')
            view_all(products)
            update_product(products)

        elif sub_option == 4:
            print('Enter the product you want to remove')
            del_product(products)
            input("Press Enter to head back to the product menu...")
            product_menu(products)
