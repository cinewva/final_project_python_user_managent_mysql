from abc import ABC, abstractmethod

# I created this blueprint because I knew I would need to add many users and delete all when testing the functionality
class ForTesting(ABC):
    @abstractmethod
    def add_users(self, id, first_name, last_name, email, age):
        pass

    @abstractmethod
    def delete_all_users(self):
        pass
