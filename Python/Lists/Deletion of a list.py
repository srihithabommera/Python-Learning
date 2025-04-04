# Create a list of your email, name, gender and age, then if the email is
# not gmail delete it, if the gender is male delete all elements from the list?
a=['srihitha@gmail.com','Srihitha','male',21]
for item in a:
    if item != 'Srihithabommera@gmail.com' or item == 'male':
        del a[0]
        print(a)
    elif a[2] == 'male':
        a.clear(a)
        print(a)