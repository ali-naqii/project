FILE_NAME = "notes.txt"


def add_note():
    """Appends a new note to the text file."""
    note = input("Enter your note: ")
    with open(FILE_NAME, "a") as f:
        f.write(note + "\n")
    print("Note saved!\n")


def view_notes():
    """Reads and displays all notes from the text file."""
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.readlines()
        if not lines:
            print("No notes found.\n")
        else:
            print("--- Your Notes ---")
            for i, line in enumerate(lines, 1):
                print(f"{i}. {line}", end="")
            print("\n------------------\n")
    except FileNotFoundError:
        print("No notes found.\n")


def main():
    """Main menu loop."""
    while True:
        print("===== NOTES MANAGER =====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        print("=========================")

        choice = input("Enter choice (1-3): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()

