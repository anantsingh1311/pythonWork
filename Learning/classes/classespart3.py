# class Animal:
#     def __init__(self):
#         self.age = 1
#     def Age(self):
#         print(self.age)

# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         self.weight=2
#     def Weight(self):
#         print(self.weight)

# m = Mammal()

# print(m.age)
# print(m.weight)

# Using multilevel inheritence

from abc import ABC,abstractmethod

class InternalOperationException(Exception):
    pass



class Stream(ABC):
    def __init__(self):
        self.streamOpen = False
    def OpenStream(self):
        if self.streamOpen:
            raise InternalOperationException("Stream is already open")
        self.opened = True
        print("Stream Opened",self.opened)

    def CloseStream(self):
            if not self.streamOpen:
                raise InternalOperationException("Stream is already closed")
            self.opened = False
            print("Stream closed")

    @abstractmethod        
    def read(self):
         pass


class LocalStream(Stream):

     def read(self):
          print("Reading from local data")


class NetworkStream(Stream):

     def read(self):
          print("Reading from network")


# s = Stream()
# s.OpenStream()
# s.CloseStream()

n = NetworkStream()

# n.OpenStream()
# n.CloseStream()

n.read()
