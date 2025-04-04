print('1.------------------------------------')
#string reversal
def string_reversal(s):
    return s[::-1]
s="Hello World"
print(string_reversal(s))

print('2.------------------------------------')
#string palindrome
def is_palindrome(s):
    a=s[::-1]
    if s==a:
        return 'True'
s="kissik"
print(is_palindrome(s))


print('3.------------------------------------')
#substring in a string
def sub_string(s):
    if sub in s:
        return 'True'
    else:
        return 'False'
s='Hello Srihitha'
sub='Hell'
print(sub_string(s))


print('4.------------------------------------')
# string uppercase
def upper_case(s):
    return s.upper()
s='bommera srihitha'
print(upper_case(s))



print('5.------------------------------------')
# string vowel count
def string_vowel_count(s):
    count=0
    for i in s:
        if i in vowel:
            count+=1
    return count
s='i am learning Python'
vowel='aeiou'
print(string_vowel_count(s))


print('6.------------------------------------')
# string character frequency
def char_frequency(s):# s=hello
    dic={}
    for c in s:
        if c in dic:
            dic[c]+=1
        else:
            dic[c]=1
    return dic
s='hello'
print(char_frequency(s))


print('7.-----------------------------------------')
# FizzBuzz
def numbers(num):
    for i in num:
        if i%3==0 and i%5==0:
            print('FizzBuzz')
        elif i%5==0:
            print('Buzz')
        elif i%3==0 :
            print('Fizz')
        else:
            print(i)
num=range(0,100)
print(numbers(num))


print('8.-----------------------------------------')
# contains duplicate
def duplicate(nums):  #1231
    a=len(set(nums))
    if a!=len(nums):
        return 'True'
    else:
        return 'False'
nums=[1,2,3,1]
print(duplicate(nums))


print('9. ----------------------------------------------')
# reverse list
def reverse_list(number):
    return number[::-1]
number=[1,2,3,4,5]
print(reverse_list(number))


print('10.---------------------------------------------')
# number is palindrome
def num_palindrome(num):
    a=num[::-1]
    if a==num:
        return 'true'
    else:
        return 'False'
num=[1,2,3,4,3,2,1]
print(num_palindrome(num))


print('11.-------------------------------------------------')
def fibonacci(n):
    fib=[]
    a,b=0,1
    c=a+b
    a=b
    b=c
    d=fib.append(b)
    print(fib)
n=5
print(fibonacci(n))

print('12.---------------------------------------------------')
def prime_number(f):
    for i in range(2,f+1):
        if f%i==0:
            return 'Not Prime'
        else:
            return 'Prime'
f=int(input('Enter a number: '))
print(prime_number(f))