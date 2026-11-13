
import os

NOTES_DIR = "notes"

def add_note():
    subject = input("Enter subject name: ").strip().lower()
    content = input("Enter your note: ").strip()

    if not subject or not content:
        print("Subject and note cannot be empty.")
        return

    os.makedirs(NOTES_DIR, exist_ok=True)

    filename = os.path.join(NOTES_DIR, subject + ".txt")

    with open(filename, "a", encoding="utf-8") as file:
        file.write(content + "\n")

    print("Note saved successfully!")

def view_notes():
    subject = input("Enter subject name: ").strip().lower()
    filename = os.path.join(NOTES_DIR, subject + ".txt")

    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            print("\nYour Notes:")
            print(file.read())
    else:
        print("No notes found for this subject.")
