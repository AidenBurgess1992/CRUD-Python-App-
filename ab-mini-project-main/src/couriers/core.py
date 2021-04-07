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
[3] : Update courier
[4] : Remove courier
"""


def view_all(couriers):
    os.system("clear")
    idx = 0
    for courier in couriers:
        print(f"[{idx}] - {courier['name']} \t Tel: {courier['phone']}")
        idx += 1


def create_new(couriers):
    conn = connection()
    new_courier = input("What is the name of the new courier?: ")
    new_courier_phone = input("Enter the phone for this courier: ")
    update = "INSERT INTO courier (name, phone) VALUES (%s,%s)"
    a = (new_courier, new_courier_phone)
    execute_query(conn, update, a)
    return couriers


def update_courier(couriers):
    update_index = int(
        input('Enter the index of the couriers you want to change: '))
    update_phone = float(input("enter phone: "))
    new_courier_name = input('Enter a new name for this courier: ')
    selected_couriers = couriers[update_index]
    conn = connection()
    sql = "UPDATE courier SET name = %s, phone = %s WHERE id=%s"
    values = (new_courier_name, update_phone, selected_couriers["id"])
    push_to_db(conn, sql, values)
    return couriers


def remove_courier(couriers):
    conn = connection()
    del_id = int(
        input('Enter the id of the courier you would like to delete: '))
    delete_course = "DELETE FROM courier WHERE id=%s;"
    a = (del_id)
    execute_query(conn, delete_course, a)
    return couriers


def courier_menu(couriers=[]):
    while True:
        print(sub_menu)
        sub_option = int(input("Please choose an option: "))

        if sub_option == 0:
            break

        elif sub_option == 1:
            view_all(couriers)

        elif sub_option == 2:
            create_new(couriers)

        elif sub_option == 3:
            print('Choose the courier you want to update or press 0 to cancel')
            view_all(couriers)
            update_courier(couriers)

        elif sub_option == 4:
            print('Enter the courier you want to remove')
            view_all(couriers)
            remove_courier(couriers)
