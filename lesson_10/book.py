class Book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow_book(self):
        self.is_borrowed = True
        print(self.is_borrowed)

    def return_book(self):
        self.is_borrowed = False
        print(self.is_borrowed)

    def get_status(self):
        return self.is_borrowed
