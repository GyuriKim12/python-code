def isInt(x):
    result=True
    for i in x:
        if x in "0123456789":
            result=False
        else:
            result=True
            break
    return result

def InputInt(s):
    while True:
        x=input('Enter an integer: ')
        ans=isInt(x)
        if ans==True:
            break
        else:
            print('Wrong integer! Input the',s,'integer again!')
        return int(x)

def 