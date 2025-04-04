print('1.-------------------------------------------------------------')
# reversing a list
def reversing(a):
    return (a[::-1])
a=[1,2,3,4,5]
print(reversing(a))

print('2.-------------------------------------------------------------')
# sort a list
def sort_list(b):
    return (sorted(b))
b=[3,6,2,8,9,5]
print(sort_list(b))

# find the max value in a list
print('3.------------------------------------------------------------')
def max_val(c):
    return max(c)
c=[34,7,3,6,9]
print(max_val(c))


# find the max value in a list
print('4.------------------------------------------------------------')
def min_value(d):
    return min(d)
d=[5,3,5,8,9,9,32]
print(min_value(d))


print('5.-----------------------------------------------------------')
# check if an element exists in a list
def check_element(input_list,target):
        return target in input_list
input_list=[2,3,4,5,5,6,7,8,9]
target=5
print(check_element(input_list,target))

print('6.----------------------------------------------------------')
# removing the duplicates
def duplicates(g):
    return list(set(g))
g=[2,3,3,4,4,5,5,6,7,6,8,9]
print(duplicates(g))


print('7.----------------------------------------------------------')
# finding the index of an element
def find_index(list_input,target):
    return (list_input.index(target))
list_input=[2,3,4,5,6,7]
target=6
print("The index of 6 is",find_index(list_input,target))

print('8.------------------------------------------------------------')
# insert element at a specific position in a list
def insert_element(input_list,target,position):
    input_list.insert(position,target)
    return input_list
input_list=[1,2,3,5,6,7,8]
target=4
position=3
print(insert_element(input_list,target,position))


print('9.------------------------------------------------------------')
# remove an element from a list
def remove_list(input_list,target):
    input_list.remove(target)
    return input_list
input_list=[3,4,5,5,6,7,8]
target=5
print(remove_list(input_list,target))


print('10.----------------------------------------------------------')
# sort a list of strings
def list_sorting(list_input):
    return sorted(list_input)
list_input=['mango','banana','apple','custard apple']
print(list_sorting(list_input))

print('11.----------------------------------------------------------')
# Find the second largest element in a list
def second_largest(list_input):
    a=sorted(list_input)
    return (a[-2])
list_input=[1,4,5,7,8,10]
print(second_largest(list_input))

print('12.----------------------------------------------------------')
# check if two lists are identical or not
def identical_lists(list_1,list_2):
   return list_1==list_2
list_1=[1,2,3,4]
list_2=[1,2,3,4]
print(identical_lists(list_1,list_2))

print('13.----------------------------------------------------------')
# Find the commaon elements in two lists'
def common_elements(input_list1,input_list2):
    a=[]
    for i in input_list1:
        if i in input_list2:
            a.append(i)
    return (a)
input_list1=[1,2,3]
input_list2=[4,5,6]
print(common_elements(input_list1,input_list2))

print('14.------------------------------???----------------------------')
# Remove empty strings from a list
def removing_empty_string(str_input):
    for char in str_input:
        if char=='' and "":
            return str_input.remove('' and "")
str_input=["hello",'',"world",""]
print(removing_empty_string(str_input))

print('15.---------------------------------------------------')
# check if a list is sorted
def sorted_list(list_input):
    return list_input==sorted(list_input)
list_input=[1,2,3,4,5]
print(sorted_list(list_input))