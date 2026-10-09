from abc import ABC, abstractmethod
class ABSabstract(ABC):
    
    def print(self, x):
        print(x)

    @abstractmethod
    def task(self):
        print('I am inside the abstract class')

class test(ABSabstract):

    def task(self):
        print('I am inside the test class')

test_obj = test()
test_obj.print(1000)
test_obj.task()