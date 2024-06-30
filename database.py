import mysql.connector

# we use this to function to connect to the database and show and error if it can't without stopping
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='UserManagementSystem',
            user='alinb',
            password='RootRoot1'
        )
        print("Connected to the database.")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None
