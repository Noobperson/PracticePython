num1 = int(input('Give me a number: '))
x = range(1, num1)
b=[]
for element in x:
    if num1 % element == 0:
        b.append(element)
print('This number is divisible by' + str(b))
