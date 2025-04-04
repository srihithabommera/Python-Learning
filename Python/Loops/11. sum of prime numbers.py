#  Find sum of all prime numbers from 0 to 100?
sum=0
for i in range(0,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sum+=i
        print(sum)
print('----------------------------')