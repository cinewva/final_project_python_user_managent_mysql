import pytest
from user_management_system import UserManagementSystem

# creating an instance of UserManagementSystem
@pytest.fixture
def user_management_system():
    ums = UserManagementSystem()
    yield ums
    ums.close_connection()

# here adding a user is unit tested, by adding it and asserting it was added correctly
def test_add_user(user_management_system):
    user_management_system.delete_all_users()
    user_management_system.add_user(1, "John", "Doe", "john.doe@example.com", 30)
    user = user_management_system.display_user_by_id(1)
    assert user is not None
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.email == "john.doe@example.com"
    assert user.age == 30

# here removing a user is unit tested, by adding one and removing it and verifying
def test_remove_user(user_management_system):
    user_management_system.delete_all_users()
    user_management_system.add_user(2, "Jane", "Doe", "jane.doe@example.com", 25)
    user_management_system.remove_user(2)
    user = user_management_system.display_user_by_id(2)
    assert user is None

# here I tested if uptading the first name is working by adding a user and then changing the name and asserting the new name
def test_update_first_name(user_management_system):
    user_management_system.delete_all_users()
    user_management_system.add_user(3, "Alice", "Smith", "alice.smith@example.com", 28)
    user_management_system.update_first_name(3, "Alicia")
    user = user_management_system.display_user_by_id(3)
    assert user is not None
    assert user.first_name == "Alicia"

# test if the email is updated succesfully
def test_update_email(user_management_system):
    user_management_system.delete_all_users()
    user_management_system.add_user(4, "Bob", "Brown", "bob.brown@example.com", 35)
    user_management_system.update_email(4, "bobby.brown@example.com")
    user = user_management_system.display_user_by_id(4)
    assert user is not None
    assert user.email == "bobby.brown@example.com"

# test if all users are displayes
def test_display_all_users(user_management_system):
    user_management_system.delete_all_users()
    user_management_system.add_user(5, "test5", "user5", "test5@example.com", 45)
    user_management_system.add_user(6, "test6", "user6", "test6@example.com", 50)
    users = user_management_system.display_all_users()
    assert len(users) == 2
    assert users[0].first_name == "test5"
    assert users[1].first_name == "test6"

# unit test for deleting all users function
def test_delete_all_users(user_management_system):
    user_management_system.add_user(7, "test7", "user7", "test7@example.com", 55)
    user_management_system.delete_all_users()
    users = user_management_system.display_all_users()
    assert users == []
