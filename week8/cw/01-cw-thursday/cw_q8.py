"""
-class Book:

-attr: title - author - publication year - rating: list of floats 

-methods: getter - setter - validation:staticmethod - get_age:(datetime)calculate age from publication year
        add_rating: add new ratings to list - get_average_rating: calculate average of rates

------------------------------------------------------------------------------------------------------------
-class Library:

-attr: name:string - books:(list of Book objects) - borrowed_books: dictionary(name, return date) - 

-methods: getter - setter - validation - add_book: add new book to books list - ramove_book(input:title):
        remove a book from books list - borrow_book(title:str - borrower_name:str - return_date:str):
        update borrowed_books dictionary - return_book(title:str): mark a borrowed book to returned in the
        dictionary

class DataMixin

method : save_to_file , load_from_file

instance objecct subclass

"""

class DataMixin :

    def save_to_file(self, value):
        ''' save the objet data to file'''
        pass

    def load_from_file(self) :
        '''load and update the object data from a file'''
        pass


class Book(DataMixin):
    def __init__(self, title:str, author:str, publication_year:int):
        '''ratings: list of rates'''
        pass

    def get_age(self):
        '''calculate age from publication year'''
        pass

    @property
    def get_average_rating(self):
        '''calculate average of rates'''
        pass

    @get_average_rating.setter
    def add_rating(self, rate:float):
        '''add new ratings to list'''
        pass

    @staticmethod
    def date_validate(publication_date):
        '''check date format(yyyy)'''
        pass

    @staticmethod
    def rate_validate(rate):
        '''check rate format'''
        pass



class Library():
    def __init__(self, name):
        '''
        books: list of Books objects
        borrowed_books: a dictionary of dictionary
        '''
        pass

    @property
    def get_book(self):
        pass

    @get_book.setter
    def add_book(self, book:Book):
        '''add new book to books list'''
        pass
        
    @get_book.deleter
    def remove_book1(self ,title:str):
        '''delete a book from books list'''
        pass

    def remove_book2(self ,title:str):
        '''delete a book from books list'''
        pass

    def borrow_book(self, title:str, borrower_name:str, return_date:str):
        pass
        
    def return_book(self, title:str):
        '''remove returned book from dictionary'''
        pass

    @staticmethod
    def title_validate(title):
        '''check: is this book in library or not'''
        pass

    @staticmethod
    def available_validate(title):
        '''check this book is returned to library'''
        pass