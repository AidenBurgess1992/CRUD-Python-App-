import os
import pymysql.cursors
from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("MYSQL_HOST")
USER = os.environ.get("MYSQL_USER")
PASSWORD = os.environ.get("MYSQL_PASSWORD")
DB = os.environ.get("MYSQL_DB")
PORT = int(os.environ.get("MYSQL_PORT"))


def connection():
    return pymysql.connect(host=HOST, user=USER, password=PASSWORD, database=DB)


def pull_table(conn, sql):
    with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


def query(conn, sql):
    with conn.cursor() as cursor:
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


def push_to_db(conn, sql, values):
    with conn.cursor() as cursor:
        cursor.execute(sql, values)
        conn.commit()


def execute_query(conn, query, value):
    cursor = conn.cursor()
    try:
        cursor.execute(query, value)
        conn.commit()
        print("Update successful")
    except Exception as e:
        input(f"ERROR: {e}")
