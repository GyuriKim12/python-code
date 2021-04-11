#근사 알고리즘을 이용하여 제곱근 구하기
x=25
epsilon=0.01
step=epsilon**2
ans=0
numGuesses=0
while abs(ans**2-x)>=epsilon and ans<=x:
    ans+=step
    numGuesses+=1
print('numGuesses =',numGuesses)
if abs(ans**2-x)>=epsilon:
    print('Failed on square root of',x)
else:
    print(ans,'is close to square root of',x)

#이진탐색을 이용하여 제곱근 구하기
x=25
epsilon=0.01
step=epsilon**2
low=0.0
high=max(1.0,x)
ans=(low+high)/2.0
while abs(ans**2-x)>=epsilon:
    print('low =',low,'high =',high,'ans =',ans)
    numGuesses+=1
    if ans**2<x:
        low=ans
    else:
        high=ans
    ans=(low+high)/2.0
print('numGuesses =',numGuesses)
print(ans,'is close to square root of',x)

#임의의 정수 10개를 가진 리스트 변수를 선언하고 순회하면서, 70점 이상의 점수에는 점수와 함께
#면허증 발급 결정을 출력하고 그 이외에는 점수와 함께 면허증 발급 취소를 출력하는 프로그램을 작성하시오.
numbers=[10,46,78,89,61,45,36,98,80,65]
i=0
while i<10:
    if numbers[i]>=70:
        print(numbers[i],'면허증 발급이 결정되었습니다')
    else:
        print(numbers[i],'면허증 발급이 취소되었습니다.')
    i+=1

#실습문제(1)에서 임의의 정수 10개를 가진 리스트 대신, 사용자로부터 정수를 입력 받아 
#리스트에 담을 수 있도록 프로그램을 리팩토링하시오. 단, 사용자로부터 입력 받은 정수는 EOF라는 문자열을 
#입력받기 전까지만 입력 받으시오.
numbers=list()
while True:
    s=input('Input an integer: ')
    if s=='EOF':
        break
    numbers.append(int(s))
for i in range(len(numbers)):
    if numbers[i]>=70:
        print(numbers[i],'면허증 발급이 결정되었습니다')
    else:
        print(numbers[i],'면허증 발급이 취소되었습니다.')
    i+=1

#for 반복문을 이용하여 1단부터 9단까지의 구구단을 출력하시오.
for i in range(1,10):
    for j in range(1,10):
        print(i,'x',j,'=',i*j)

#임의의 정수가 주어지면 순차탐색을 이용하여 오차범위 0.01이내의 제곱근을 구하시오.
#순차탐색을 수행할 때마다 관련 변수들의 상태를 프린트하시오.
x=int(input('Input number: '))
ans=0
epsilon=0.01
while abs(ans**2-x)>=epsilon and ans**2<=x:
    print('Current square root is',round(ans,2))
    ans+=epsilon
if abs(ans**2-x)>=epsilon:
    print('Failed on square root of',round(ans,2))
else:
    print(str(x)+"'s",'square root is',ans)

#임의의 정수가 주어지면 이진탐색을 이용하여 오차범위 0.01이내의 제곱근을 구하시오.
#이진탐색을 수행할 때마다 관련 변수들의 상태를 프린트하시오
x=int(input('Input number: '))
epsilon=0.01
low=0
high=max(1.0,x)
x_sqrt=(low+high)/2.0

while abs(x_sqrt**2-x)>=epsilon:
    print('low =',low,'high =',high,'x_sqrt =',x_sqrt)
    if x_sqrt**2<x:
        low=x_sqrt
    else:
        high=x_sqrt
    x_sqrt=(low+high)/2.0
print(str(x)+"'s",'square root is',x_sqrt)