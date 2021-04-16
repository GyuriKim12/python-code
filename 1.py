a = [1,2,3,['a','b','c']]
print(a[0])
print(a[-1])
print(a[-1][2])

a = 'hobby'
print(a.count('b')) #b가 몇번 나오는지

a = 'python is the best choice.'
print(a.find('b')) #b가 문자열 중 어디에 있는지
print(a.find('k')) #k가 없으면 -1나옴

a = 'Life is too short'
print(a.index('t')) # 없는 것을 넣으면 에러나옴

a = '.'.join('abcd')
print(a)


a,b = input('숫자 2개를 입력하세요: ').split() #공백을 기준으로 할당
print(a)
print(b)


sum,num=0,1
i=0
while i<10:
    i+=1
    n=int(input())
    while n==1:
        if n==1:
            sum+=num
print(sum)