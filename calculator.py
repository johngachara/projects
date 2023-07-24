def main():
    print('Welcome to my calculator')
    print('Choose the type of calculation you would like to perfom')
    operations=['Addition','Subtraction','Multiplication','Division','Average']
    for element in enumerate(operations):
        print(element)
main()
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    return x/y
def average(x,y):
    return x+y/2
def operation():
    choice=int(input('Choose operation(0-4) '))
    if choice==0:
        numone=int(input('Enter first number: '))
        numtwo=int(input('Enter second number: '))
        result=add(numone,numtwo)
        print('The answer is',result)
    if choice==1:
        numone = int(input('Enter first number: '))
        numtwo = int(input('Enter second number: '))
        result = subtract(numone,numtwo)
        print('The answer is', result)
    if choice==2:
        numone = int(input('Enter first number: '))
        numtwo = int(input('Enter second number: '))
        result = multiply(numone, numtwo)
        print('The answer is', result)
    if choice==3:
        numone = int(input('Enter first number: '))
        numtwo = int(input('Enter second number: '))
        result = division(numone, numtwo)
        print('The answer is', result)
    if choice==4:
        numone = int(input('Enter first number: '))
        numtwo = int(input('Enter second number: '))
        result = average(numone, numtwo)
        print('The answer is', result)
    if choice>4:
        print('Wrong input')
operation()
def calcagain():
    print('Would you like to perfom another calculation?')
    print('1. Yes')
    print('2. No')
    second=int(input())
    if second==1:
        main()
        operation()
    if second==2:
        print('Happy calculating')
calcagain()
main()
operation()