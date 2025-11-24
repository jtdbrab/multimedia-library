#!/usr/bin/env python

#packages & libraries
from rich import print
import sqlite3

from UserInterface import UserInterface
from helpers import *
from DatabaseManager import *

def main():
    db = DatabaseManager()
    ui = initialize_interface(db)
    ui.run()
    

if __name__ == "__main__":
    main()