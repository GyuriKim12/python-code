#while문으로 변경하라
for i in range(10):
    print(i)

i=0
while i<10:
    print(i)
    i+=1

#출력결과를 순서대로 작성하라
x=4
for i in range(x):
    for j in range(x):
        print(j)
        x=2
#->0
#1
#2
#3
#0
#1
#0
#1
#0
#1

#출력결과를 순서대로 작성하라
x='11011'
y=0
for i in range(len(x)):
    y=y+int(x[i])+3**i
print(y)
#->125 

#별을 출력하시오
for i in range(5,0,-1):
    print('*'*i)

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()

#별을 출력하시오
for i in range(1,5):
    print('*'*i)

for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print()

#n이 정수일 때 소수인지 판별하여 Boolean 타입으로 결과를 출력하는 
# isPrime()함수를 작성하라.
def isPrime():
    n=int(input())
    if n==1:
        return False
    ans=True
    for i in range(2,n):
        if n%i==0:
            ans=False
            break
        else:
            ans=True
    if ans==True:
        return True
    else:
        return False

def isPrime():
    n=int(input())
    if n==1:
        pass
    for i in range(2,n):
        if n%i==0:
            return False
            break
        else:
            return True
isPrime()

#다음 연산식 결과를 작성하라
x=7
y=3
z=5
x+y*Z #->22
x/z**y #->0.056
x//y+y/z #->2.6

#출력결과를 순서대로 작성하라
x=6
for i in range(0,x,1):
    for j in range(i):
        print(j)
#0
#0
#1
#0
#1
#2
#0
#1
#2
#3
#0
#1
#2
#3
#4

#프로그램을 보고 프로그램의 의도를 유추하여 제대로 동작하도록 
#빈칸을 알맞게 채우시오
if x%2==0:
    if x%3==0:
        print(x,'is divisible by 2 and 3')
    else:
        print(x,'is divisible by 2 and not by 3')
elif x%3==0:
    print(x,'is divisible by 3 and not by 2')
else:
    print(x,'is divisible not by 2 and 3')

#n팩토리얼 
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input())
fact(n)

#n에 대한 피보나치수열
def fib(x):
    global numCalls
    numCalls+=1
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)

def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls=0
        print('fib of',i,'=',fib(i))
        print('fib called',numCalls,'times')
n=int(input())
testFib(n)

#palindrome
def isPalindrome1(s):
    def toCharts(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans+=c
        return ans
    def isPal(s):
        print('isPal called with',s)
        if len(s)<=1:
            print('About to return True from base case')
            return True
        else:
            ans=s[0]==s[-1] and isPal(s[1:-1])
            print('About to return',s,'for',ans)
            return ans
    return isPal(toCharts(s))
def testIsPalindrome1():
    print(isPalindrome1('dogGod'))
testIsPalindrome1()

#다음을 while문을 고치시오(break사용 금지)
sum,num=0,1
for i in range(10):
    if int(input())!=1:
        break
    sum+=num
print(sum)

sum,num=0,1
i=0
while i<10 and num==1:
    i+=1
    num=int(input())
    if num==1:
        sum+=num
print(sum)

#다음 코드의 출력값을 서술하시오
cnt,a,n=0,10,10
while a>10:
    b=10
    while b>=0:
        if a+b==n:
            print(a,b)
            cnt+=1
            break
        b-=1
    a-=1
print(cnt)
