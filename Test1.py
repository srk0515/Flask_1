

fruits=['apples','oranges','banana','grapes']
vege=['potato' ,'carrot']
print(fruits)
print(len(fruits))
print(fruits[3])

#negative index to come from reverse
print(fruits[-4])

#select index
print(fruits[0:3])

print(fruits[2:])

#add to end of list
fruits.append('pineapple')

#add to a position
fruits.insert(1,'mango')
print(fruits)

#add another list
fruits.extend(vege)
print(fruits)

#remove values from list
fruits.pop()
print(fruits)

#reverse order
fruits.reverse()
print(fruits)

#sort a list
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

#sorted function used to not alter orgonal list
sorted_fruit=sorted(fruits)
print(sorted_fruit)

numbs=[1, 2, 3, 4]
print(sum(numbs))

#get index
print(fruits.index('mango'))

#in
print('apples' in fruits)

for item in fruits:
    print(item)

for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(index,fruit)

#concatenate

fruit_str=',' .join(fruits)
print(fruit_str)

new_fruit= fruit_str.split(',')
print(new_fruit)

#tuple -immutable

tuple_1=(1,2,3,4)

#Sets
set1={'car','bike','truck','train','car'}
print(set1)
print('car' in set1)

set2={'bike' ,'spaceship' ,'train'}
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))

empty_list1={}
empty_list=list()

empty_set=set()
empty_tuple=tuple()

#dict

student={'name':'Jason','age':'20','courses':['math','science']}
print(student)
print(student['name'])
print(student['age'])
print(student['courses'])

print(student.get('name'))

student['phone']='610-952-5555'
print(student)
student['name']='jane'
print(student)

student.update({'name':'Queen','phone':'5555'})
print(student)

del(student['age'])
print(student)

phone=student.pop('phone')
print(student)
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

for key in student:
    print(key)
for key,value in student.items():
    print(key,value)