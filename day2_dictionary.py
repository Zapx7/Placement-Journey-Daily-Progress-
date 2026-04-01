#q1
info={'name':'Karan','age':19 , 'gender':'female','eligible':True,'class':10}
print(info)

#q2
info['year']=2007
print(info)

#q3
print(info['name'])
print(info.get('name'))

#q4
print("All keys ")
for keys in info.keys():
    print(keys)

print("\n All values")
for values in info.values():
    print(values)

print("\n All items")
for key,value in info.items():
    print(f"{key}:{values}")

#q5
info.pop('name')
print(info)


#q6
for key,value in info.items():
    print(f"The value for correspondin key {key} is : {value}")