w = ['월','화','수','목','금','토','일']
for wday in w:
    print(wday)

w = ['금','토','일']
for wday in w:
    print(wday)
else :
    print('주말입니다.')

for i in range(10,5,-1):
    print(i)

for i in range(20,40,2):
    print(i)

x=11
for i in range(5,x):
    print(i)

for i in range(20,40,2):
    print(i)

#소수 확인
a=int(input("please input the number: "))
b=0
for i in range(2,a):
    if a%i==0:
        b==1
        if b==0:
            print(a,"는 소수입니다.")
        else :
            print(a,"는 소수가 아닙니다.")

a=0
while a<=5:
    print(a)
    a+=1

a=0
b=5
while a<5:
    if (b-a)<=0:
        break
    print(b-a)
    a+=1


while(True):
    a=input("프로그램을 종료하시겠습니까?: ")
    if a=="y":
        break

while(True):
    a = input("please input your password: ")
    if a=="orange":
        break
