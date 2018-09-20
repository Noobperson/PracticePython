num1 = int(input('Give me a number: '))
remainder = num1%2

if num1%4==0:
    print('The number is divisible by 4')
elif remainder== 0:
    print('The number is even')
else:
    print('The number is odd')
