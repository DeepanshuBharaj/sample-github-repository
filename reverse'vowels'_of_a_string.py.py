class solution():
    def rev_vowels(self,s:list[str]):
        vowels='aeiouAEIOU'
        left=0 
        right=len(s) - 1
        print(s)
        while left < right :
            if s[left] not in vowels:
                left+=1
            elif s[right] not in vowels:
                right-=1
            else:
                s[left],s[right]=s[right],s[left]
                 
                left+=1
                right-=1
        print(s)
        return s

obj1=solution()
s=list(input("enter a string containing vowels"))
obj1.rev_vowels(s)            