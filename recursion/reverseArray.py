
# This is 2 pointer approach Better than recursive approach 
# TC = O(N)  SC = O(1)
# def swapfunc(nums:list)->list:  
#     left=0
#     right=len(nums)-1
#     while(left<right):
#         nums[right],nums[left]=nums[left],nums[right]
#         left+=1
#         right-=1
#     return nums

# print(swapfunc([1,2,3,4,5,6,7,8,9,10]))


# Recursive Approach
def swapfunc(nums,left,right):
    if left>=right:
        return nums
    nums[left],nums[right] = nums[right],nums[left]
    return swapfunc(nums,left+1,right-1)

nums = [1,2,3,4,5,6,7,8,9,10]
print(swapfunc(nums,0,9))


