# how to use logger in python inside class

# Path: utils\logger.py
# Compare this snippet from utils\classes.py:

# # this file refers to topics related to classes in python

import logging

# create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"

class User:
    # constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter(LOG_FORMAT)
        file_handler = logging.FileHandler('user.log')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def greeting(self):
        self.logger.info(f'{self.name} has logged in.')
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# init user object
brad = User('Brad Traversy', 'brad@email.com', 23)

# call method
print(brad.greeting())

