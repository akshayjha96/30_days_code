#Implements the Book class' abstract display() method so it prints these lines:

#Title, a space, and then the current instance's title.
#Author, a space, and then the current instance's
#Price, a space, and then the current instance's .
from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
#Write MyBook class
class MyBook(Book):
    def __init__(self,title,author,price):
          super().__init__(title,author)
          self.price = price
    
    def display(self):
        #super(MyBook,self).display()
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Price: {}".format(self.price)) 

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()
