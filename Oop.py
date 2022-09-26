# class Parrot:
#     my_attribute = "Hello"

#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color

#     def __repr__(self):
#         return f"<Parrot {self.name} {self.age} {self.color}>"



# # parrot object
# parrot = Parrot("parrot", 12, "red")
# print(parrot.name)
# print(parrot.age)
# print(parrot.color)
# print(parrot.my_attribute)


# class parrot:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color

# parrot = parrot("Carol", 20, "Black")

# print(parrot.name)
# print(parrot.age)
# print(parrot.color)

# class car:
#     def __init__(self, model, color, brand, price):
#         self.model = model
#         self.color = color
#         self.brand = brand
#         self.price = price

# class Animal:
#     def __init__(self):
#         self.name = "cow"
#         self.color = "Brown"

#     def change_name(self, name):
#         self.name = name

#     def print_animal(self):
#         print(f"{self.name} {self.color}")


# cow = Animal()
# print(cow.name)
# cow.change_name("Some Cow")
# print(cow.name)

# cow.print_animal()



# class Car:
#     def __init__(self, model, color, brand, price):
#         self.model = model
#         self.color = color
#         self.brand = brand
#         self.price = price

#     def move(self, direction, speed):
#         print(f"{self.brand} is moving in {direction} direction at a speed of {speed} km/h")

#     def stop(self):
#         print(f"{self.brand} has stopped")

#     def update_price(self, price):
#         self.price = price
#         print(f"The new price is {self.price}")

# import time


# car_bmw = Car("X5", "Black", "BMW", 50000.0)
# # benz = Car(model, color, brand, price)
# # nissan = Car(model, color, brand, price)

# print(f"My car is a {car_bmw.color} {car_bmw.model} {car_bmw.brand} that costs {car_bmw.price}")

# car_bmw.move("North", 50)
# car_bmw.stop()
# car_bmw.update_price(600000.00)
# print(car_bmw.price)

# class Student:
#     def __init__(self, name, age, course):
#         self.name = name
#         self.age = age
#         self.course = course
# Student1 = Student("Nanostarlee", 25, "IST")
# Student2 = Student("Lauryn", 20, "AWS")
# Student3 = Student("Abigail", 22, "SE")

# print("STUDENT ONE")
# print(f"Name: {Student1.name} \nAge: {Student1.age} \nCourse: {Student1.course}\n")
# print("STUDENT TWO")
# print(f"Name: {Student2.name} \nAge: {Student2.age} \nCourse: {Student2.course}\n")
# print("STUDENT THREE")
# print(f"Name: {Student3.name} \nAge: {Student3.age} \nCourse: {Student3.course}")
        


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


        
