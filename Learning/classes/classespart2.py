# # Setting up a class to create our own custom object example:
# class TagCloud:
#     # defining an empty dictionary named tags
#     def __init__(self):
#         self.__tags = {}

#     def __str__(self):
#         return f"{self.__tags}"

#     def add(self,tag):
#         # To check if tag is empty, if not we increment it by 1 and save it under the variable name:
#         self.__tags[tag.lower()] = self.__tags.get(tag.lower(),0) + 1

#     def __len__(self):
#         return len(self.__tags)


# cloud = TagCloud()

# cloud.add("python")
# cloud.add("python")
# cloud.add("python")
# cloud.add("Python")

# print(len(cloud))
# print(cloud)
# print(cloud.__tags)

# class Animals:

#     def __init__(self,__animal):
#         self.__animal = __animal

#     def __str__(self):
#         return f"{self.__animal}:{self.petSound}"

#     @property
#     def petSound(self):

#         if self.__animal.lower()=="dog":
#             return "woof"
#         elif self.__animal.lower()=="cat":
#             return "meow"
#         return "Animal sound unregistered"
        

#     @petSound.setter
#     def petSound(self,pet):
#         self.__animal = pet


# pet = Animals("Cow")

# print(pet.petSound)

# Inheritance works this way in Python

class Animals:

    def __init__(self,age):
        self.age = age

    def __str__(self):
        return f"{self.age}"

class Mammal(Animals):

    def walk(self):
        return f"Walking"
    def __str__(self):
        return super().__str__()

class cat(Animals):

    def sound(self):
        return f"Meow"
    


m = Mammal(10)

print(m.age)

print(m)