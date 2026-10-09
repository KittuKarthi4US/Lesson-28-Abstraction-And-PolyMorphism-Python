from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print('I can walk and run')

class Snake(Animal):
    def move(self):
        print('I can slither')

class Dog(Animal):
    def move(self):
        print('I can bark')

class Lion(Animal):
    def move(self):
        print('I can bark')

L = Lion()
L.move()

S = Snake()
S.move()

H = Human()
H.move()

D = Dog()
D.move()
