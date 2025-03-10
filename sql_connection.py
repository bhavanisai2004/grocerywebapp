from datetime import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
    print("Opening MySQL connection")
    global __cnx

    if __cnx is None:
        try:
            __cnx = mysql.connector.connect(
                user='root',
                password='bhavani@1',
                database='grocery_store',
                host='localhost',
                port=3306
            )
            print("✅ Database connection successful!")
        except mysql.connector.Error as err:
            print(f"❌ Error: {err}")
    
    return __cnx
