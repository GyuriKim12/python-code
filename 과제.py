numbers=list()
def isInt():
    count=0
    for i in s:
        count+=1
        if i in "0123456789":
            result='positive'
        elif '-' in x:
            if '0123456789' in s[1:] and count==0:
                break
            elif '0123456789' in s[1:] and count!=0:
                result='negative' 
            else:
                result='wrong'
        else:
            result='wrong'
    return result   
    
def InputInt():
    while (True):
        s=input("양정수를 입력하시오: ")
        result=isInt(s)
        if result=='positive':
            numbers.append(int())
        elif result=='negative':
            break
        else:
            print('잘못 입력하였습니다. 다시입력하십시오')
InputInt()

def my_max():
    while True:
        if len(numbers)==0:
            pass
        else:
            i=0
            a=numbers[0]
            while i<len(numbers):
                if a<numbers[i]:
                    a=numbers[i]
                i+=1
            return a
print('최대값은',my_max())

def my_min():
    while True:
        if len(numbers)==0:
            pass
        else:
            i=0
            a=numbers[0]
            while i<len(numbers):
                if a>numbers[i]:
                    a=numbers[i]
                i+=1
            return a
print('최소값은',my_min())

def my_sum():
    while True:
        if len(numbers)==0:
            pass
        else:
            i=0
            sum=0
            while i<len(numbers):
                sum+=numbers[i]
                i+=1
            return sum
print('합은',my_sum())

def my_avg():
    while True:
        if len(numbers)==0:
            pass
        else:
            i=0
            sum=0
            while i<len(numbers):
                sum+=numbers[i]
                i+=1
            result=sum/len(numbers)
            return result
print('평균은',my_avg())