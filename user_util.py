import random

class UserUtil:
    @staticmethod
    def generate_user_id():
        return random.randint(100000000, 999999999)