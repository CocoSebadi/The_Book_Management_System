# Function to delete a book from the text file
def delete_book():
    isbn = input("Enter the isbn of the book to delete: ")
    try:
        with open(book_path, "r") as file:
            lines = file.readlines()
        with open(book_path, "w") as file:
            found = False
            for line in lines:
                if isbn in line:
                    found = True
                else:
                    file.write(line)
            if found:
                print("Book deleted successfully!")
            else:
                print("Book not found.")
    except FileNotFoundError:
        print("No books found.")
