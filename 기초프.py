x=int(input('Input number: '))
epsilon = 0.01
low = 0
high = max(1.0,x)
x_squrt = (high + low)/2.0
while abs(x_squrt**2 - x) >= epsilon: 
    x_squrt = (high + low)/2.0
    print('low =', str(low)+',', 'high =', str(high)+',', 'x_squrt =', x_squrt)
    if x_squrt**2 < x:
        low = x_squrt 
    else:
        high = x_squrt 

sum=0
for i in range(3):
    x=int(input('Input an integer: '))
    sum+=x
print(sum)
