# 9 questions about classes, objects, inheritance, polymorphism, queues, stacks, 
# and more

# 1. create a credit card class with the following attributes: card number,
#  expiration date, and security code. Create a method that will print out 
# the card number, expiration date, and security code. Create an instance 
# of the class and call the method.

print("QUESTION ONE")
class credit_card:
    def __init__(self, card_number, expiration_date, security_code):
        self.card_nmber = card_number
        self.expiration_date = expiration_date
        self.security_code = security_code
    
    def card_details(card_number, expiration_date, security_code):
        card_number = int(input("Enter your card number: "))
        expiration_date = (input("Enter your card number expiration date: "))
        security_code = int(input("Enter your card number's security code: "))

        print(f"\nYOUR CREDIT CARD DETAILS ARE: \n\nCard Number: {card_number}\
            \nExpiration Date: {expiration_date}\nSecurity Code: {security_code}")

card = credit_card(int,"",int)
print(credit_card.card_details(int,"", int))

# 2. create Animal class and Dog class. Make the Dog class inherit from the
#  Animal class. Add a bark method to the Dog class. Create an instance of the 
# Dog class and call the bark method.
print("QUESTION TWO")
class Animal:
    def __init__(self, family):
        self.family = family
class Dog(Animal):
    def __init__(self, family, sound):
        super().__init__(family)
        self.sound = sound
    def bark(self):
        return print(f"The dog {self.sound} and comes from the {self.family} family")

Dog = Dog("cat", "barks")
print(Dog.bark())

# 3. create a class called Queue. The class should have the following methods: 
# enqueue, dequeue, and size. The enqueue method should add an item to the queue. 
# The dequeue method should remove an item from the queue. The size method should 
# return the size of the queue.

print("QUESTION THREE")
class Queue:
    def __init__(self):
        self.queue = list()
    
    def enqueue(self, data):
        self.queue.append(data)
        return True
    
    def isEmpty(self):
        return len(self.queue) == 0

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(1)

    def size(self):
        return len(self.queue)
    
    def display(self):
        return self.queue

# creating a Queue object
q=Queue()

print(q.dequeue())
q.enqueue('Lawrence')
q.enqueue('Ssettuba')
q.enqueue('Is a Programmer')
print(q.display())
print(q.size())
print(q.dequeue())
print(q.size())

# 4. create a class called Stack. The class should have the following methods: push, 
# pop, and size. The push method should add an item to the stack. The pop method should
#  remove an item from the stack. The size method should return the size of the stack.

print("QUESTION FOUR")
class stack:
    def __init__(self):
        self.stack = list()
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self, data):
        if self.isEmpty():
            return ("Stack is empty :(")
        return self.stack.pop(0)
    
    def size(self):
        return len(self.stack)

    def show(self):
        return self.stack

st = stack()
st.push("python")
st.push("java")
st.push("C#")
st.push("C++")
st.push("HTML")
st.push("CSS")

print(st.show())
print(st.size())
print(st.pop(0))
print(st.show())
print(st.size())

# 5. create a class called Person. The class should have the following attributes: 
# name, age, and address. The class should have the following methods: eat, sleep, 
# and work. The eat method should print out the name of the person and the word 
# "is eating". The sleep method should print out the name of the person and the word
#  "is sleeping". The work method should print out the name of the person and the word
#  "is working".

print("QUESTION FIVE")
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    
    def eat(self):
        return f"{self.name} is eating and he is {self.age} years old"
    
    def sleep(self):
        return f"{self.name} is sleeping and he is {self.age} years old"
    
    def work(self):
        return f"{self.name} is working at {self.address}"

p = Person("Lawrence", 25, "Kampala")
print(p.eat()+"\n"+p.sleep()+"\n"+p.work())

# 6. create a class called Employee. The class should have the following attributes:
#  name, age, and salary. The class should have the following methods: eat, sleep, 
# and work. The eat method should print out the name of the person and the word "is 
# eating". The sleep method should print out the name of the person and the word "is
#  sleeping". The work method should print out the name of the person and the word 
# "is working". Create a subclass of Employee called Programmer. The Programmer class 
# should have the following attributes: name, age, salary, and programming language. 
# The Programmer class should have the following methods: eat, sleep, work, and code. 
# The code method should print out the name of the person and the word "is coding in" 
# and the programming language. Create an instance of the Programmer class and call all 
# the methods.

