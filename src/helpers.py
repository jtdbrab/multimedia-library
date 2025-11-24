from UserInterface import UserInterface

def initialize_interface(db):
    print("Enter your name:", end=" ")
    username = input()
    return UserInterface(username, db)

