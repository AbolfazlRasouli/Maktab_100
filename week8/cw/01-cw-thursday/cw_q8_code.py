from datetime import datetime
# from t9 import DataMixin
from t10 import DataMixin

class Book(DataMixin):
    def __init__(self, title: str, author: str, publication_year):
        """ratings: list of rates"""
        self.title = title
        self.author = author
        self.publication_year = Book.date_validate(publication_year)
        self.rating = []

    def get_age(self):
        """(datetime)calculate age from publication year"""
        year_now = datetime.now().year
        return year_now - self.publication_year

    @property
    def get_average_rating(self):
        return sum(self.rating) / len(self.rating)

    @get_average_rating.setter
    def add_rating(self, rate):
        result = self.rate_validate(rate)
        self.rating.append(result)

    @staticmethod
    def date_validate(publication_date):
        """check date format(yyyy)"""
        year_now = datetime.now().year
        if not publication_date.isdigit():
            raise ValueError("your input is not number!!!")
        elif len(publication_date) != 4:
            raise ValueError("please enter 4 digits(YYYY)")
        elif int(publication_date) > year_now:
            raise ValueError("your date is larger than now!!!")
        else:
            return int(publication_date)

    @staticmethod
    def rate_validate(rate):
        """check rate format"""
        if not isinstance(rate, (float, int)):
            raise ValueError("your input is not number!!!")
        elif float(rate) < 0:
            raise ValueError("rate cant be negative!!!")
        elif float(rate) > 20:
            raise ValueError("your rate is larger than 20!!!")
        else:
            return float(rate)
        

class Library(DataMixin):
    borrowed_books = {}
    def __init__(self, name):
        """
        books: list of Books objects
        borrowed_books: a dictionary of dictionary
        """
        self.name = name
        self.books = []
        
    @property
    def get_book(self):
        return "\n".join(
            (item.title + " " + item.author + " " + str(item.publication_year))
            for item in self.books
        )
    
    @get_book.setter
    def add_book(self, book: Book):
        self.books.append(book)
        self.save_to_file(self.books)


    # @get_book.deleter
    # def remove_book_del(self, title: str):
    #     """delete a book from books list"""
    #     for i in self.books:
    #         if title in i.title:
    #             self.books.remove(i)
    #             return f"{i.title} deleted successfully!!!"
    #     else:
    #         return f"{i.title} is not exist!!!"
        

    def remove_book(self, title: str):
        """delete a book from books list"""
        boolean , result = self.title_validate(title)
        if boolean:
            self.books.remove(result)
            return f"{title} deleted successfully!!!"
        else:
            return f"{title} is not exist!!!"




    def borrow_book(self, title: str, borrower_name: str, return_date: str):
        boolean = self.available_validate(title)
        if boolean :
            Library.borrowed_books[title] = {"name" : borrower_name , "date" : return_date}
            return f"you borrowed {title}!!!"
        else:
            return f"{title} is not available!!!"
            



    def return_book(self, title: str):
        """remove returned book from dictionary"""
        if title in Library.borrowed_books.keys():
            Library.borrowed_books.pop(title)
            return f"{title} is returned!!!"
        else:
            return f"{title} is not exist!!!"



    def title_validate(self,title):
        """check: is this book in library or not"""
        for i in self.books:
            if title == i.title:
                return True, i
        else:
            return False, None
        

    def available_validate(self, title):
        """check this book is returned to library"""
        is_exist, get_title = self.title_validate(title)
        if is_exist :
            for i in Library.borrowed_books.keys():
                if title == i:
                    return False
            else:
                return True
            
book1 = Book("koory", "saramago", "2002")
book2 = Book("Emma", "Jane", "2004")
book3 = Book("mamad", "meysam", "1997")
print(book1.get_age())
book1.add_rating = 10
book1.add_rating = 20
book2.add_rating = 17.5
book3.add_rating = 20
print(book1.rating)
print(book1.get_average_rating)
print(book2.get_average_rating)
print(book3.get_average_rating)
library1 = Library("lib_mamad")
library1.add_book = book1
library1.add_book = book2
library1.add_book = book3
library1.load_from_file()
# print(library1.get_book)

# print(library1.remove_book("asghar"))
# print(library1.remove_book("mamad"))
# print(library1.get_book)

# print(library1.borrow_book("koory", "zeinab", "2023"))
# print(library1.borrow_book("koory", "zeinab", "2023"))
# print(library1.borrow_book("Emma", "zeinab", "2023"))

# print(library1.borrowed_books)

# print(library1.return_book("Emma"))
# print(library1.return_book("asghar"))

# print(library1.borrowed_books)