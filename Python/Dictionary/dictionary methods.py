# to insert a key and value
a={'native':'kamareddy','village':'Jangampally'}
a['mandal']='bhiknoor'
print(a)
print('-----------------------------------------')

# to update a value(method-1)
a={'native':'kamareddy','village':'Jangampally'}
b={'native':'Jangampally','postalcode':503102}
a.update(b)
print(a)
print('-----------------------------------------')

# updating the value (method-2)
a={'native':'kamareddy','village':'Jangampally'}
a['native']='jangampally'
print(a)
print('-----------------------------------------')

