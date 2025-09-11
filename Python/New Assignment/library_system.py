class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")

class EBook(Book):
    def __init__(self, title, author, price, size):
        super().__init__(title, author, price)
        self.size = size
    
    def display(self):
        super().display()
        print(f"File Size: {self.size} MB")

class PrintedBook(Book):
    def __init__(self, title, author, price, no_of_pages):
        super().__init__(title, author, price)
        self.numberOfPages = no_of_pages
    
    def display(self):
        super().display()
        print(f"Number of Pages: {self.numberOfPages}")

# Example usage and testing
if __name__ == "__main__":
    # Create instances
    regular_book = Book("Y", "X", 15)
    ebook = EBook("A", "B", 20, 30)
    printed_book = PrintedBook("C", "D", 45, 350)
    
    print("=== Regular Book ===")
    regular_book.display()
    
    print("\n=== EBook ===")
    ebook.display()
    
    print("\n=== Printed Book ===")
    printed_book.display()