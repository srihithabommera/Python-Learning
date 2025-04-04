#  Create a list of your email, name, gender and age, then print your name?
details=['srihitha@gmail.com','Srihitha','Female',21]
print(details[1])
print('-----------------------------------------------------------------')


# Create a list of your email, name, gender and age, then append your password
# and insert your username to the list at index 1.
a=['srihitha@gmail.com','Srihitha','Female',21]
a.append('Ganesha@756')
print(a)
a.insert(1,'Bommera_Srihitha')
print(a)
print('-----------------------------------------------------------------')

#Create a list of your email, name, gender and age, then create another list which 
# contains your birth date, month, year and extend/add it to former list?
b=['srihitha@gmail.com','Srihitha','Female',21]
c=['30-06-2003']
#b+=c
b.extend(c)
print(b)
print('-----------------------------------------------------------------')

