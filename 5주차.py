x=int(input('Input number: '))
ans=0
epsilon=0.01
step=epsilon**2
numGuesses=0
while (abs(ans**2-x)>=epsilon and ans<=x):
    ans+=step
    print('Current square root is',ans)
print(str(x)+'\''+'s'+' square root is', ans)