from user import User
from user_service import UserService
from user_util import UserUtil

if __name__ == "__main__":
    user1 = User(UserUtil.generate_user_id(), "Madina", "Nurlanova", "2000-05-15")
    UserService.add_user(user1)
    print(user1.get_details())
    print("Age:", user1.get_age())
    print("Users count:", UserService.get_number())

