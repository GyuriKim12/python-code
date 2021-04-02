#구구단
for i in range(1,10):
    for j in range(1,10):
        print(i,'x',j,'=',i*j)

#임의의 정수가 주어지면 순차탐색을 이용하여 오차범위 0.01이내의 제곱근을 구하시오.
#순차탐색을 수행할 때마다 관련 변수들의 상태를 프린트 하시오.
x=int(input('Input number: '))
ans=0
epsilon=0.01
step=0.01
while (abs(ans**2-x)>=epsilon and ans**2<=x):
    print('Current square root is',round(ans,2))
    ans+=step
if abs(ans**2-x)>=epsilon:
    print('Failed on sqaure root of',round(ans,2))
else:
    print(str(x)+"'s"+'square root is', round(ans,2))

#임의의 정수가 주어지면 이진탐색을 이용하여 오차범위 0.01 이내의 제곱근을 구하시오.
#이진탐색을 수행할 때마다 관련 변수들의 상태를 프린트하시오
x=int(input('Input number: '))
epsilon=0.01
low=0
high=max(1.0,x)
x_spart=(low+high)/2.0
while abs(x_spart**2-x)>=epsilon:
    print('low =',str(low)+',','high =',str(high)+',','x_spart =',x_spart)
    if x_spart**2<x:
        low=x_spart
    else:
        high=x_spart
    x_spart=(low+high)/2.0
print(str(x)+'\''+'s','square root is',x_spart)