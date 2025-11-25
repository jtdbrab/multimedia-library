#packages & libraries
from rich import print

class UserInterface():
    def __init__(self, username, db):
        self.username = username
        self.db = db
    
    def run(self):
        running = True
        while running:
            print(f"""
            Welcome to [bold]Paper & Grooves[/bold], {self.username}
            What would you like to do?
            1. Check library
            2. Add item
            2. Remove item
            3. Search
            4. Quit
            """)
            user_choice = input("enter a number: ")
            if (user_choice == "1"):
                print("this will be good")           
            elif (user_choice == "2"):
                self.add_item()
            elif (user_choice == "3"):
                print("this will be good")
            elif (user_choice == "4"):
                running = False
            else:
                print("Not a valid choice")
    
    def add_item(self):
        toAdd = input("What would you like to add (book/record)? ")
        if toAdd.lower() == "book":
            print("A BOOK!")
            return
        if toAdd.lower() == "record":
            print("A RECORD!")
            return
        else:
            print("Not a valid choice!")
            return

    

        


 





