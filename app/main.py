import mysql.connector
from mysql.connector import Error

def create_and_insert_data():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host="mysql_db",
            user="root",
            password="password",
            database="test_db"
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            cursor = connection.cursor()

            # Create the table if it doesn't exist
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL
                )
            """)

            # Insert data using parameterized queries
            insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            data_to_insert = [
                ('Alice', 'alice@example.com'),
                ('Bob', 'bob@example.com')
            ]
            cursor.executemany(insert_query, data_to_insert)
            connection.commit()
            print("Data inserted into 'users' table")

            # Fetch and display data
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            print("Data from 'users' table:")
            for row in rows:
                print(row)

    except Error as e:
        print(f"Error: {e}")
    finally:
        # Ensure proper cleanup
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_and_insert_data()
