import mysql.connector
from user import User
from for_testing import ForTesting
from database import connect_to_database

class UserManagementSystem(ForTesting):
    # database initialization and connection
    def __init__(self):
        self.connection = connect_to_database()
    def close_connection(self):
        if self.connection:
            self.connection.close()

    # function to return a list of objects representing all users
    def display_all_users(self):
        users = []
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users")
            result = cursor.fetchall()

            if len(result) == 0:
                print("No users found.")
            else:
                print("All users:")
                for row in result:
                    user = User(*row)
                    users.append(user)
                    print(user)

            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        return users

    # funtion for adding a user manually to the database
    def add_user(self, id, first_name, last_name, email, age):
        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO users (id, first_name, last_name, email, age) VALUES (%s, %s, %s, %s, %s)",
                (id, first_name, last_name, email, age)
            )
            self.connection.commit()
            print("User added successfully.")
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")


    # function to delete a user from the database unig the ID
    def remove_user(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM users WHERE id=%s", (id,))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("User removed successfully.")
            else:
                print("User not found.")
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # function to change the first name of a user in the database using ID
    def update_first_name(self, id, new_first_name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE users SET first_name=%s WHERE id=%s", (new_first_name, id))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("First name updated successfully.")
            else:
                print("User not found.")
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # function to update the email of a user in the database using ID
    def update_email(self, id, new_email):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE users SET email=%s WHERE id=%s", (new_email, id))
            self.connection.commit()
            if cursor.rowcount > 0:
                print("Email updated successfully.")
            else:
                print("User not found.")
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    # funtion to display a user by ID
    def display_user_by_id(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM users WHERE id=%s", (id,))
            result = cursor.fetchone()
            if result:
                user = User(*result)
                print(user)
                return user
            else:
                print("User not found.")
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None

    # add many users for testing purposes
    def add_users(self, id, first_name, last_name, email, age):
        self.add_user(id, first_name, last_name, email, age)

    # delete all users for testing purposes
    def delete_all_users(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM users")
            self.connection.commit()
            print("All users deleted successfully.")
            cursor.close()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
