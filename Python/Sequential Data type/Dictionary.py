dict={"name":"Srihitha","age":21,"Qualification":"B.tech"}
print(dict['name'])
print("--------------------------------------------------")
# Accesing only keys using loops
for keys in dict:
    print(keys)
print("--------------------------------------------------")
# Accesing only values using loops
for value in dict.values():
    print(value)
print("--------------------------------------------------")
# Accesing both keys and values using loops
for keys,values in dict.items():
    print(keys,values)
print("--------------------------------------------------")
# Dictionary Comprehension.
mul={x: x*2 for x in range(1,6)}
print(mul)