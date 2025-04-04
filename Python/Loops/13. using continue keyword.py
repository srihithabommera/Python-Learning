# Print all prime numbers from 1 to 100 except numbers divisible by 3 ?
for i in range(1,100):
    if i==3:
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)