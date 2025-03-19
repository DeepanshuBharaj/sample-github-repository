class Solution:
        def reverseWords(self,s:str):  
            s=s.split()                              
            s=s[::-1]                                
            s=" ".join(s) 
            print(s)                           
            return s
        
obj1=Solution()      
x="what is my name"
obj1.reverseWords(x)  