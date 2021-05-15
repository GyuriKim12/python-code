#1번
import collections
Student=collections.namedtuple("Student","name,stdId,grade")

def isInt(n):
    ans=True
    for i in n:
        if i in "0123456789":
            ans=True
        else:
            ans=False
    return ans

def isLetters(n):
    ans=True
    for i in n:
        if n in ",<.>/?~`!@#$%^&*()_+=-1234567890":
            ans=False
        else:
            ans=True
    return ans

while True:
    cnt=input("Input loop count: ")
    if isInt(cnt)==True:
        cnt1=int(cnt)
        break
    else:
        print('Wrong Input! please input again')
        
def isName():
    while True:
        name=input("Input name: ")
        if isLetters(name)==True:
            name1=name
            break
        else:
            print("Wrong input! please input again")
    return name1
    
def isStdId():
    while True:
        stdId=input("Input student id: ")
        if isInt(stdId)==True and len(stdId)==8:
            stdId1=int(stdId)
            break
        else:
            print("Wrong input! please input again")
    return stdId1
    
def isGrade():
    while True:
        grade=input("input grade: ")
        if isInt(grade)==True and grade!="0" and len(grade)==1:
            grade1=int(grade)
            break
        else:
            print("Wrong input! please input again")
    return grade1
    
List=[]
for i in range(cnt1):
    print("--------------------")
    std=Student(name=isName(),stdId=isStdId(),grade=isGrade())
    List.append(std)

def isOperator(List):
    import operator
    List=sorted(List,key=operator.attrgetter("name"))
    print(List)
isOperator(List)

#2번
def getDiscriminant(a, b, c):
    if b%2==0:
        return ((b/2) ** 2) - (a*c)
    else:
        return (b ** 2) - (4*a*c)

def getQuadraticFormula(a, b, c):
    QF = None
    D=0
    if a == 0:
        if b == 0:
            # Answer is infinity
            if c == 0:
                QF = True

            # Answer is none
            else:
                QF = False

        # Answer is one real root
        else:
            QF = c / (-b)

    else:
        D = getDiscriminant(a, b, c)

    # Answer are two real root
    if a!=0 and b!=0:
        if D > 0:
            if b%2==0:
                QF = (
                    (-b/2 + D ** 0.5) / (a),
                    (-b/2 - D ** 0.5) / (a))
            else:
                QF = (
                    (-b + D ** 0.5) / (2 * a),
                    (-b - D ** 0.5) / (2 * a))

    # Answer are two imaginary root
        elif D < 0:
            QF = (
                complex((-b) / (2 * a), (-D) ** 0.5 / (2 * a)),
                complex((-b) / (2 * a), - ((-D) ** 0.5) / (2 * a)))

    # Answer is multiple root
        else:
            QF = (-b) / (2 * a)

    return QF

print("Calculate QF(Quadratic Formula) for PSE(Perfect Square Expression)")
print("ex) ax^2 + bx + c = 0")

a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))
QF = getQuadraticFormula(a, b, c)

print("Calculated answer is(are):")

if QF == True:
    print("Infinity.")

elif QF == False:
    print("None.")

elif isinstance(QF, tuple):
    for answer in QF:
        print("{:.2f}".format(answer))

else:
    print("{:.2f}".format(QF))