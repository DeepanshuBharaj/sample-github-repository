#return max amount of water container can save
#height=[1,8,6,2,5,4,8,3,2]
# brute force approach        time-complexity=O(n^2)
"""def bforce(height:list[int])->int:
    max_water=0
    num=1
    for i in range(0,len(height)):           #using nested loop to find every possibility 
        for j in range(i+1,len(height)):
           print("iteration number: ",num)
           print("for height[i]= ",height[i]," height[j] = ",height[j])
           width=j-i #formula to calculate width
           ht=min(height[i],height[j])     
           # to calculate area between two heights
           area=width*ht
           max_water=max(max_water,area)
           print(max_water)
           num+=1
    print("maximum amount of water that can be filled in the container is : ",max_water)
"""

# using two pointers (optimal approach)       time-complexity=O(n)
def twoptr(height:list[int])->int:
    left=0
    right=len(height)-1
    max_area=0
    # container = width * ht

    while left<right:
        width=right-left
        ht=min(height[left],height[right])

        current_area=width*ht
        max_area = max(max_area,current_area)

        #  ***imp*** moving the min. one
        if height[left] < height[right]:             
            left +=1

        else :
            right -=1

    return max_area        

height=[1,8,6,2,5,4,8,3,2]
result=twoptr(height)
print(result)