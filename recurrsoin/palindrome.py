# This is a two pointer approach O(N) and O(1)
# def palindromefunc(nums):
#     left=0
#     right=len(nums)-1
#     while(left<=right):
#         if(nums[left]!=nums[right]):
#             return False
#         left+=1
#         right-=1
#     return True

# print(palindromefunc('1234321'))


# This is a recursie approach O(N) & O(1)
def recPalindromFunc(nums,left=0,right=None):
    if right is None:
        right = len(nums) - 1
    if(left>=right):
        return True
    if(nums[left]!=nums[right]):
        return False
    return recPalindromFunc(nums,left+1,right-1)
print(recPalindromFunc('1234321'))