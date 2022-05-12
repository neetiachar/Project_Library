Instructions To use the Program

The Program is written in python. An IDLE(Integrated Development and Learning Environment) is needed to run it.
Open the program in IDLE and run it by adding the module instruction given below.

There are five modules

1 LookUp
   This method take an ISBN and prints all the catalog information about that book.
eg.
ObjLirarian.LookUp('9781472258229')

2 Adding the Book
  This method adds a book from the catalog to the library, and optionally add multiple copies of the same book at once.

ObjLibrarian.AddBooks('9781472258229')
ObjLibrarian.AddBooks('9781472258229', 3) Adds 3 copies at once.

3 Returning a Book.
  This method deals with returning of the book.
eg.
ObjLibrarin.ReturnBooks('9781472258229')

4. Borrowing a Book.
   This method deals with borrowing the book.
eg.
ObjLibrarian.BorrowBooks('9781472258229')

5. Stock.
   This metod gives the stock of the books.
eg.
ObjLibrarian.StockOfBooks()


  
