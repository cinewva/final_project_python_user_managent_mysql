The application will target the management of a user base that has data  main: id, name, surname, email, age. 
Added methods: displaying a user by id, displaying all users,  entering a user, deleting a user, name change, email change.

It communicates with a Mysql database to store user data using mysql-connector-python.

Install it by running comand in console: pip install mysql-connector-python

Install Mysql application and run these commands in Mysql Workbench to setup the database:

    -- Connect to MySQL
    mysql -u your_uername -p

    -- enter password
    Your password

    -- create database
    CREATE DATABASE UserManagementSystem;

    -- utilize database
    USE UserManagementSystem;

    -- create table
    CREATE TABLE users (
        id INT PRIMARY KEY,
        first_name VARCHAR(50),
        last_name VARCHAR(50),
        email VARCHAR(50),
        age INT
    );

    -- verify table
    DESCRIBE users;

The unit tests are created from pytest library for every method.

Install it by running comand in console: pip install pytest

You cand run the Unit-tests in Pycharm console by pasting this command:

pytest test_user_management_system.py

I used Pycharm Community IDE.

These are the files in the project:

database.py : it contains the database connection function, exception and credentials

for_testing.py : It contains the unit-tests for every function in the application

user.py : The blueprint that represents the user with all properties

user_management_system.py : The class that has the definitions of most functions such as Add users, update name, delete users, read if users present

user_management_application.py : The main script of the application that interacts with the other files, runs the main loop of the application
and displays the menu of options in the console

How to use: Install Pycharm Community or some other IDE, clone the repository and run the user_management_application.py script, 
by right clicking on the page and click on Run user_management_application.py

Here's the entire run of the program by using every command once:

Connected to the database.

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 1
Enter user ID: 22
User{id=22, first_name=Test321, last_name=user123, email=test@user, age=23}

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 3
Enter user ID: 21
Enter first name: test2
Enter last name: user2
Enter email: test@user.com
Enter age: 33
User added successfully.

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 2
All users:
User{id=21, first_name=test2, last_name=user2, email=test@user.com, age=33}
User{id=22, first_name=Test321, last_name=user123, email=test@user, age=23}

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 4
Enter user ID: 22
User removed successfully.

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 2
All users:
User{id=21, first_name=test2, last_name=user2, email=test@user.com, age=33}

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 5
Enter user ID: 21
Enter new first name: test_updated
First name updated successfully.

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 6
Enter user ID: 21
Enter new email: test_updated@user.com
Email updated successfully.

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 2
All users:
User{id=21, first_name=test_updated, last_name=user2, email=test_updated@user.com, age=33}

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 7
User added successfully.
User added successfully.
User added successfully.
User added successfully.
User added successfully.

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 2
All users:
User{id=1, first_name=test1, last_name=user1, email=user1@test.com, age=1}
User{id=2, first_name=test2, last_name=user2, email=user2@test.com, age=2}
User{id=3, first_name=test3, last_name=user3, email=user3@test.com, age=3}
User{id=4, first_name=test4, last_name=user4, email=user4@test.com, age=4}
User{id=5, first_name=test5, last_name=user5, email=user5@test.com, age=5}
User{id=21, first_name=test_updated, last_name=user2, email=test_updated@user.com, age=33}

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 8
All users deleted successfully.

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 2
No users found.

User Management System
1. Display user by ID
2. Display all users
3. Add user
4. Remove user
5. Update first name
6. Update email
7. Add many users for testing
8. Remove all users
9. Exit
Enter your choice: 9
Exiting application...

Process finished with exit code 0
