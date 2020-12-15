print('Hello World!')

number = 2
print(number)

# calculate the area of a cirle
pi = 3.14
r = 4
area = pi * r * r

print (area)

# Lists: are ordered collections of elements
l = [2, 3, 4, 5]
print(l)
print(f'The first element of t he list is {l[0]}')
print (l[:2]) #slicing
print (l[2:]) #slicing
print (l[-2])

list2 = ['Alexander', 'TA7', 'AAU']
list3 = [3, 'TechnoAnthroProblems', 3.14, 'Goat'] #it is not recommended to have different data types in the same list
for element in list3:
    print(element)

#Making pizza

ingredients = ['pepperoni', 'goat cheese', 'ruccola', 'oregano']
for ingredient in ingredients:
    print(ingredient)
    #removing an element from the list
ingredients.remove('goat cheese')
print(ingredients)

nr_elements = len(ingredients)
print(f'There are {nr_elements} ingredients in the list of pizza ingredients')

#Doing something fancy with the strings
print(ingredients[0])
print(ingredients[0].title())
print(ingredients[0].upper())
print(ingredients[0].lower())

#adding something to the list, using append method
ingredients.append('salami')
ingredients.append('horse radish')
ingredients.append('tomato sauce')
print(ingredients)

print (range(5))
for i in range (5):
    print (i)

numbers = list(range (10))
print(numbers)
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# if conditions
age = 25
if age >= 18:
    print('You can buy beer')
else:
    print('You are not allowed to buy alcohol - Wait until you are old enough')

# restriction on persons not in a given list
authorized_persons = ['Henning', 'John', 'Frank']
name = 'jens' #defines what name is used in this case
if name in authorized_persons:
    print('You are authorized to proceed')
else:
    print('Restriction on your name. Please contact Marcus to get authorization.')

