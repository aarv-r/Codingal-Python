from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass
class Human(Animal):
    def move(self):
        print("I can walk and run")
class Snake(Animal):
    def move(self):
        print("I can slither")
class Dog(Animal):
    def move(self):
        print("I can bark and run")
class Gorilla(Animal):
    def move(self):
        print("I can climb and run") 
R = Human()
R.move()

K = Snake()
K.move()

R = Dog()
R.move()

K=Gorilla()
K.move()
