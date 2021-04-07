def printName(firstName,lastName,reverse):
    if reverse:
        print(lastName+', '+firstName)
    else:
        print(firstName,lastName)
printName('Olga','Puchmajer ova',True)
printName('Olga','Puchmajerova',False)
printName('Olga','Puchmajerova',reverse=False)
printName('Olga',lastName='Puchmajerova',reverse=False) 

def printName(firstName,lastName,reverse=False):
    if reverse:
        print(lastName+', '+firstName)
    else:
        print(firstName,lastName)
printName('Olga','Puchmajerova')
printName('Olga','Puchmajerova',True)
printName('Olga','Puchmajerova',reverse=True)

def min():
    if a<b:
        return a
    else:
        return b
a,b=map(int,input('Input two integer: ').split())
min()
