class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._pages = []

    def __str__(self):
        return f'Book : {self.title} by {self.author}'

    @property
    def my_pages(self):
        return self._pages

    @my_pages.setter
    def my_pages(self, pages: list):
        self._pages = pages

    def __len__(self):
        return len(self._pages)

    def __getitem__(self, item):
        return self._pages[item]
 
    def __setitem__(self, key, value):
        self._pages[key] = value

    def __delitem__(self, key):
        self._pages.pop(key)

    def __contains__(self, item):
        if item in self._pages:
            return True
        else:
            return False


book1 = Book("harrypoter", "jonatan")
book1.my_pages = ["onvan", "moghadame", "dastan"]       #my_page @seter
print(book1.my_pages)       #my_page @property
print(book1)         #__str__
print(len(book1))       #__len__
print(book1[2])         #__getitem__
book1[2] = "romance"        #__setitem__
print(book1[2])     #__getitem__
del book1[1]        #__delitem__
print(book1.my_pages)      #my_page @property
print("deram" in book1)         #__contains__
print("onvan" in book1)         #__contains__
