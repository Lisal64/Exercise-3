# Exercise 1
text = str


def count_vowels(text):
    text = str(input("Please enter the word you want counted: "))
    text = text.lower()  # I decided to convert all letters into lower case ones to be able to accept both upper & lower case in the input
    count = 0
    vowels = ["a", "e", "i", "o", "u"]
    for j in text:  # looping through the given text for every letter
        for i in vowels:  # looping through every index in my list
            if j == i:  # checking if any of the positions are the same
                count += 1  # having the counter tick up, if there are same ones
    if count != 0:  # if the count did go up return the count
        return count
    else:
        return 42


print(count_vowels(text))

# Exercise 2
text1 = str
text2 = str


def hamming(text1, text2):
    text1 = str(input("Please enter your first word: "))
    text2 = str(input("Please enter your second word: "))
    hamming_distance = 0  # defining the variable to count with
    len(text1)  # getting the length of the strings
    len(text2)
    if len(text1) == len(text2):  # only goes through the loop if the length is equal
        for i in range(len(text1)):  # range to assign positions to the letter
            if text1[i] != text2[i]:  # needed the [i] to make sure they check at the same position of the word
                hamming_distance += 1
        return hamming_distance
    else:
        return 0


print(hamming(text1, text2))


# Exercise 3


class Vehicle():

    def __init__(self, color, fuel_type):  # defining constructor
        self.color = color
        self.fuel_type = fuel_type


class Car(Vehicle):

    def __init__(self, color, fuel_type, doors):
        super().__init__(color, fuel_type)  # letting my parent class handle these values
        self.doors = doors  # defining values, that the class should handle itself

    def __str__(self):  # overriding the method to get desired output
        return f"Color: {self.color}, Fuel type: {self.fuel_type}, Doors: {self.doors}"


class Bus(Vehicle):

    def __init__(self, color, fuel_type, passengers):
        super().__init__(color, fuel_type)
        self.passengers = passengers

    def __str__(self):
        return f"Color: {self.color}, Fuel type: {self.fuel_type}, Passengers: {self.passengers}"


my_car = Car("blue", "petrol", 4)  # test objects

print(my_car)

my_bus = Bus("red", "diesel", 35)

print(my_bus)


# Exercise 4

class Book():

    def __init__(self, name, author):  # creating the constructor
        self.name = name
        self.author = author

    def __str__(self):  # overriding to the wanted format
        return f"{self.name}, {self.author}"


aut_book = Book("Das flüssige Land", "Raphaela Edelbauer")  # text object

print(aut_book)


# Exercise 5:

class Book2():
    all_books = []  # "library"

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def add_book(self, name: object, author: object) -> object:
        book = Book2(name, author)  # ads book to the "library" and makes a list of all books
        self.all_books.append(book)
        return self.all_books

    def print_all_books(self, lst):  # method to customize output and print the books in the list
        self.lst = lst  # accepting as input which list the user wants to print
        for i in range(len(self.all_books)):  # creating a loop to look at all indexes of my list
            print(f"{self.all_books[i].name}, {self.all_books[i].author}")  # giving the format it should be printed in


library = Book2.add_book(Book2, "Das flüssige Land",
                         "Raphaela Edelbauer")  # adding different books to be able to check the functionality of my code
library = Book2.add_book(Book2, "Grundwissen Grammatik", "Duden")
library = Book2.add_book(Book2, "Großwörterbuch Englisch", "Langenscheidt")
library = Book2.add_book(Book2, "Österreichisches Wörterbuch", "öbv")
library = Book2.add_book(Book2, "Das Oxford Schulwörterbuch", "Oxford")
library = Book2.add_book(Book2, "Wörterbuch Deutsch", "Duden")

print(f"This is a list of books in your library:")
print(Book2.print_all_books(Book2, Book2.all_books))


# print(Book2.print_lst(Book2))

class BookShelf():
    bookshelf_lst = []  # creating class variables the whole class can use
    author_lst = []

    def __init__(self, books):
        self.books = books

    def add_book_list(self, books):
        for i in books:  # for every element in the given list
            for j in Book2.all_books:  # and for every element in my all_books-list
                if i.name == j.name and i.author == j.author:  # if both name and author are the same in both lists
                    self.bookshelf_lst.append(
                        i.name)  # add it to the list in my bookshelf - makes sure only book objects can be entered
        print(self.bookshelf_lst)
        return self.bookshelf_lst

    def books_by_author(self, author):
        self.author = author
        author_lst = []  # creating an empty list to store the book names in
        for a in Book2.all_books:  # checking every element in the list all_books
            if a.author == self.author:  # if the given author and the author in the list are the same
                self.author_lst.append(a.name)  # add the name to the list
        print(self.author_lst)  # printing the list out, so that the user can see the list
        return self.author_lst

    def get_books(self):
        my_books = []  # creating a list to only store the names in
        for n in self.bookshelf_lst:  # saved as str, so appending the str at the given index
            my_books.append(n)
        print(my_books)
        return my_books

    def clear_shelf(self):
        self.bookshelf_lst = []  # setting the list to an empty list to clear it

    def __str__(self):  # overriding to get the output in the desired format
        return f"{self.name}, {self.author}"


print("This is your search list: ")
search_lst = [Book2("Das flüssige Land", "Raphaela Edelbauer"), Book2("Grundwissen Grammatik", "Duden"),
              Book2("Wörterbuch Deutsch", "Duden")]

BookShelf.add_book_list(BookShelf,
                        search_lst)

# print(BookShelf.bookshelf_lst)

print("These are all the books in your list: ")
BookShelf.get_books(BookShelf)

print("These books were written by the given author: ")
BookShelf.books_by_author(BookShelf, "Duden")

print("These books are in your list: ")
print(BookShelf.bookshelf_lst)

print("We're clearing the list")
BookShelf.clear_shelf(BookShelf)

print(f"These books are currently in your list after clearing it: {BookShelf.bookshelf_lst}")
