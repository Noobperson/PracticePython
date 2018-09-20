import random
n= int(input('how many numbers do you want to generate for each list? '))

a= []
b= []
while n != 0:
    n-= 1
    a.append(random.randint(1,1000))
    b.append(random.randint(1,1000))
else:
    print('list a: ' + str(a))
    print('list b: ' + str(b))

c= []
for x in a:
    for y in b:
        if x==y:
            c.append(x)
print('Common Numbers: ' + str(c))
