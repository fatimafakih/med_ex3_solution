class Book:
    
    def __init__(self,title, author, year):
        self.title=title
        self.author=author
        self.year=year
        self.is_checked_out=False
    
    def checkout(self):
        self.is_checked_out=True
    
    def return_book(self):
        self.is_checked_out=False
    
    def  __str__(self):
        return(f"{self.year} by {self.author} (Checked out: {self.is_checked_out})")
    
class Library:
    
    def __init__(self):
        self.collection=[]
    
    def add_book(self,book):
        self.collection.append(book)
    
    def list_books(self):
        for book in self.collection:
            print(book)
    
    def find_book(self, title):
        
       for book in self.collection:
           if book.title.lower() == title.lower():
              return book
       return None

    def available_books(self):
        available=False
        for book in self.collection:
            if book.is_checked_out==True:
                print(book)
                available=True
            
        if not available:
          print("No books are available at the moment.")
          
          


lib = Library()
book1 = Book("1984", "George Orwell", 1949)
book2 = Book("The Alchemist", "Paulo Coelho", 1988)

lib.add_book(book1)
lib.add_book(book2)

# Check available books
lib.available_books()  # Should print the details of available books

# Checkout a book
book1.checkout()

# Check available books again
lib.available_books()