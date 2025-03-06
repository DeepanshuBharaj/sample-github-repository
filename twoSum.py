class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i]+nums[j] == target :
                    return [i, j]
        # Return an empty list if no solution is found
        return []
    
nums=[2,4,7,5]
target=12

solution=Solution()
result=solution.twoSum(nums,target)
print(result)