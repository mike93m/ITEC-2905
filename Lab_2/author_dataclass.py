# Author dataclass
class Author:
    # #Each author gets a name and a list of books
    # You do not need to pass in the book list just the author name
    def __init__(self, name): 
        self.name = name
        self.books_published = []  # Book list 

    # Method to add a book to the authors list of books published
    def publish(self, book):
        if book not in self.books_published: # Verify book not already published
            self.books_published.append(book) # Add book to list
        else:
            print(f'Book "{book}" already published!') # Already published
        
    # String representation of the author and their books
    # Returns a nicely formated string instead of the object itself
    def __str__(self):
        books_published = self.books_published
        return (f'Books by: {self.name}: ' + ', '.join(books_published))

# Main function to demonstrate the Author class
def main(): 
    author = Author("Steve Stevenson") # Add the author name

    # Add the book titles to the list 
    author.publish("Cheese")
    author.publish("Crackers")
    author.publish("Crackers")

    #  Call the __str__ method to print the author and their books
    print(author)

main()