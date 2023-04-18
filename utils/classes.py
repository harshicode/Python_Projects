# how to use setter and getter methods of a class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    def __ne__(self, other):
        return self.name != other.name or self.age != other.age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __le__(self, other):
        return self.age <= other.age
    
    def __gt__(self, other):
        return self.age > other.age
    


if __name__ == "__main__":
    p1 = Person("John", 20)
    print(p1)
    print(p1.get_name())
    print(p1.get_age())
    p1.set_name("Jane")
    p1.set_age(30)
    print(p1)
    print(p1.get_name())
    print(p1.get_age())

    p2 = Person("John", 20)
    print(p1 == p2)
    print(p1 != p2)
    print(p1 < p2)
    print(p1 <= p2)
    print(p1 > p2)
    print(p1 >= p2)
    