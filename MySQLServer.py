import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL Server (adjust username and password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''  # Update this to your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create the database (if it doesn't exist)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error: {err}")

    finally:
        # Close cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
