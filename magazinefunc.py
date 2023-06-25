from model import Magazine

def printInfo(magazine):
        print(f"ISBN NO:{magazine.magNo}, Title:{magazine.title}, Format:{magazine.colorprint}, Subject:{magazine.subject}, Rental Price:{magazine.rental_price}, Available Copies:{magazine.copies}")


class magazineFunction:
    def __init__(self):
        self.listOfMags = []
        self.__initialData()

    def __initialData(self):
        mag1 = Magazine(magNo="01", title="History of Cricket", colorprint="color", subject="Sports", rental_price=5.00, copies=7)
        mag2 = Magazine(magNo="02", title="Evolution of the Computer", colorprint="black&white", subject="Technology", rental_price=3.00, copies=21)
        mag3 = Magazine(magNo="03", title="The Wonders of the Universe", colorprint="color", subject="Science", rental_price=6.50, copies=15)
        self.listOfMags.append(mag1)
        self.listOfMags.append(mag2)
        self.listOfMags.append(mag3)

    def add(self):
        __magNum = int(input("Enter Magazine Number: "))
        #Check if user's input is already in the system
        matchedData = list(Magazine for Magazine in self.listOfMags)
        for Magazine in matchedData:
            if Magazine.CD_no == __magNum:
                print(f"{__magNum} This Magazine Number is already in this system")
                return
            else:
                pass
        
        __title = input("Enter the title: ")
        
        colorprint = input("Enter Color Format (Color or Black & White): ").strip()
        
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

        magazine = Magazine(magNo=__magNum, title=__title, colorprint=colorprint, subject=__subject, rental_price=__rental_price, copies=__copies)
        self.listOfMags.append(magazine)
        print(f"Magazine added {magazine.magNo} - {magazine.title}")

    def remove(self):
        __magNum = input("Enter ISBN number: ").strip().upper()
        matchedData = list(magazine for magazine in self.listOfMags if magazine.magNo == __magNum)
        for magazine in self.listOfMags:
            if __magNum == magazine.magNo:
                confirmation = input(f"Remove the {magazine.magNo} - {magazine.title} Y/N: ").upper()
                if confirmation == "Y":
                    for x in matchedData:
                        self.listOfmMags.remove(x)
                        print("Item Removed.")
                        return
                else:
                    print("Operation Cancelled.")
                    return
            else:
                print(f"The ISBN Number {__magNum} not in this system")
                return

    def lend(self):
        __magNum = input("Enter ISBN number: ")
        __copies = int(input("Enter How Many Copies: "))
        matchedData = list(magazine for magazine in self.listOfMags if magazine.magNo == __magNum)
        for x in matchedData:
            x.copies -= __copies
            print("Item Lent.")

    def recieve(self):
        __magNum = input("Enter ISBN number: ")
        __copies = int(input("Enter received copies: "))
        matchedData = list(x for x in self.listOfMags if x.magNo == __magNum)
        for x in matchedData:
            x.copies += __copies
            print(f"Item Received with {__copies} Copies")

    def displayAll(self):
        for x in self.listOfMags:
            printInfo(magazine = x)

    def available(self):
        matchedData = list(x for x in self.listOfMags if x.copies > 0)
        for x in matchedData:
            printInfo(magazine = x)

    def unavailable(self):
        matchedData = list(x for x in self.listOfMags if x.copies == 0)
        for x in matchedData:
            printInfo(magazine = x)
