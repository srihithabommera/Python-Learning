''' create a program that takes the marks of a student in different subjects as input. calculate 
the total marks and average, and then display the corresponding grade based on the average'''
math,science,english=85,90,78
total=85+78+90
print("The sum of three subjects is",total)
average=total/3
print("The Average of three subjects is",average)
if average>90:print("Grade-A")
elif average>80 and average<90:print("Grade-B")
elif average>70 and average<80:print("Grade-C")
elif average>60 and average<50:print("Grade-D")
else:print("You had failed the subjects.")