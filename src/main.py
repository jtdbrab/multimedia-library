#!/usr/bin/env python

#packages & libraries
from rich import print

from UserInterface import UserInterface

def main():
    print("Enter your name:")
    username = input()
    userinterface = UserInterface(username)
    userinterface.startscreen()



if __name__ == "__main__":
    main()