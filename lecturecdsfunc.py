from model import LectureCD

def printInfo(lectureCD):
        print(f"ISBN NO:{lectureCD.CD_no}, Title:{lectureCD.title}, Subject:{lectureCD.subject}, Rental Price:{lectureCD.rental_price}, Available Copies:{lectureCD.copies}")


class lectureCDFunction:
    def __init__(self):
        self.listOflectureCDs = []
        self.__initialData()

    def __initialData(self):
        lectureCD1 = LectureCD(CD_no="21", title="Basics of Western Music", subject="Music", rental_price=1.50, copies=11)
        lectureCD2 = LectureCD(CD_no="22", title="Japanese Language", subject="Foreign Languages", rental_price=2.00, copies=3)
        lectureCD3 = LectureCD(CD_no="ISBN0003", title="Title3", subject="Science", rental_price=32.50, copies=3)
        self.listOflectureCDs.append(lectureCD1)
        self.listOflectureCDs.append(lectureCD2)
        self.listOflectureCDs.append(lectureCD3)

    def add(self):
        __CDNum = input("Enter Lecture CD Number NUmber: ").strip().upper()
        #Check if user's input is already in the system
        matchedData = list(lectureCD for lectureCD in self.listOflectureCDs)
        for lectureCD in matchedData:
            if lectureCD.CD_no == __CDNum:
                print(f"{__CDNum} This Lecture CD number is already in this system")
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

        lectureCD = lectureCD(CD_no=__CDNum, title=__title, subject=__subject, rental_price=__rental_price, copies=__copies)
        self.listOflectureCDs.append(lectureCD)
        print(f"lectureCD added {lectureCD.CD_no} - {lectureCD.title}")

    def remove(self):
        __CDNum = input("Enter Lecture CD number: ").strip().upper()
        matchedData = list(lectureCD for lectureCD in self.listOflectureCDs if lectureCD.CD_no == __CDNum)
        for lectureCD in self.listOflectureCDs:
            if __CDNum == lectureCD.CD_no:
                confirmation = input(f"Remove the {lectureCD.CD_no} - {lectureCD.title} [Y/N]: ").upper()
                if confirmation == "Y":
                    for x in matchedData:
                        self.listOflectureCDs.remove(x)
                        print("Item Removed.")
                        return
                else:
                    print("Operation Cancelled.")
                    return
            else:
                print(f"The Lecture CD Number {__CDNum} not in this system")
                return

    def lend(self):
        __CDNum = input("Enter Lecture CD Number: ")
        __copies = int(input("Enter How Many Copies: "))
        __borrowerId = int(input("Enter Borrower ID number")) 
        matchedData = list(lectureCD for lectureCD in self.listOflectureCDs if lectureCD.CD_no == __CDNum)
        for x in matchedData:
            x.copies -= __copies
            print("Item Lent.")

    def recieve(self):
        __CDNum = input("Enter Lecture CD Number: ")
        __copies = int(input("Enter received copies: "))
        matchedData = list(x for x in self.listOflectureCDs if x.CD_no == __CDNum)
        for x in matchedData:
            x.copies += __copies
            print(f"Item Received with {__copies} Copies")

    def displayAll(self):
        for x in self.listOflectureCDs:
            printInfo(lectureCD = x)

    def available(self):
        matchedData = list(x for x in self.listOflectureCDs if x.copies > 0)
        for x in matchedData:
            printInfo(lectureCD = x)

    def unavailable(self):
        matchedData = list(x for x in self.listOflectureCDs if x.copies == 0)
        for x in matchedData:
            printInfo(lectureCD = x)
