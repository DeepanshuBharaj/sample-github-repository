class Solution(object):
    def search(self, nums, target):

        if len(nums) == 0:
            return -1
        
        left , right = 0 ,len(nums) - 1   

        while left <= right:
            mid =left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1     

ob=Solution()
nums = [1,2,9,63,273]
print(ob.search(nums,9))               