#1. Create a 2-D array and slice out the 
# second number in the second column
print("Question 1")
arr = [[7, 30, 2, 3], [10, 12, 11, 21,], [20, 13, 15, 8,]]
print(arr[1][1])
print("===========================================================")

#2. Write a python program to sort array element in the ascending/descending order
print("Question 2")
n = int(input("Enter size of an array: "))
arr = list(map(int, input("Enter elements in of an array: \n") .split()))
arr.sort(revers = False)
print("Ascending order array")
print(arr)
arr.sort(reverse = True)
print("Descending order array")
print(arr)
print("===========================================================")

#3. Write a python program to find the maximum 
# and minimum value in a given 2-D array
print("Question 3")
n = int(input("Enter size of an array: "))
arr = list(map(int, input("Enter elements in of an array: \n") .split()))
print("The array is: " + str(arr))
print("The maximum number in the array")
print(max(arr))
print("The minimum number in the array")
print(min(arr))
print("===========================================================")

# 4. Write a python program to input 5 subject marks and 
# calculate total marks, percentage and grade based on following criteria
# percentage less than 50 (Grade C)
# percentage equal to 50 and less than 80 (Grade B)
# percentage equal to 80 and more than 80 (Grade A)
print("Question 4")
from audioop import add
import math
sub = int(input("Enter the number of subjects you sat for: "))
marks = list(map(int, input("Enter marks got for all the five subjects: ") .split()))
total = sum(marks)
print("The total marks got is: "+ str(total))
percentage = (total/500) * 100
print("The percentage total mark got is: "+str(percentage) + "%")
if percentage < 50:
    print("Your grade is 'C' Tried")
elif percentage == 50 or percentage < 80:
    print("Your grade is 'B' Very good")
elif percentage == 80 or percentage > 80:
    print("Your grade is 'A' Excellent")
else:
    print("Failed")
print("===========================================================")

#5. Write a python program to fetch only Email ID 
# from text file which include following fields -:
# Name
# Mobile Number
# Roll Number
# Email ID
print("Question 5")

print("===========================================================")

# 7. Write a function called show_stars(rows).
#  If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****
print("Question 7")
rows = int(input("Enter the number of rows: "))
# outer loop
for i in range(rows):
    # nested loop
    for j in range(i):
        # display number
        print("*", end=' ')
    # new line after each row
    print('')
print("===========================================================")


#11. Write a function to compute 5/0 and 
# use try/except to catch the exceptions.
def divide(x, y):
    try:
        result = x / y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Math error ! You are dividing by zero ")

a = int(input("Enter your numerator:\n"))
b = int(input("Enter your denominator:\n"))
divide(a, b)
print("===========================================================")
