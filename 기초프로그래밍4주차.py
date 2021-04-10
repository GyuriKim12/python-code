#PI변수를 3.14로 초기화하고, 원의 반지름 값에 따라 원의 넓이를 출력하는 프로그램을 만드시오. 
#단, 입력 반지름의 0이하라면 'Wrong input!'를 출력,
#원의 넓이가 50이상이면 'Very big circle!'을 출력하고, 50미만이면 'Normal circle!'을 출력하시오.
PI=3.14
radius=int(input('Input an integer radius: '))
area=PI*(radius**2)
if radius<0:
    print('Wrong input!')
if area>=50:
    print('Very big circle')
else:
    print('Normal circle!')

#Read 2numbers and print the smaller one
x=int(input('첫 번째 숫자를 입력하시오 : '))
y=int(input(('두 번째 숫자를 입력하시오 : '))
print('입력한 두 수 중 더 작은 수 : ')
if x>y:
    print(y)
elif x<y:
    print(x)
else:
    print('두 수는 같습니다.')

#x의 제곱근을 구하시오
x=int(input('숫자를 입력하시오 : '))
ans=0
itersLeft=x
while itersLeft!=0:
    ans+=x
    itersLeft-=1
    print('ans =',ans)
print('결과값 :',ans)
print('itersLeft =',itersLeft)

#11과 12의 최소공배수
##1
x=1
while True:
    if x%11==0 and x%12==0:
        break
    x+=1
print(x,'is divisible by 11 and 12')

##2
x=1
while x%11!=0 or x%12!=0:
    x+=1
print(x,'is divisible by 11 and 12')

#사용자가 입력한 문자열을 모든 문자가 출력될 때까지 한 글자씩 출력하는 프로그램을 만드시오.
##1
korean_str=input('문자열을 입력하시오 : ')
str_len=len(korean_str)
i=0
while str_len>0:
    print(str_len[i:i+1])
    i+=1
    str_len-=1

##2
korean_str=input('문자열을 입력하시오 : ')
for val in korean_str:
    print(val)

##3
korean_str=input('문자열을 입력하시오 : ')
str_len=len(korean_str)
i=0
while i<str_len:
    print(korean_str[i:i+1])
    i+=1

#프로그램 사용자로부터 임의의 문자열을 입력 받고, 입력 받은 문자열의 길이를 출력하시오.
#또한, 입력 받은 문자열 중 영문 소문자의 개수를 세어 출력하시오.
##1
str_=input('Input a string: ')
length=len(str_)
print('Length of input string:',length)
i=0
count=0
while i<length:
    if str_[i]>='a' and str_[i]<='z':
        count+=1
    i+=1
print('The number of lower letters are:',count)

##2
str_=input('Input a string: ')
length=len(str_)
print('Length of input string:',length)
count=0
for i in range(len(str_)):
    if str_[i].islower()==True:
        count+=1
    i+=1
print('The number of lower letters are:',count)

##3
str_=input('Input a string: ')
length=len(str_)
print('Length of input string:',length)
i=0
count=0
while i<length:
    if str_[i].islower()==True:
        count+=1
    i+=1
print('The number of lower letters are:',count)

#프로그램 사용자로부터 3개의 문자열을 입력 받고, 이를 모두 합쳐 하나의 문자열로 출력하는
#프로그램을 작성하시오.
str1=input('Input 1st string: ')
str2=input('Input 2nd string: ')
str3=input('Input 3rd string: ')
print('The merged string:',str1+' '+str2+' '+str3)

#프로그램 사용자로부터 문자열을 입력 받고, 영문 소문자'a'가 처음 등장하는 곳 다음부터  
#'z'가 등장하기 전까지의 문자열만 필터링하여 출력하시오.
#단,'a'는 반드시 'z'전에 입력되어야 하며, 'a'와 'z'는 문자열 중에 반드시 포함되어야 한다.
##1
str_=input('Input a string: ')
length=len(str_)
i=0
j=0
while i<length:
    if str_[i]=='a': 
        break
    i+=1
while j<length:
    if str_[j]=='z':
        break
    j+=1
print('The result is:',str_[i+1:j])

##2
str_=input('Input a string: ')
length=len(str_)
i=0
j=0
result=True
for i in range(len(str_)):
    if str_[i]=='a':
        result==False
        break
    i+=1
    for j in range(len(str_)):
        if str_[j]=='z':
            break
        j+=1
print(str_[i+1:j])