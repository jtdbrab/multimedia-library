#packages & libraries
from rich import print

class UserInterface():
    def __init__(self, username):
        self.username = username
    
    def startscreen(self):
        print(f"Welcome to [bold]Paper & Grooves[/bold], {self.username}")
        print("What would you like to do?")

