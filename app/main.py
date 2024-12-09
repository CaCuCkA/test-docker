from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

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

@app.route('/create_table', methods=['POST'])
def create_table():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Failed to connect to the database"}), 500
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
        return jsonify({"message": "Table 'users' created successfully"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/insert_data', methods=['POST'])
def insert_data():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Failed to connect to the database"}), 500
    cursor = connection.cursor()
    try:
        data_to_insert = request.json.get('users', [])
        if not data_to_insert:
            return jsonify({"error": "No data provided"}), 400
        insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
        cursor.executemany(insert_query, data_to_insert)
        connection.commit()
        return jsonify({"message": f"{cursor.rowcount} rows inserted"}), 201
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/get_users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    if not connection:
        return jsonify({"error": "Failed to connect to the database"}), 500
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return jsonify(rows), 200
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

