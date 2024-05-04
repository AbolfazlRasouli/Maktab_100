from user import *
from exception import *
import hashlib


class Authenticator:
    def __init__(self): 
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists("This username already exists.")
        if len(password) < 8:
            raise PasswordTooShort("Password should be at least 8 characters long.")
        
        self.users[username] = User(username, password)
        # self.users[username] = {"username": username, "password": password}



    def login(self, username, password):
        if username in self.users:
            user = self.users[username]
            if user.password == hashlib.sha256(password.encode()).hexdigest():
                user.is_logged_in = True
                return True
            else:
                raise InvalidPassword("Invalid password.")
        raise InvalidUsername("Invalid username.")

    def is_logged_in(self, username):
        if username in self.users:
            use = self.users[username]
            if use.is_logged_in == True :
                return f'The user is logged in {username}'
            else :
                return f'The user has not logged in {username}'
        return f'There is no such user : {username}'




authenticator = Authenticator()
authenticator.add_user("abolfazl", "password1")
authenticator.add_user("meysam", "password2")
authenticator.add_user("parsa", "password3")
authenticator.add_user("moein", "password4")
authenticator.add_user("ali", "password5")
authenticator.add_user("amir", "password6")
authenticator.add_user("reza", "password7")

print(authenticator.users)

# authenticator.add_user("reza", "aaaaa")



print(authenticator.login("abolfazl", "password1"))  # True
# print(authenticator.login("parsa", "password111111"))  # false raise





print(authenticator.is_logged_in("abolfazl"))  # True
print(authenticator.is_logged_in("reza"))  # False

