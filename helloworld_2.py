print('Hello World!')

number = 2
print(number)

# calculate the area of a cirle
pi = 3.14
r = 4
area = pi * r * r
print(f'The area of the circle with radius {r}cm {area}cm**2')
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
nr_elements = len(ingredients)
print(f'there are {nr_elements} ingredients in the list of pizza making ')
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
age = 16
if age >= 18:
    print('You can buy beer')
elif age >= 14 and age < 18:
    print('You can only buy light-alcohol, given you are a minor. Please wait until you are 18 to buy strong alcohol')
else:
    print('You are not allowed to buy alcohol - Wait until you are old enough')

# restriction on persons not in a given list
authorized_persons = ['Henning', 'John', 'Frank']
name = 'jens' #defines what name is used in this case
if name in authorized_persons: #loops through the authorized.persons list
    print('You are authorized to proceed')
else:
    print('Restriction on your name. Please contact Marcus to get authorization.')

#Dictionaries (Maps in Java)
book = {
    'title': 'Alice in Wonderland',
    'author': 'Henning Mankell',
    'year': 1930,
    'language': 'English'
}

phonebook = {
    'Alexander': {'Home': 33, 'Work': 55},
    'Mussi': {'Home': 64,},
    'Lad1': {'Mobile':1525}

}
print([phonebook])
print(phonebook['Alexander']['Work'])


print('')
print('')


print(book)
print(book['title'])
print(book['author'])
book['year']=1950
print(book)

print(book.keys())
print(book.values())
print(book.items())

books =[]
books.append(book)
print(books)

print()
print()

#Functions
def sum(a,b,c):
    return  a + b + c
s = sum(3,4,5)
print(s)

def circle_area(r):
    area: 3.14 * r * r
    return area

n1 = input('Insert a number: ')
n2 = input('Insert a second number: ')
n3 = input('Insert a third number: ')
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
print(f'the sum of your numbers is: {sum(n1,n2, n3)}')

#Read numbers until user inputs -1
print()
user_input = 0
while user_input != -1:
    user_input = input('Insert your options: 0 for printing the list of books \n'
                       ' 0 for printing the list of books \n'
                       '...\n'
                       '-1 to quit\n')
    user_input = int(user_input)
    #based on  the user input value I do some actions
    if user_input == 0:
        #I will need to print the list of books
        print('I am printing the list of books...')
    # TODO
    elif user_input == 1:
        print('This is the first book in your list:')
    #TODO


#How to read files

with open('11.txt', 'r') as book_file:
    text =
