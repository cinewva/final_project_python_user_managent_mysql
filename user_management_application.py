from user_management_system import UserManagementSystem

def main():
    user_management_system = UserManagementSystem()

    # menu of things to select in the console in a loop until the user coses to exit
    while True:
        print("\nUser Management System")
        print("1. Display user by ID")
        print("2. Display all users")
        print("3. Add user")
        print("4. Remove user")
        print("5. Update first name")
        print("6. Update email")
        print("7. Add many users for testing")
        print("8. Remove all users")
        print("9. Exit")
        choice = input("Enter your choice: ")

        # using the methods from user_management_system.py depending on the menu selection
        if choice == '1':
            id = int(input("Enter user ID: "))
            user_management_system.display_user_by_id(id)
        elif choice == '2':
            user_management_system.display_all_users()
        elif choice == '3':
            id = int(input("Enter user ID: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            age = int(input("Enter age: "))
            user_management_system.add_user(id, first_name, last_name, email, age)
        elif choice == '4':
            id = int(input("Enter user ID: "))
            user_management_system.remove_user(id)
        elif choice == '5':
            id = int(input("Enter user ID: "))
            new_first_name = input("Enter new first name: ")
            user_management_system.update_first_name(id, new_first_name)
        elif choice == '6':
            id = int(input("Enter user ID: "))
            new_email = input("Enter new email: ")
            user_management_system.update_email(id, new_email)

        # created test users to add many at once
        elif choice == '7':
            user_management_system.add_users(1, "test1", "user1", "user1@test.com", 1)
            user_management_system.add_users(2, "test2", "user2", "user2@test.com", 2)
            user_management_system.add_users(3, "test3", "user3", "user3@test.com", 3)
            user_management_system.add_users(4, "test4", "user4", "user4@test.com", 4)
            user_management_system.add_users(5, "test5", "user5", "user5@test.com", 5)
        elif choice == '8':
            user_management_system.delete_all_users()
        elif choice == '9':
            print("Exiting application...")
            user_management_system.close_connection()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
