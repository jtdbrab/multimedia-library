#!/usr/bin/env python

#packages & libraries
from rich import print
import sqlite3

from UserInterface import UserInterface
from helpers import *

def main():
    while True:
        userinterface = initialize_interface()
        userinterface.startscreen()



if __name__ == "__main__":
    main()