#Reading the whole book at once
with open('46-0.txt', 'r') as book_file:
     text = book_file.read()
print(text)


#Reading the book line by line
with open('46-0.txt', 'r') as book_file:
    for line in book_file.readlines():
        print(line)