#!/usr/bin/python3

class User:
    """
    User class
    """

    def __init__(self):
        """
        Init method
        """
        self.__password = "test"

    def is_valid_password(self, password):
        """
        Check if password is valid
        """
        return password == self.__password


if __name__ == "__main__":
    u = User()
    print("Test User")
    print("is_valid_password should return True if it's the right password")

