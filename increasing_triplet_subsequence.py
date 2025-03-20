class solution:
    def find_Triplet(self,nums):

        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] < nums[i+2]:
               print("True , triplet exists")
              # print(i)           
               return True
            
        print("False , triplet doesnot exists")
        return False   
        
        
    
ob1=solution()
nums=[1,2,-3,-44,2342,12333,1222222]      # it is 
ob1.find_Triplet(nums)