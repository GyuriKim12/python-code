#1
string=input('input a string: ')
length=len(string)
check1=False
check2=False
s=0
p=0
i=0
for i in range(length):
    if (check1==False and siring[i]=='a'):
        s=i+1
        check1=True
    if (check2==False and string[i]=='z'):
        p=i
        check2=True
print(s:p)
            
#2
string=input('input a string: ')
length=len(string)
i=0
j=0
while i<length:
    if string[i]=='a':
        break
    i+=1
while j<length:
    if string[j]==z
        break
    j+=1        
print(string[i+1:j])