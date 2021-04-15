#kyeword argument 
#not legal to follow a keyword argument with a non-keyword argument
def printName(firstName,lastName,reverse):
    if reverse:
        print(lastName+', '+firstName)
    else:
        print(firstName,lastName)
printName('Olga','Puchmajerova',True)
printName('Olga','Puchmajerova',False)
printName('Olga','Puchmajerova',reverse=False)
printName('Olga',lastName='Puchmajerova',reverse=False)

#default parameter values
def printName(firstName,lastName,reverse=False):
    if reverse:
        print(lastName+', '+firstName)
    else:
        print(firstName,lastName)
printName('Olga','Puchmajerova')
printName('Olga','Puchmajerova',True)
printName('Olga','Puchmajerova',reverse=True)
printName('Olga','Puchmajerova',False)

#2개의 number중에 작은 값을 return하는 함수를 작성하시오
def printSmaller():
    x=int(input())
    y=int(input())
    if x>y:
        return y
    else:
        return x
printSmaller()

#scoping
def f(x):
    y=1
    x+=y
    print('x =',x)
    return x

x=3
y=2
z=f(x)
print('z =',z)
print('x =',x)
print('y =',y)

#제곱근 구하기
def findRoot(x,power,epsilon):
    if x<0 and power%2==0:
        return None
    low=0.0
    high=max(1.0,x)
    ans=(low+high)/2.0
    while abs(ans**2-x)>=epsilon:
        if ans**power<x:
            low=ans
        else:
            high=ans
        ans=(low+high)/2.0
    return ans
x=int(input())
power=int(input())
epsilon=float(input())
print(findRoot(x,power,epsilon))

#두 개의 숫자를 입력 받으면 두 수를 더하여 반환하는 함수 my_plus 함수를 정의하시오
def my_plus():
    print('Input two numbers :')
    x=int(input())
    y=int(input())
    result=x+y
    return result
print('Result is',result)

#두 개의 숫자를 입력 받으면 두 수를 뺴고, 곱하고, 나누는 함수 my_minus, my_multiply, my_division
#함수를 정의하시오
def my_plus():
    return x+y
def my_minus():
    return x-y
def my_multiply():
    return x*y
def my_division():
    return x/y
print('Input two numbers: ')
x=int(input())
y=int(input())
print('Plus result is',my_plus())
print('Minus result is',my_minus())
print('Multiply result is',my_multiply())
print('Division result is',my_division())

#두 개의 숫자와 +,-,*,/ 기호 중 하나를 입력 받으면 입력 받은 기호에 따라 앞에서 선언한 
#my_plus, my_minus 등의 함수를 적적히 사용하여 연산을 수행할 수 있도록 돕는
# my_calculate 함수를 선언하시오
def my_plus():
    return x+y
def my_minus():
    return x-y
def my_multiply():
    return x*y
def my_division():
    return x/y 

def my_calculate(x,y,op):
    if op=='+':
        return my_plus()
    elif op=='-':
        return my_minus()
    elif op=='*':
        return my_multiply()
    else:
        return my_division()
print('Input two numbers: ')
x=int(input())
y=int(input())
op=(input('Input operation: '))
print('Result is',my_calculate(x,y,op))

#두 개의 정수를 입력 받을 때, 사용자의 잘못된 input을 다음의 예시와 같이 찾아내어,
#사용자에게 재 input을 받도록 하는 isInt()와 InputInt()함수와
#하나의 연산자를 입력 받을 때, 사용자의 잘못된 input()을 다음의 예시와 같이 찾아내어,
#사용자에게 재 input을 받도록 하는 isOp()와 InputOp()함수를 프로그래밍 하시오
def my_plus():
    return x+y
def my_minus():
    return x-y
def my_multiply():
    return x*y
def my_division():
    return x/y 

def my_calculate(x,y,Op):
    if Op=='+':
        return my_plus()
    elif Op=='-':
        return my_minus()
    elif Op=='*':
        return my_multiply()
    else:
        return my_division()

def isInt(x):
    result=True
    for i in x:
        if i not in '0123456789':
            result=False
        else:
            result=True
    return result

def InputInt(s):
    while True:
        s=input('Enter an integer: ')
        result=isInt(x)
        if result==True:
            break
        else:
            print('Wrong integer! Input the',s,'integer again!')
    return x

def isOp(x):
    if x in '+-*/':
        result=True
    else:
        result=False
    return result

def InputOp():
    result=isop()
    while True:
        if result==Ture:
            break
        else:
            print('Wrong operation! Input the operation again!')
    return x

x=InputInt('first')
y=InputInt('second')
Op=InputOp()
print(str(x)+op+str(y),'is',my_calculate(x,y,Op))