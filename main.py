from bookfunction import BookFunction
from magazinefunc import magazineFunction
from educationaldvdsfunc import eduDVDFunction
from lecturecdsfunc import lectureCDFunction

def mainMenu():
    print("Main Menu")
    print("---------------")
    print("1 - Books")
    print("2 - Magazines")
    print("3 - External DVD")
    print("4 - Lecture CD")
    print("0 - Quit")

def subMenu(selectedChoice):
    selectedOperation = 1
    #check what choice is recieved from main menu
    if selectedChoice == 1:
        selectedResource = "Book"
        func = BookFunction()
    elif selectedChoice == 2:
        selectedResource = "Magazine"
        func = magazineFunction()
    elif selectedChoice == 3:
        selectedResource = "External DVD"
        func = eduDVDFunction()
    elif selectedChoice == 4:
        selectedResource = "Lecture CD"
        func = lectureCDFunction()
    else:
        print("Invalid Operation")

    while selectedOperation > 0:
        print("Please select the operation menu")
        print("---------------------------------")
        print(f"1 - Add a {selectedResource}")
        print(f"2 - Remove a {selectedResource} (WARNING!)")
        print(f"3 - Display Available {selectedResource}[s]")
        print(f"4 - Dispaly Unavailable {selectedResource}[s]")
        print(f"5 - Display All {selectedResource}[s]")
        print(f"6 - Lend {selectedResource}[s]")
        print(f"7 - Recieve {selectedResource}[s]")
        print(f"8 - Back To Main Menu")
        print("0 - Quit")
        while True:
            try:
                selectedOperation = int(input("Please type the number of your choice: ").strip())
                break
            except ValueError:
                print("Invalid Input. Please enter a valid number...")

        if selectedOperation == 1:
            func.add()
        elif selectedOperation == 2:
            func.remove()
        elif selectedOperation == 3:
            func.available()
        elif selectedOperation == 4:
            func.unavailable()
        elif selectedOperation == 5:
            func.displayAll()  
        elif selectedOperation == 6:
            func.lend()
        elif selectedOperation == 7:
            func.recieve()
        elif selectedOperation == 8:
            return
        elif selectedOperation == 0:
            print("Exiting program...")
            break
        else:
            print("Invaild Number")

        if 1 <= selectedOperation <= 7:
            input("press any key to continue...")


print(" _     __         ___ _  _  _  _ \ /    __\ / _____ __   ")
print("/ \| |(_ |     |   | |_)|_)|_||_) Y    (_  Y (_  | |_ |V|")
print("\_/|_|__)|__   |___|_|_)| \| || \ |    __) | __) | |__| |")
print("==============================")
while True:
    mainMenu()
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            # Access Books menu
            subMenu(selectedChoice = 1)
        elif choice == 2:
            # Access Magazines menu
            subMenu(selectedChoice = 2)
        elif choice == 3:
            # Access External DVD menu
            subMenu(selectedChoice = 3)
        elif choice == 4:
            # Access Lecture CD menu
            subMenu(selectedChoice = 4)
        elif choice == 0:
            # Quit the program
            print("Exiting program...")
        else:
            print("Invalid choice. Please enter a number between 0 and 4.")
    except ValueError:
        print("Invalid choice. Please enter a number between 0 and 4.")