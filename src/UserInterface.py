#packages & libraries
from rich import print

class UserInterface():
    def __init__(self, username):
        self.username = username
    
    def run(self):
        running = True
        while running:
            print(f"""
            Welcome to [bold]Paper & Grooves[/bold], {self.username}
            What would you like to do?
            1. Add book
            2. Remove book
            3. Search
            4. Quit
            """)
            user_choice = int(input("enter a number: "))
            if (user_choice == 1):
                print("this will be good")
                running = False




