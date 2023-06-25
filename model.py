class Book:
    def __init__(self, isbn_no, title, book_format, subject, rental_price, copies):
        self.isbn_no = isbn_no
        self.title = title
        self.book_format = book_format
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies

class Magazine:
    def __init__(self, magNo, title, colorprint, subject, rental_price, copies):
        self.magNo = magNo
        self.title = title
        self.colorprint = colorprint
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies

class EducationalDVD:
    def __init__(self, DVD_no, title, subject, rental_price, copies):
        self.DVD_no = DVD_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies

class LectureCD:
    def __init__(self, CD_no, title, subject, rental_price, copies):
        self.CD_no = CD_no
        self.title = title
        self.subject = subject
        self.rental_price = rental_price
        self.copies = copies

