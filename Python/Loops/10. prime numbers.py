#  Print all prime numbers from 0 to 100?
a=102
for i in range(1,a):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)