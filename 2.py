a = [1,2,3,['a','b','c']]
print(a[1])
print(a[-1])
print(a[3][-2])

a = [1.3,2.5,3.9,4.1]
a = list(map(int,a))
print(a)

a = input("숫자 2개를 입력하시오: ").split()
print(a)

print("안녕하세요\n저는 김규리 입니다.")
print("안녕하세요\r저는 김규리 입니다.") 
print("\"안녕하세요 저는 김규리 입니다.\"")
print("\'안녕하세요 저는 김규리 입니다.\'")

for i in range(5):
    print(i)

a = "i wanna go to house"
print(a.count('a'))
print(a.find('a'))
print(a.index('a'))

a = '.'.join('abcd')
print(a)

print(list(range(10)))

i = 5
while i>3:
    print('i= ', i)
    i= i-1

str1 = 'hellow'
for val in str1:
    print(val, str1)

x=4
for i in range(0,x):
    print(i)
    x=5

x=4
for i in range(2,x):
    print(i)

x=5
for i in range(x):
    for i in range(x):
        print(i)
    x=3

a = ['apple','lemon','orange','cherry']
for val in a:
    print(val,len(val))