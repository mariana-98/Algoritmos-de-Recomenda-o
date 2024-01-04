print("***Testing string format:*** \n")

age = 25
name = "Genny"
relationship = "married"

print ("{} is {:>5} years old and she is {}".format(name, age, relationship))
print ("{} is {:<5} years old and she is {}".format(name, age, relationship))

print("\n______\n")

print (f"{name} is {age} years old and she is {relationship}")

print("\n______\n") #just to skip lines and separate de subject

print ("********************************************************")

print ("***Testing data input:*** \n")

print ("a) Two given numbers somatory:")
print("\n______\n")
a = int(input("Give the first number: "))
b = int(input("Please, give de second one: "))
print(f"The sum of the numbers gived previously is {a + b}")

print("\n______\n")
        
print ("b)Converting a given number from meters to centimeters:")
print("\n______\n")
meter_value = float(input("Please, insert your hight in meters: "))
#centimeter_value = meter_value * 100 -- it is not necessary if you use the 'f' and '{}.
print (f"In centimeters it is the same as {meter_value * 100} cm")

print("\n______\n")
print ("c) A resourse that receives a number of days, minuts and seconds from the user and returns it only in secconds:")
print("\n______\n")

days = int(input("Give e me de number of the days, please: "))
minuts = int(input("Now, the number of minuts: "))
seconds = int(input("Give de seconds: "))
print(f"In amount, the number of seconds that you have runned this time is exactelly {(days * 24 * 60 * 60) + (minuts * 60) + seconds} seconds. Congrates!!!")

print("\n______\n")
        
print ("d) Calculate the percentage incrises of the salary:")
print("\n______\n")

fomer_salary = float(input("How much wore you receiving in the past? \n R$ "))
currently_salary = float(input("How much do you receive now a days? \n R$ "))
print(f"Your salary was incrised in {(100 * currently_salary / fomer_salary) - 100:.2f}%.")

