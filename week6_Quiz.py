# class Test:
#      def __init__(self,a="Hello World"):
#          self.a=a
 
#      def display(self):
#          print(self.a)
# obj=Test()
# obj.display()

# class change:
#     def __init__(self, x, y, z):
#         self.a = x + y + z
 
# x = change(1,2,3)
# y = getattr(x, 'a')
# setattr(x, 'a', y+1)
# print(x.a)

# class test:
#      def __init__(self,a):
#          self.a=a
 
#      def display(self):
#          print(self.a)
# obj=test()
# obj.display()

# class A:
# 	def __init__(self,b):
# 		self.b=b
# 	def display(self):
# 		print(self.b)
# obj=A("Hello")
# del obj

# class test:
#     def __init__(self):
#         self.variable = 'Old'
#         self.Change(self.variable)
#     def Change(self, var):
#         var = 'New'
# obj=test()
# print(obj.variable)

# class fruits:
#     def __init__(self, price):
#         self.price = price
# obj=fruits(50)
 
# obj.quantity=10
# obj.bags=2
 
# print(obj.quantity+len(obj.__dict__))

# class Demo:
#     def __init__(self):
#         pass
 
#     def test(self):
#         print(__name__)
 
# obj = Demo()
# obj.test()

# # try:
# #     if '1' != 1:
# #         raise "someError"
# #     else:
# #         print("someError has not occurred")
# # except someError:
# #     print ("someError has occurred")

# class People():
#     def __init__(self, name): 
#         self.name = name

#     def namePrint(self): 
#         print(self.name) 

# person1 = People("Sally") 
# person2 = People("Louise") 
# person1.namePrint()

# class Pokemon():

#     def __init__(self, name, type):
#         self.name = name
#         self.type = type

#     def stringPokemon(self):
#         print(f"Pokemon name is {self.name} and type is {self.type}")

# class GrassType(Pokemon):

#     # overrides the stringPokemon() function on 'Pokemon' class
#     def stringPokemon(self):
#         print(f"Grass type pokemon name is {self.name}")

# poke1 = GrassType('Bulbasaur', 'Grass')
# poke1.stringPokemon
# poke1.stringPokemon()
# poke2 = Pokemon('Charizard', 'Fire')
# poke2.stringPokemon
# poke2.stringPokemon()

# class Book:
# 	def __init__(self,author):
# 		self.author=author
# book1=Book("V.M.Shah")
# book2=book1
# print(book2.author)

# class Demo:
#     def check(self):
#         return " Demo's check "
#     def display(self):
#         print(self.check())
# class Demo_Derived(Demo):
#     def check(self):
#         return " Derived's check "
# Demo().display()
# Demo_Derived().display()

# class A:
#     def __init__(self):
#         self.multiply(15)
#         print(self.i)
 
#     def multiply(self, i):
#         self.i = 4 * i
# class B(A):
#     def __init__(self):
#         super().__init__()
 
#     def multiply(self, i):
#         self.i = 2 * i
# obj = B()

# i = 0  
# while i < 5:  
#     print(i)  
#     i += 1  
#     if i == 3:  
#         break  
# else:  
#     print(0)  

# i = 1  
# while True:  
#     if i%3 == 0:  
#         break  
#     print(i)    

# class Std_Name:   
#     def __init__(self, Std_firstName, Std_Phn, Std_lastName):  
#         self.Std_firstName = Std_firstName  
#         self.Std_PhnStd_Phn = Std_Phn  
#         self.Std_lastName = Std_lastName  
   
# Std_firstName = "Wick"  
# name = Std_Name(Std_firstName, 'F', "Bob")  
# Std_firstName = "Ann"  
# name.lastName = "Nick"  
# print(name.Std_firstName, name.Std_lastName) 

# class book:  
#     def __init__(a, b):  
#         a.o1 = b  
   
# class child(book):  
#     def __init__(a, b):  
#         a.o2 = b  
   
# obj = page(32)  
# print ("%d %d" % (obj.o1, obj.o2) 

# class A:

# 	def __init__(self,num):

# 		num=3

# 		self.num=num

# 	def change(self):

# 		self.num=7

# a=A(5)

# print(a.num)

# a.change()

# print(a.num)

