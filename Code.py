# Preloaded list of books
books = [
    {"Title": "Python Crash Course", "Author": "Eric Matthes", "ISBN": "9781593279288", "Available": "yes"},
    {"Title": "Automate the Boring Stuff with Python", "Author": "Al Sweigart", "ISBN": "9781593275990", "Available": "yes"},
    {"Title": "Clean Code", "Author": "Robert C. Martin", "ISBN": "9780132350884", "Available": "no"},
    {"Title": "The Pragmatic Programmer", "Author": "Andrew Hunt", "ISBN": "9780201616224", "Available": "yes"},
]

# Function to display the main menu
def display_menu():
    print("\nLibrary Management System")
    print("1. Add a Book")
    print("2. Search for a Book")
    print("3. Display All Books")
    print("4. Remove a Book")
    print("5. Exit")

# Function to get a valid user choice
def get_menu_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            print("Invalid choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

# Function to add a book
def add_book():
    print("\nAdding a New Book")
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    isbn = input("Enter ISBN (10 or 13 digits): ").strip()
    available = input("Is the book available? (yes/no): ").strip().lower()

    if not title or not author or not isbn.isdigit() or len(isbn) not in [10, 13] or available not in ["yes", "no"]:
        print("Invalid input! Please enter correct book details.")
        return

    books.append({"Title": title, "Author": author, "ISBN": isbn, "Available": available})
    print(f"\nBook '{title}' added successfully!")

# Function to search for a book
def search_book():
    print("\nSearch for a Book")
    search_term = input("Enter book title or author to search: ").strip().lower()
    
    if not search_term:
        print("Search term cannot be empty!")
        return

    found_books = [book for book in books if search_term in book["Title"].lower() or search_term in book["Author"].lower()]

    if found_books:
        print("\nMatching Books:")
        display_table(found_books)
    else:
        print("No matching books found.")

# Function to display all books
def display_books():
    print("\nList of Books")
    if not books:
        print("No books available.")
    else:
        display_table(books)

# Function to display books in table format without external libraries
def display_table(book_list):
    print("\n{:<35} {:<25} {:<15} {:<10}".format("Title", "Author", "ISBN", "Available"))
    print("=" * 90)
    for book in book_list:
        print("{:<35} {:<25} {:<15} {:<10}".format(book["Title"], book["Author"], book["ISBN"], book["Available"]))
    print("=" * 90)

# Function to remove a book
def remove_book():
    print("\nRemove a Book")
    title = input("Enter book title to remove: ").strip().lower()

    if not title:
        print("Title cannot be empty!")
        return

    global books
    new_books = [book for book in books if book["Title"].lower() != title]

    if len(new_books) == len(books):
        print("Book not found!")
    else:
        books = new_books
        print(f"Book '{title}' has been removed successfully!")

# Main Program Execution
def main():
    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 1:
            add_book()
        elif choice == 2:
            search_book()
        elif choice == 3:
            display_books()
        elif choice == 4:
            remove_book()
        elif choice == 5:
            print("Thank you for using the Library System.")
            break

# Run the program
if __name__ == "__main__":
    main()