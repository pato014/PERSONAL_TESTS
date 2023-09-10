from datetime import datetime
# Task  - Create simple class with methods
class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        name = self.name
        return name.capitalize()

    def age(self, current_year):
        return current_year - self.birth_year


user = User(name="nika", birth_year=1999)

print(user.age(2023))
print(user.get_name())