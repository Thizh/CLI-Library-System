from model import Book

def printInfo(book):
        print(f"ISBN NO:{book.isbn_no}, Title:{book.title}, Format:{book.book_format}, Subject:{book.subject}, Rental Price:{book.rental_price}, Available Copies:{book.copies}")


class BookFunction:
    def __init__(self):
        self.listOfBooks = []
        self.__initialData()

    def __initialData(self):
        book1 = Book(isbn_no="ISBN1234", title="The Solar System", book_format="Hardcover", subject="Science", rental_price=15.00, copies=5)
        book2 = Book(isbn_no="ISBN9876", title="Types of Animal Species", book_format="Paperback", subject="Science", rental_price=10.00, copies=8)
        book3 = Book(isbn_no="ISBN1290", title="Second World War", book_format="Hardcover", subject="History", rental_price=12.50, copies=1)
        self.listOfBooks.append(book1)
        self.listOfBooks.append(book2)
        self.listOfBooks.append(book3)

    def add(self):
        __isbn = input("Enter ISBN NUmber: ").strip().upper()
        #Check if user's isbn is already in the system
        for book in self.listOfBooks:
            if __isbn == book.isbn_no:
                print(f"{__isbn} This isbn number is already in this system")
                return
            else:
                pass
        
        __title = input("Enter the title: ")
        
        __book_format = input("Enter Format (Hardcover or Paperback): ").strip()

        __subject = input("Subject: ")

        try:
            __rental_price = input("Rental Price: ")
        except ValueError:
            print("Invalid price entered, terminating...")
            return
        
        try:
            __copies = int(input("Copies: "))
        except ValueError:
            print("Invalid copies, Program terminating...")
            return

        book = Book(isbn_no=__isbn, title=__title, book_format=__book_format, subject=__subject, rental_price=__rental_price, copies=__copies)
        self.listOfBooks.append(book)
        print(f"Book added {book.isbn_no} - {book.title}")

    def remove(self):
        __isbn = input("Enter ISBN number: ").strip().upper()
        matchedData = list(book for book in self.listOfBooks if book.isbn_no == __isbn)
        for book in self.listOfBooks:
            if __isbn == book.isbn_no:
                confirmation = input(f"Remove the {book.isbn_no} - {book.title} [Y/N]: ").upper()
                if confirmation == "Y":
                    for x in matchedData:
                        self.listOfBooks.remove(x)
                        print("Item Removed.")
                        return
                else:
                    print("Operation Cancelled.")
                    return
            else:
                print(f"The ISBN Number {__isbn} not in this system")
                return

    def lend(self):
        __isbn = input("Enter ISBN number: ")
        __copies = int(input("Enter How Many Copies: "))
        matchedData = list(book for book in self.listOfBooks if book.isbn_no == __isbn)
        for x in matchedData:
            x.copies -= __copies
            print("Item Lent.")

    def recieve(self):
        __isbn = input("Enter ISBN number: ")
        __copies = int(input("Enter received copies: "))
        matchedData = list(x for x in self.listOfBooks if x.isbn_no == __isbn)
        for x in matchedData:
            x.copies += __copies
            print(f"Item Received with {__copies} Copies")

    def displayAll(self):
        for x in self.listOfBooks:
            printInfo(book = x)

    def available(self):
        matchedData = list(x for x in self.listOfBooks if x.copies > 0)
        for x in matchedData:
            printInfo(book = x)

    def unavailable(self):
        matchedData = list(x for x in self.listOfBooks if x.copies == 0)
        for x in matchedData:
            printInfo(book = x)
            