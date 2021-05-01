#1
count=int(input('학생의 수를 입력하세요: '))
numbers=list()
while count>0:
    s=input('성적을 입력하세요: ')
    numbers.append(int(s))
    count-=1
    
i=0
sum=0
while i<len(numbers):
    sum+=numbers[i]
    i+=1
result=sum/len(numbers)
print('성적 평균은',result,'입니다.')

i=0
a=numbers[0]
while i<len(numbers):
    if a<numbers[i]:
        a=numbers[i]
    i+=1
print('가장 높은 점수는',a,'입니다.')

i=0
a=numbers[i]
while i<len(numbers):
    if a>numbers[i]:
        a=numbers[i]
    i+=1
print('가장 낮은 점수는',a,'입니다.')

#2번 method1
Tuple=(10,20,30,40)
count=5
numbers=[]
while count>0:
    x=input('숫자를 입력해 주세요: ')
    numbers.append(int(x))
    count-=1

List=[]   
def merge(List):
    i=0
    while i<len(Tuple):
        List.append(int(Tuple[i]))
        i+=1
    List+=numbers
    return List

def listSort(x):
    for i in range(len(x)):
        k=len(x)-i
        for j in range (1,k):
            temp=x[0]
            if x[j-1]>x[j]:
                temp=x[j-1]
                x[j-1]=x[j]
                x[j]=temp
    return x

x=listSort(numbers)
print('tupel과 list를 합친 결과',listSort(merge(List)))  
print('내 list 정렬 값',listSort(x))

#method2
Tuple=(10,20,30,40)
count=5
numbers=[]
while count>0:
    x=input('숫자를 입력해 주세요: ')
    numbers.append(int(x))
    count-=1

def merge():
    add=numbers[:]
    for i in Tuple:
        add.append(i)
    return add
merge()

def listSort(x):
    for i in range(1,len(x)):
        j=i
        while j>0 and x[j-1]>x[j]:
            x[j-1],x[j]=x[j],x[j-1]
            j-=1   
    return x

x=listSort(numbers)
print('tupel과 list를 합친 결과',listSort(merge()))  
print('내 list 정렬 값',listSort(x))