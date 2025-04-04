'''Build a temperature converter program that allows the user to convert temperature between 
celsius, kelvin and Fahrenheit.'''
temp=int(input("Enter the Temperature: "))
unit=input("Enter Units: ")
if unit=="K":print(273+temp)
elif unit=="F":print(temp*(9/5)+32)
else:print("Enter valid Units.")