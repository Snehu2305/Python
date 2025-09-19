class Book:
   def __init__(self, title, author):
    self.__title = title
    self.__author = author
    self.__available = True
   
   def getTitle(self):
     return self.__title
   
   def isAvailabe(self):
     return self.__available
   
   def borrow(self):
     if self.__available:
       self.__available = False
       return True
     return False
   
   def returnBook(self):
     self.__available = True

class Member:
   def __init__(self, name, memberId, limit):
     self.name = name
     self.memberId = memberId
     self.limit = limit
     self.borrowedBooks = []

   def borrowBook(self, book):
       if len(self.borrowedBooks) < self.limit and book.borrow():
         self.borrowedBooks.append(book)
         print(f"{self.name} borrowed {book.getTitle()}")
       else:
         print(f"{self.name} can't borrow {book.getTitle()}")

   def returnBook(self, book):
       if book in self.borrowedBooks:
         book.returnBook()
         self.borrowedBooks.remove(book)
         print(f"{self.name} returned {book.getTitle()}")
         
class StudentMember(Member):
  def __init__(self, name, memberId):
    super().__init__(name, memberId, limit = 3)

class FacultyMember(Member):
  def __init__(self, name, memberId):
    super().__init__(name, memberId, limit = 5)


b1 = Book("FireOfWings", "Kalam")
b2 = Book("Shivcharitra", "Desai")

m1 = StudentMember("Snehal", 108)
m2 = FacultyMember("Prof.Kumbhar", 123)

m1.borrowBook(b1)
m1.borrowBook(b2)
m1.borrowBook(b1)
m1.returnBook(b1)
m2.borrowBook(b1)
   