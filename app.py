# use the datetime module to set the year published  attibute of the book class to the current year
from datetime import datetime
# interact with the operating system/create a directory and store the book data
import os
# use this module to store book colleciton data in a json file
import json
# sotre the book collection data in memory
from collections import defaultdict

class Book():
    def __init__(self, title, author, genre, year_published):
        self.title = title
        self.author = author
        self.genre = genre
        self.year_published = year_published 
        
    # string method to format the book info as an str
    def __str__(self):
        return f"{self.title} by {self.author}, {self.genre}, {self.year_published}"
    
    def create_book(cls):
        title = input("Enter the book title:  ")
        author = input("Enter the book author:  ")
        genre = input("Enter the book genre:  ")
        year_published = int(input("Enter the year the book was publsihed:  "))
        return cls(title, author, genre, year_published)
