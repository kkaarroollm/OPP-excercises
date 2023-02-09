import re
class Book:
    def __init__(self, title, author, isbn):
        self.author = author
        self.title = title
        self.isbn = isbn
        if Book.check_isbn(isbn) == False:
            raise ValueError('Wrong ISBN data.')


    @staticmethod
    def check_isbn(isbn: str):
        if len(isbn) == 10 and isbn.isdigit():
            return True
        elif len(isbn) == 13:
            if re.match(r'^[0-9]-[0-9]{3}-[0-9]{5}-[0-9]', isbn):
                return True
            else:
                return False

## that should work but idk how isbn works