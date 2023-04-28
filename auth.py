import re

class User:
    users = []

    def __init__(self, first_name, last_name, email, password, mobile_phone):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.mobile_phone = mobile_phone
        User.users.append(self)

    @staticmethod
    def validate_email(email):
        # Check if email format is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False

        # Check if email is unique
        for user in User.users:
            if user.email == email:
                return False

        return True

    @staticmethod
    def validate_password(password):
        # Check if password is at least 8 characters long and contains at least one uppercase letter, one lowercase letter, and one digit
        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$", password):
            return False

        return True

    @staticmethod
    def validate_mobile_phone(mobile_phone):
        # Check if mobile phone format is valid (11 digits and starts with 01)
        if not re.match(r"^01\d{9}$", mobile_phone):
            return False

        # Check if mobile phone is unique
        for user in User.users:
            if user.mobile_phone == mobile_phone:
                return False

        return True

    @classmethod
    def register(cls):
        while True:
            # Prompt user for registration details
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")

            if not User.validate_email(email):
                print("Email is not valid or already taken.")
                continue

            password = input("Enter password: ")

            if User.validate_password(password):
                print("Password is not valid.")
                continue

            confirm_password = input("Confirm password: ")

            if password != confirm_password:
                print("Passwords do not match.")
                continue

            mobile_phone = input("Enter mobile phone: ")

            if not User.validate_mobile_phone(mobile_phone):
                print("Mobile phone is not valid or already taken.")
                continue

            # Create new user
            user = User(first_name, last_name, email, password, mobile_phone)
            print("Registration successful.")
            break

    @classmethod
    def login(cls):
        while True:
            # Prompt user for login details
            email = input("Enter email: ")
            password = input("Enter password: ")

            # Check if email and password match any registered user
            for user in User.users:
                if user.email == email and user.password == password:
                    print("Login successful.")
                    return user

            print("Email or password is incorrect.")
