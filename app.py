# use the datetime module to set the year published  attibute of the book class to the current year
from datetime import datetime
# interact with the operating system/create a directory and store the book data
import os
# use this module to store book colleciton data in a json file
import json
# store the book collection data in memory
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
    
    # book method to create a new book object
    def create_book(cls):
        title = input("Enter the book title:  ")
        author = input("Enter the book author:  ")
        genre = input("Enter the book genre:  ")
        year_published = int(input("Enter the year the book was published:  "))
        return cls(title, author, genre, year_published)
    
    def display_book(self):
        print(self)
        
    # book data dictionary
    book_data = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "year_published": 1960},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "year_published": 1925},
    {"title": "1984", "author": "George Orwell", "genre": "Fiction", "year_published": 1949},
    {"title": "Animal Farm", "author": "George Orwell", "genre": "Fiction", "year_published": 1945},
    {"title": "Brave New World", "author": "Aldous Huxley", "genre": "Fiction", "year_published": 1932},
    {"title": "Lord of the Flies", "author": "William Golding", "genre": "Fiction", "year_published": 1954},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "genre": "Fiction", "year_published": 1813},
    {"title": "Sense and Sensibility", "author": "Jane Austen", "genre": "Fiction", "year_published": 1811},
    {"title": "Northanger Abbey", "author": "Jane Austen", "genre": "Fiction", "year_published": 1818},
    {"title": "Emma", "author": "Jane Austen", "genre": "Fiction", "year_published": 1815},
    {"title": "Persuasion", "author": "Jane Austen", "genre": "Fiction", "year_published": 1817},
    {"title": "Moby-Dick", "author": "Herman Melville", "genre": "Fiction", "year_published": 1851},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "genre": "Fiction", "year_published": 1951},
    {"title": "The Grapes of Wrath", "author": "John Steinbeck", "genre": "Fiction", "year_published": 1939},
    {"title": "Of Mice and Men", "author": "John Steinbeck", "genre": "Fiction", "year_published": 1937},
    {"title": "East of Eden", "author": "John Steinbeck", "genre": "Fiction", "year_published": 1952},
    {"title": "The Sun Also Rises", "author": "Ernest Hemingway", "genre": "Fiction", "year_published": 1926},
    {"title": "A Farewell to Arms", "author": "Ernest Hemingway", "genre": "Fiction", "year_published": 1929},
    {"title": "The Old Man and the Sea", "author": "Ernest Hemingway", "genre": "Fiction", "year_published": 1952},
    {"title": "Wuthering Heights", "author": "Emily Bronte", "genre": "Fiction", "year_published": 1847},
    {"title": "Jane Eyre", "author": "Charlotte Bronte", "genre": "Fiction", "year_published": 1847},
    ]

        
class Book_collection:
    def __init__(self, book_data):
       self.books = book_data
       
    def add_book(self, book):
        self.books.append(book)
        
    def remove_book(self, book):
        self.books.remove(book)
        
    def display_collection(self):
        for book in self.books:
            print(book)
    
    def dave_collection(self, data_file):
        with open(data_file, "w") as f:
            json.dump(self.books, f)
        
        

         
