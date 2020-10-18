import random
from src.sort import *

class man:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # @property
    # def age(self):
    #     return self.age

    # @age.setter
    # def age(self, val):
    #     self.age = val

    def __repr__(self):
        return f"{self.name} : {self.age}"

    def __lt__(self, other):
        return self.name < other.name
    
    def __gt__(self, other):
        return self.name < other.name

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


def name_gen():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    length = random.randint(3, 8)
    name = ""
    for i in range(length):
        name += random.choice(alphabet)
    return name

men = set()
for i in range(10):
    new_man = man(name_gen(), random.randint(18, 80))
    men.add(new_man)

print(men)
print(bubble_sort(men))
