import datetime

class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.birthday = birthday

    def get_details(self):
        return f"ID: {self.user_id}, Name: {self.name} {self.surname}"

    def get_age(self):
        birth_year = int(self.birthday.split('-')[0])
        return datetime.date.today().year - birth_year