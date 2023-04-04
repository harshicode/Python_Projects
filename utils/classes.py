# this file refers to topics related to classes in python

# class is a blueprint for creating objects
# an object has properties and methods(functions) associated with it

# create a class
class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# extend class
class Customer(User):
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'
    
# init user object
brad = User('Brad Traversy', 'brad@email.com', 25)

# init customer object
sem = Customer('Adam', 'adam@email.com', 27)

# edit property
brad.age = 37

# call method
print(brad.greeting())

# call method
print(sem.greeting())

# call method
sem.set_balance(500)
print(sem.greeting())

