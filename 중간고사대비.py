while True:
    x=int(input('x ='))
    if x%2!=0:
        break
while True:
    y=int(input('y ='))
    if y%2!=0:
        break
while True:
    z=int(input('z ='))
    if z%2!=0:
        break
if x>y and y>z:
    print(x,'is the largest odd')
elif y>z:
    print(y,'is the largest odd')
else:
    print(z,'is the largest odd')

numbers=list()
count=0
while count<10:
    s=int(input())
    if s%2!=0:
        numbers.append(s)
        count=0
    else:
        pass
a=numbers[0]
i=0
while i<len(numbers):
    if a<numbers[i]:
        a=numbers[i]
    i+=1
print(a,'is the largest odd')

#소수판별
n=int(input())
i=1
result=True
while Ture:
    if n==1:
        pass
    else:
        if n%i==0:
            result=False
            break
        else:
            result=True
print(result)
        
x=25
ans=0
epsilon=0.01
step=epsilon*2
low=0.0
high=max(1.0,x)
numGuesses=0
while abs(ans**2-x)>=epsilon and ans<=x:
    numGuesses+=1
    ans+=step
print('numGuesses =',numGuesses)
if abs(ans**2-x)>=epsilon:
    print('Failed on square root of',x)
else:
    print(ans,'is close to square root of',x)

x=25
epsilon=0.01
low=0.0
high=max(1.0,x)
ans=(low+high)/2.0
numGuesses=0
while abs(ans**2-x)>=epsilon:
    numGuesses+=1
    print('low =',low,'high =',high,'numGuesses =',numGuesses)
    if ans**2<x:
        low=ans
    else:
        higj=ans
    ans=(low+high)/2.0
print('numGuesses =',numGuesses)
print(ans,'is close to square root of',x)

