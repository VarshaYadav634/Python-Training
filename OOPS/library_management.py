'''
task: Library book management
objective: use python classes to model how books are added and issued in a
library
 
task description: create a class called Book
 
the class should have:
1. constructor that accepts account holder book title, author,ISBN number,
Availability status
2. a method display_info()- prints book details
3. a method issue_book()- sets availability to "issued" if available
4. a method return_book()- sets availability back to "available"
'''
'''
task: Library book management
objective: use python classes to model how books are added and issued in a
library
 
task description: create a class called Book
 
the class should have:
1. constructor that accepts account holder book title, author,ISBN number,
Availability status
2. a method display_info()- prints book details
3. a method issue_book()- sets availability to "issued" if available
4. a method return_book()- sets availability back to "available"
'''
class book:
    def __init__(self,book_title,author,isbn,availability):
        self.book_title=book_title
        self.author=author
        self.isbn=isbn
        self.availability=availability
    def display_info(self):
        print("Book title: ",self.book_title)
        print("Author: ",self.author)
        print("ISBN number: ",self.isbn)
        print("Availability: ",self.availability)
        print( )
    def issue_book(self):
        if self.availability:
            self.availability=False
        else:
            print("Book not available")
    def return_book(self):
        self.availability=True
b1=book("abc","xyz",12,True)
b1.display_info()
b1.issue_book()
b1.display_info()
b1.return_book()
b1.display_info()

