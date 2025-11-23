#packages & libraries
from rich import print

class UserInterface():
    def __init__(self, username):
        self.username = username
    
    def startscreen(self):
        print(f"""
        Welcome to [bold]Paper & Grooves[/bold], {self.username}
        What would you like to do?
        1. Add book
        2. Remove book
        3. Search
        4. Quit
        """)

