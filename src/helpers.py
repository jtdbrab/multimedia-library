from UserInterface import UserInterface

def initialize_interface():
    print("Enter your name:", end=" ")
    username = input()
    return UserInterface(username)

