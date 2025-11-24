#!/usr/bin/env python

#packages & libraries
from rich import print
import sqlite3

from UserInterface import UserInterface
from helpers import *

def main():
    library = sqlite3.connect("library.db")
    cur = library.cursor()
    ui = initialize_interface()
    ui.run()
    

if __name__ == "__main__":
    main()