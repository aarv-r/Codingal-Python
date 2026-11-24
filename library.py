class book:
    def __init__(self, title, author, is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
    def borrow(self):
        self.is_borrowed = True
        print("You have borrowed the book:", self.title)
    def return_book(self):
        self.is_borrowed = False
        print("You have returned the book:", self.title)
book1 = book("The Hobbit", "J.R.R. Toliken")
book2 = book("1984", "George Orwell")
book3 = book("Past the shallows", "Favel Parret")
book1.borrow()
book2.borrow()
book3.borrow()
book1.return_book()
book2.return_book()
book3.return_book()