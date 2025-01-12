import mysql.connector
from mysql.connector import Error


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="mysql_db",
            user="root",
            password="password",
            database="test_db"
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def create_table():
    connection = get_db_connection()
    if not connection:
        return -1
    cursor = connection.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL
            )
        """)
        connection.commit()
        return -1
    except Error as e:
        return -1
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    create_table()
    print("Updated row +7")
