#count = 10

#if count > 20:
 #   print("Count is greater")
#else:
#    print("Count is not greater")

#if..elif..elif..else
#is_Fanta = False
#is_Coke = True
#is_Mirinda = False

#if is_Fanta:
 #   print("Buying Fanta")

#elif is_Coke:
 #   print("Buying Coke")

#elif is_Mirinda:
 #   print("Buying Mirinda")

 #else:
 #   print("Buying water")

#Nested If statememnts
#is_raining = False
#is_Sunny = True
#voting_age = 18

#age = int(input("How old are you? "))

#if age >= voting_age:
 #   if is_raining:
  #      print("Please move with your umbrella and go vote")
    
   # elif is_Sunny:
   #     print("Please wear light clothes and go to vote")
    
    #else:
     #   print ("Wear normal clothes")

#else:
 #   print("Sorry your ar unable to go for voting!")


#Write a program that coverts temperature based on the choice
# of the user. The figures should be from a user input. 
# Use if statement to check which conversion the user wants to perform.

print("================WELCOME TO OUR TEMPERATURE CONVERTER CALCULATOR==================")

temp = int(input("Please enter the temperature value you want to convert "))
conversionType = input("Enter 'C' if you want to convert from celicius or enter 'F' if you want to convert from fahrenheight ")

if conversionType == "C":
    result = (temp - 32) * 5/9 
    print("The teperature after conversion is "+ str(result)+ " degrees Fahrenheight")

elif conversionType == "F":
    result = (temp * 9/5) + 32
    print("The teperature after conversion is "+ str(result)+ " degrees celcius")

else:
    print("You have entered a wrong option")
    




