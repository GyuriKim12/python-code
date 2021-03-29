#세제곱근 구하기
#while문 이용하기
x=int(input('Enter an integer: '))
ans=0
while ans**3<abs(x):
    ans+=1
if ans**3!=abs(x):
    print(x,'is not a perfect cube.')
else:
    print('Cube root of',x,'is',ans)

#for문 사용하기
x=int(input('Enter an integer: '))
ans=0
for i in range(0,abs(x)+1):
    if ans**3>=abs(x):
        break
if ans**3!=abs(x):
    print(x,'is not a perfect cube.')
else:
    print('Cube root of',x,'is',ans)

x=4
for i in range(x):
    for j in range(x):
        print(j)

x=4
for i in range(x):
    for j in range(x):
        print(i,j)
        x=2

#제곱근 구하기
#논리 알고리즘
x=int(input('Enter an integer: '))
epsilon=0.01
step=epsilon**2
ans=0.0
numGuesses=0
while (abs(ans**2-x)>=epsilon and ans<=x):
    ans+=step
    numGuesses+=1
print('numGuesses=',numGuesses)
if abs(ans**2-x)>=epsilon:
    print('Failed on square root of',x)
else:
    print(ans,'is close to square root of',x)

#이진탐색
x=int(input('Enter an integer: '))
low=0.0
high=max(1.0,x)
ans=(low+high)/2.0
numGuesses=0
while abs(ans**2-x)>=epsilon:
    print('low=',low,'high=',high,'ans',ans)
    numGuesses+=1
    if ans**2<x:
        low=ans
    else:
        high=ans
    ans=(low+high)/2.0
print('numGuesses=',numGuesses)
print(ans,'is close to square root of',x)

#임의의 정수 10개를 가진 리스트 변수를 선언하고 순회 하면서, 70점 이상의 점수에는 점수와 함께
#면허증 발급 결정을 출력하고 
# 그 외에는 점수와 함께 면허증 발급 취소를 출력하는 프로그램을 작성하시오
scores=[10,70,30,35,68,89,95,100,56,75]
for score in scores:
    if score>=70:
        print('The score is'+str(score)+',so no dirber license!')
    else:
        print('The score is'+str(score)+',so issued driver license')

#1번과 다르게 사용자로부터 정수를 입력 받아 리스트에 담을 수 있도록 프로그램을 리팩토링하시오.
#단, 사용자로부터 입력받는 정수는 EOF라는 문자열을 입력 받기 전까지만 입력 받으시오.
#(hint: 리스트 객체 numbers.append()활용. while(1)문에서 빠져나가는 방법은 break)
scores=[]
while (1):
    temp=input('Input an integer: ')
    if (temp=='EOF'):
        numbers.append(int(tempt))
    else:
        break
for score in scores:
    if score>=70:
        print('The score is'+str(score)+',so no dirber license!')
    else:
        print('The score is'+str(score)+',so issued driver license')