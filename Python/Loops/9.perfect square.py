# Print all perfect square numbers from 0 to 100?
# Using for loop.

perfect=0
for i in range(1,11):
    perfect=i*i
    print(i,'square','=',perfect)
print('----------------------------')
    
# using while loop
count=1
square=0
while count<11:
    square=count*count
    print(count,'Square','=',square)
    count+=1
print('----------------------------')
