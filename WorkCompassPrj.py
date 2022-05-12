

class Librarian:
    ListOfBooks=[]

    def LookUp(self,idno):
        found=False 
        for x in self.ListOfBooks:
            if x.ISBN==idno:
                print(x.Name +"," + x.Author +"," + "(" + x.Year+ ")")
                found=True
        Librarian.CheckForValue(found)

    def AddBooks(self,idno,num=1):
        found=False   
        for x in self.ListOfBooks:
            
            if x.ISBN==idno:
                x.NoOfCopies=x.NoOfCopies+num
                x.AvailableCopies=x.AvailableCopies+num
                found=True
        Librarian.CheckForValue(found)        
         
    def BorrowBooks(self,idno):
        found=False
        for x in self.ListOfBooks:
            if x.ISBN==idno:
              x.AvailableCopies-=1
              found=True
        Librarian.CheckForValue(found)

        
    def ReturnBooks(self,idno):
        found=False
        for x in self.ListOfBooks:
            if x.ISBN==idno:
              x.AvailableCopies+=1
              found=True
        Librarian.CheckForValue(found)      
              

    def StockOfBooks(self):
        for x in self.ListOfBooks:
            print( "{} Copies:{} Available:{}".format(x.ISBN,x.NoOfCopies,x.AvailableCopies))
      
    def CheckForValue(found):
        if found==False:
            print("Please give valid ISBN")
    
        
        
    
class book:
    def __init__(self,idno,name,author,year):
        self.ISBN=idno
        self.Name=name
        self.Author=author
        self.Year=year
        self.NoOfCopies=1
        self.AvailableCopies=1

        
        
ObjLibrarian=Librarian()

ObjLibrarian.ListOfBooks.append(book('9780143111597',"The Left Hand of Darkness","Ursula K. Le Guin","1979"))
ObjLibrarian.ListOfBooks.append(book('9781472258229',"Kindred","Octavia E. Butler","1979"))
ObjLibrarian.ListOfBooks.append(book('9780441569595',"Neuromancer","William Gibson","1984"))
ObjLibrarian.ListOfBooks.append(book('9781857231380',"Consider Phlebas","Iain M. Banks","1987"))
ObjLibrarian.ListOfBooks.append(book('9780553283686',"Hyperion","Dan Simmons","1989"))


ObjLibrarian.AddBooks('9781472258229',3)
ObjLibrarian.BorrowBooks('9781472258229')
ObjLibrarian.StockOfBooks()




