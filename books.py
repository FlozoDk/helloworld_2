class Book:
    """This is a class that represents books"""

    def __init__(self, title, author, year, language, price):
        self.title = title
        self.author = author
        self.year = year
        self.language = language
        self.price = price


    def apply_discount(self, percentage):
        self.price = self.price * 0.75