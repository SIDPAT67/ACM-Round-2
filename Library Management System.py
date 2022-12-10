
import sys
class Library:
      def __init__(self,listofbooks):
            self.availablebooks=listofbooks

      def displayAvailablebooks(self):
                   print("|=================================================|")
                   print("|The books we have in our library are as follows: |")
                   print("|=================================================|")
                   for book in self.availablebooks:
                         print(book)
                   print("================================================")     
      def lendBook(self,requestedBook):
            if requestedBook in self.availablebooks:
                  print("The book you requested has been borrowed.")
                  print("Thanks for using our portal.")
                  self.availablebooks.remove(requestedBook)
            else:
                  print("Sorry the book you have requested is currently not in the library.")
                  
      def addBook(self,returnedBook):
            self.availablebooks.append(returnedBook)
            print("Thanks for returning your borrowed book.")
            

class Student:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow:")
            self.book=input()
            return self.book

      def returnBook(self):
            print("Enter the name of the book you'd like to return:")
            self.book=input()
            return self.book

def main():            
      library=Library(["Thomas Calculus",
                       "An Introduction to Mechanics",
                       "Elements of Physical Chemistry",
                       "Vibration & Waves",
                       "Foundation of Electrical Engineering",
                       "Engineering Graphics with AutoCAD",
                       "Solonon's Organic Chemistry"])
      student=Student()
      home=False
      while home==False:
            print("__________________________________")
            print("|          LIBRARY MENU          |")
            print("|________________________________|")
            print("|1. Display all available books  |")     
            print("|2. Request a book               |")
            print("|3. Return a book                |")
            print("|4. Exit                         |")
            print("|________________________________|")
                  
            choice=int(input("Enter Choice:"))
            if choice==1:
                library.displayAvailablebooks()
            elif choice==2:
                library.lendBook(student.requestBook())
            elif choice==3:
                library.addBook(student.returnBook())
            elif choice==4:
                  sys.exit()
            

                  
main()
