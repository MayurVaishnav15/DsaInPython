# Selection Sort Ascending Order

# def selectionSort(nums:list):
#     n=len(nums)
#     for i in range(0,n):
#         min_index=i 
#         for j in range(i+1,n):
#             if(nums[j]<nums[min_index]):
#                 min_index=j 
#         nums[i],nums[min_index]=nums[min_index],nums[i]

#     return nums 

# print(selectionSort([9,8,7,6,5,4,3,2,1 ]))


# Selection Sort Descending Order
def selectionSort(nums:list):
    n=len(nums)
    for i in range(0,n):
        max_index=i
        for j in range (i+1,n):
            if(nums[j]>nums[max_index]):
                max_index=j 

        nums[i],nums[max_index]=nums[max_index],nums[i]
    return nums

print(selectionSort([1, 2, 3, 4, 5, 6, 7, 8, 9]))