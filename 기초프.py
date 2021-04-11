def my_plus(x,y):
    return x+y

def my_minus(x,y):
    return x-y

def my_multiply(x,y):
    return x*y

def my_division(x,y):
    return x/y

def my_calculate(x,y,Op):
    if Op=="-":
        return my_miuus(x,y)
    elif Op=="*":
        return my_multiply(x,y)
    elif Op=="/":
        return my_division(x,y)
    else:
        return my_plus(x,y)

def isInt(x):
    for i in x:
        if i not in "0123456789":
            result=False
        else:
            result=True
    return result

def InputInt(s):
    while (True):
        x=input("Enter an integer: ")
        result=isInt(x)
        if result==True:
            break
        else:
            print("Wrong integer! Input the",s,"integer again!")
    return int(x)

def isOp(x):
    if x in "+-*/":
        result=True
    else:
        result=False
    return result

def InputOp():
    while (True):
        x=input("Enter an operation: ")
        result=isOp(x)
        if result==True:
            break
        else:
            print("Wrong operation! Input the operation again!")
    return x

x=InputInt("first")
y=InputInt("second")
Op=InputOp()
print(str(x)+Op+str(y),"is",my_calculate(x,y,Op))