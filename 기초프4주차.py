string=input('input a string: ')
length=len(string)
check1=False
check2=False
s=0
p=0
for i in range(len(string)):
    if check1==False and string[i]=='a':
        s=i+1
        check1=True
    if check2==False and string[i]=='z':
        p=i
        check2=True
print(string[s:p])