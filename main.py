
from notes import add_note, view_notes, search_notes

while True:
    print("\n==============================")
    print("       CAMPUS NOTES")
    print("==============================")
    print("1. View Notes")
    print("2. Add Notes")
    print("3. Search Notes")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_notes()
    elif choice == "2":
        add_note()
    elif choice == "3":
        search_notes()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")
