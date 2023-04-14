
# Function to search for a book in the text file
def search_book():
    search_cat = input("search for book by category, author, genre or isbn: ")
    
    try:
        with open(book_path, "r") as file:
            found = False
            for line in file:
                if search_cat in line:
                    found = True
                    print(line.strip())
            if not found:
                print("Book not found in the library.")

# Function to display all books in the text file
# category = ["fiction" ,"horror", "romance" , "history","fantasy","mystery","memoir","thriller","politics"]
book_path = "/Users/damacm172_/Desktop/Book_Store/The_Book_Management_System/Books.txt"
def display_books():
    try:
        with open(book_path, "r") as file:
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("No books found in the library.")
        
        

        # Main function to run the program
def main():
    while True:
        print("\nWelcome to the book management system!")
        print("1. Display all books")
        print("2. Add a book")
        print("3. Search for a book")
        print("4. Edit a book")
        print("5. Delete a book")
        print("6. Quit")


        choice = input("Enter your choice (1-6): ")
        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            edit_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            print("Thank you for visiting the book store, Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()