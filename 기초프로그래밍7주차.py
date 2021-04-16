#n팩토리얼
def fact():
    n=int(input())
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
#palindrome
def isPalindrome1(s):
    def toCharts(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans+=c
        return ans
    def isPal(s):
        print('isPal called with',s)
        if len(s)<=1:
            print('About to return True from base case')
            return True
        else:
            ans=s[0]==s[-1] and isPal(s[1:-1])
            print('About to return',ans,'for',s)
            return ans
    return isPal(toCharts(s))
def testIsPalindrome1():
    print(isPalindrome1('dogGod'))
testIsPalindrome1()

#피보나치 수열
def fib(x):
    global numCalls
    numCalls+=1
    if x==0 or x==1:
        return 1
    else:
        return fib(x-1)+fib(x-2)
def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls=0
        print('fib of',i,'=',fib(i))
        print('fib called',numCalls,'times')
n=int(input())
testFib(n)