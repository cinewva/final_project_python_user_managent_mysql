# blueprint for a user object with method for dipsplaying it as a string
class User:
    def __init__(self, id, first_name, last_name, email, age):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def __str__(self):
        return f'User{{id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, age={self.age}}}'
