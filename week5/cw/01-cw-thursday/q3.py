class Book:
    __available = True
    def __init__(self, title, genre, auther):
        self.title = title
        self.genre = genre
        self.auther = auther
        

    def borrow(self):
        if Book.__available :
            Book.__available = False
            return f'{self.title} is available'
        else:
            return f'{self.title} is not available at the moment'

        
book1 = Book('A', 'romance', 'a')
book2 = Book('A', 'romance', 'a')
print(book1.borrow())
print(book1.borrow())
print(book2.borrow())



