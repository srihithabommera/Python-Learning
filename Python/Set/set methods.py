# using add()
a={1,2,3,4,5}
a.add(6)
print(a)

# using update()
a={1,2,3,4,5}
b={6,7,8}
a.update(b)
print(a)
 
# using copy()
a={1,2,3,4,5}
b=a.copy()
print(b)

# exercise:- 
''' Create set of files ~ ( Img_01.png, Avatar.mp4 ), add new file ‘Track01.mp3’ 
then Rename ‘Track01.mp3’ to ‘Music01.mp3’, finally Copy all files  to new set 
(Folder)?'''
file={"Img_01.png","Avatar.mp4"}
file.add("Track01.mp3")
print(file)
print("-------------------------------")
b=file.copy()
print(b)
print('---------------------------------------')

# pop()
a={"srihitha","pavithra","swajith","ganesha","Vignith"}
print(a.pop())


# remove()
#a={"srihitha","pavithra","swajith","ganesha","vignith"}
a={1,2,3,4,5}
#a.remove("pavithra")
a.remove(4)
print(a)

# discard()
a={"srihitha","pavithra","swajith","ganesha","Vignith"}
a.discard("srihitha")
print(a)

# clear()
a={"srihitha","pavithra","swajith","ganesha","Vignith"}
a.clear()
print(a)

# frozenset()
a={"srihitha","pavithra","swajith","ganesha","Vignith","ganesha","ganesha"}
b=frozenset(a)
print(b)
print(type(b))

#min
a={"srihitha","pavithra","swajith","ganesha","vignith","ganesha","ganesha"}
print(min(a))
print(max(a))
print(len(a))
b={1,2,3,4,5,5}
print(sum(b))
