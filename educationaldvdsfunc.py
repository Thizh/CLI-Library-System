from model import EducationalDVD

def printInfo(eduDVD):
        print(f"ISBN NO:{eduDVD.DVD_No}, Title:{eduDVD.title}, Subject:{eduDVD.subject}, Rental Price:{eduDVD.rental_price}, Available Copies:{eduDVD.copies}")


class eduDVDFunction:
    def __init__(self):
        self.listOfeduDVDs = []
        self.__initialData()

    def __initialData(self):
        eduDVD1 = EducationalDVD(DVD_No=10, title="Birth of the Solar System", subject="Astronomy", rental_price=2.50, copies=1)
        eduDVD2 = EducationalDVD(DVD_No=11, title="Pythagoras Theorem", subject="Math", rental_price=1.00, copies=50)
        eduDVD3 = EducationalDVD(DVD_No=12, title="Introduction to Programming", subject="Technology", rental_price=3.00, copies=20)
        self.listOfeduDVDs.append(eduDVD1)
        self.listOfeduDVDs.append(eduDVD2)
        self.listOfeduDVDs.append(eduDVD3)

    def add(self):
        __DVDNum = input("Enter Educational DVD Number: ").strip().upper()
        #Check if user's input is already in the system
        matchedData = list(EducationalDVD for EducationalDVD in self.listOfeduDVDs)
        for EducationalDVD in matchedData:
            if EducationalDVD.CD_no == __DVDNum:
                print(f"{__DVDNum} This Educational DVD number is already in this system")
                return
            else:
                pass
        
        __title = input("Enter the title: ")
        
        __subject = input("Subject: ")

        try:
            __rental_price = float(input("Rental Price: "))
        except ValueError:
            print("Invalid price entered, terminating...")
            return
        
        try:
            __copies = int(input("Copies: "))
        except ValueError:
            print("Invalid copies, Program terminating...")
            return

        eduDVD = eduDVD(DVD_No=__DVDNum, title=__title, subject=__subject, rental_price=__rental_price, copies=__copies)
        self.listOfeduDVDs.append(eduDVD)
        print(f"eduDVD added {eduDVD.DVD_No} - {eduDVD.title}")

    def remove(self):
        __DVDNum = input("Enter Educational DVD Number: ").strip().upper()
        matchedData = list(eduDVD for eduDVD in self.listOfeduDVDs if eduDVD.DVD_No == __DVDNum)
        for eduDVD in self.listOfeduDVDs:
            if __DVDNum == eduDVD.DVD_No:
                confirmation = input(f"Remove the {eduDVD.DVD_No} - {eduDVD.title} Y/N: ").upper()
                if confirmation == "Y":
                    for x in matchedData:
                        self.listOfeduDVDs.remove(x)
                        print("Item Removed.")
                        return
                else:
                    print("Operation Cancelled.")
                    return
            else:
                print(f"The Educational DVD Number {__DVDNum} not in this system")
                return

    def lend(self):
        __DVDNum = input("Enter Educational DVD Number: ")
        __copies = int(input("Enter How Many Copies: "))
        matchedData = list(eduDVD for eduDVD in self.listOfeduDVDs if eduDVD.DVD_No == __DVDNum)
        for x in matchedData:
            x.copies -= __copies
            print("Item Lent.")

    def recieve(self):
        __DVDNum = input("Enter Educational DVD Number: ")
        __copies = int(input("Enter received copies: "))
        matchedData = list(x for x in self.listOfeduDVDs if x.DVD_No == __DVDNum)
        for x in matchedData:
            x.copies += __copies
            print(f"Item Received with {__copies} Copies")

    def displayAll(self):
        for x in self.listOfeduDVDs:
            printInfo(eduDVD = x)

    def available(self):
        matchedData = list(x for x in self.listOfeduDVDs if x.copies > 0)
        for x in matchedData:
            printInfo(eduDVD = x)

    def unavailable(self):
        matchedData = list(x for x in self.listOfeduDVDs if x.copies == 0)
        for x in matchedData:
            printInfo(eduDVD = x)
