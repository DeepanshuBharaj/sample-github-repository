# move all the zeroes in an array in the last
class solution:
    def moveZero(self,nums:list[int]) -> int :
        next_Non_Zero = 0
#using two pointer approach
        for i in range(len(nums)):
            if nums[i] != 0:
               
               nums[next_Non_Zero] , nums[i] = nums[i] , nums[next_Non_Zero]

               next_Non_Zero += 1
        return nums       

ob=solution()
nums=[1,0,342,0,4,0,346]
print(ob.moveZero(nums))        