print("QUESTION SIX")
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def eat(self):
        return f"{self.name} is eating"
    def sleep(self):
        return f"{self.name} is sleeping"
    def work(self):
        return f"{self.name} is working"
class Programmer(Employee):
    def __init__(self, name, age, salary, programming_language):
        super().__init__(name, age, salary)
        self.programming_language = programming_language
    def eat(self):
        return f"{self.name} is eating"
    def sleep(self):
        return f"{self.name} is sleeping"
    def work(self):
        return f"{self.name} is working"
    def code(self):
        return f"{self.name} is coding in a {self.programming_language} programming language"

Prog = Programmer("Nanostarlee",25,2000000,"Python")
print(Prog.eat())
print(Prog.sleep())
print(Prog.work())
print(Prog.code())

# 7. create a class called Vehicle. The class should have the following attributes: 
# make, model, and year. The class should have the following methods: start, stop, and 
# drive. The start method should print out the make, model, and year of the vehicle and 
# the word "is starting". The stop method should print out the make, model, and year of 
# the vehicle and the word "is stopping". The drive method should print out the make, 
# model, and year of the vehicle and the word "is driving". Create a subclass of Vehicle 
# called Car. The Car class should have the following attributes: make, model, year, and 
# color. The Car class should have the following methods: start, stop, drive, and park. 
# The park method should print out the make, model, year, and color of the car and the 
# word "is parking". Create an instance of the Car class and call all the methods.

print("QUESTION SEVEN")
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        return f"The {self.make} {self.model} {self.year} is starting."
    def stop(self):
        return f"The {self.make} {self.model} {self.year} is stopping."
    def drive(self):
        return f"The {self.make} {self.model} {self.year} is driving itself."
class Car(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year)
        self.color = color
    def start(self):
        return f"The {self.make} {self.model} {self.year} is starting."
    def stop(self):
        return f"The {self.make} {self.model} {self.year} is stopping."
    def drive(self):
        return f"The {self.make} {self.model} {self.year} is driving itself."
    def park(self):
        return f"The {self.make} {self.model} {self.year} {self.color} car is parking"

C = Car("Toyota", "V8", 2020, "Black")

print(C.start())
print(C.stop())
print(C.drive())
print(C.park())

# 8. create a class called Animal. The class should have the following attributes: name, 
# color, and age. The class should have the following methods: eat, sleep, and make_sound.
# The eat method should print out the name of the animal and the word "is eating". 
# The sleep method should print out the name of the animal and the word "is sleeping". 
# The make_sound method should print out the name of the animal and the word "is making 
# a sound". Create a subclass of Animal called Dog. The Dog class should have the 
# following attributes: name, color, age, and breed. The Dog class should have the 
# following methods: eat, sleep, make_sound, and bark. The bark method should print out
#  the name of the dog and the word "is barking". Create an instance of the Dog class and 
# call all the methods.

print("QUESTION EIGHT")
class Animal:
    def __init__(self, name, color, age):
        self.name = name
        self.color = color
        self.age = age
    def eat(self):
        return f"The {self.name} is eating"
    def sleep(self):
        return f"The {self.name} is sleeping"
    def make_sound(self):
        return f"The {self.name} is making a sound"

class Dog(Animal):
    def __init__(self, name, color, age, breed):
        super().__init__(name, color, age)
        self.breed = breed
    def eat(self):
        return f"The {self.name} is eating"
    def sleep(self):
        return f"The {self.name} is sleeping"
    def make_sound(self):
        return f"The {self.name} is making a sound"
    def bark(self):
        return f"The {self.name} dog is barking"

d = Dog("Max", "Black", 3, "German Shepherd")
print(d.eat())
print(d.sleep())
print(d.make_sound())


# 9. create a class of your choice. It should have at least 3 attributes and 3 methods 
# where one of the methods is a static method. Implement polymorphism, encapsulation, 
# and inheritance.
from datetime import date
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # a class method to create a Person object by birth year.
    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)
 
    # a static method to check if a Person is adult or not.
    @staticmethod
    def isAdult(age):
        return age > 18
 
 
person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)
 
print(person1.age)
print(person2.age)
 
# print the result
print(Person.isAdult(22))