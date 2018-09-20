a = []
a.append(int(input('Give me a number: ')))
a.append(int(input('Give me another number: ')))
print('currently in list: ' + str(a))

request= input('Do you want to add more numbers? [y/n] ')

while request=='y':
    if request =='y':
        a.append(int(input('Give me a number: ')))
        a.append(int(input('Give me another number: ')))
        request= input('Do you want to 2 more numbers? [y/n] ')
        print('currently in list: ' + str(a))
    else:
        print('Thank you for inputting these numbers, lets continue...')

Less_than= int(input('Give me a number, and i will give you the numbers in the list that is less than that. Number= '))
b=[]
for element in a:
    if int(element)<int(Less_than):
        b.append(element)


print(b)
