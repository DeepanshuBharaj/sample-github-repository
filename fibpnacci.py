class Solution:
    def fib(self,n:int)->int:
        if n == 0 or n == 1:
            return n
        elif n < 0:
            return -1
        else :
            return self.fib(n-1)+self.fib(n-2)  # imp to use self parameter
        
ob1=Solution()
num=4
print(ob1.fib(num))     