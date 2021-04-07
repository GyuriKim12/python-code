#Read 3 numbers and print the sum
#for문 사용
sum=0
for i in range(3):
    x=int(input('원하는 숫자를 입력하세요 : '))
    print(x)
    sum+=x
print('입력한 숫자들의 합 :')
print(sum)

#while문 사용
sum=0
count=0
while count<3:
    x=int(input('원하는 숫자를 입력하세요 : '))
    sum+=x
    print(x)
    count+=1
print('입력한 숫자들의 합 :') 
print(sum)

#Read 2 numbers and add them
#input 넣기
a=int(input('첫 번째 숫자를 입력하시오 : '))
b=int(input('두 번째 숫자를 입력하시오 : '))
print('입력한 두 수의 합: ')
print(a+b)

#for문 사용
sum=0
for i in range(2):
    x=int(input('숫자를 입력하시오 :'))
    sum+=x
print('입력한 두 수의 합: ')
print(sum)

#while문 사용
sum=0
count=0
while count<2:
    x=int(input('숫자를 입력하시오 :'))
    sum+=x
    count+=1
print('입력한 두 수의 합: ')
print(sum)

#과제
your_name=print(input('Input your first name: '))
birth_year=print(input('Input your birth year: '))
this_year=print(input('Input your this yea'))