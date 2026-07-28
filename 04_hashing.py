# nums = [1,2,3,4,5,6,7,8,5,9,10]
# hashmap=dict()
# n= len(nums)
# for i in range(0,n):
#     hashmap[nums[i]] = hashmap.get(nums[i],0)+1
# print(hashmap[5])





# n = [1,2,4,4,5,6,9,7,8,7,8,2,2,3,1,1,9,10,10,9,10]
# m = [2,23,32,1,9,7,5,3,10,111] 

# hash_list = [0]* 11
# for num in n:
#     hash_list[num] += 1 
# print(hash_list)
# res=[]
# for num in m:
#     if num>10 or num<1:
#         res.append(0)
#     else:
#         res.append(hash_list[num])
# print(res)


# HASH DICTIONARY
# nums = [1,2,4,4,5,6,9,7,8,7,8,2,2,3,1,1,9,10,10,9,10]
# m = [2,23,32,1,9,7,5,3,10,111] 
# hash_map = {}
# size = len(nums)
# for i in range(0,size):
#     hash_map[nums[i]] = hash_map.get(nums[i],0)+1
# res_dict = {}
# for i in range(0,len(m)):
#     res_dict[m[i]] = hash_map.get(m[i],0)
# print(res_dict)
# print(hash_map)


# CHARACTER VALUES 
# s= "akswtpxzo"
# q= ["d","a","y","x"]
# hash_list = [0]*27
# for ch in s:
#     ascii_val = ord(ch)
#     index = ascii_val-97
#     hash_list[index]+=1
# dict={}
# for ch in q:
#     ascii_val = ord(ch)
#     index = ascii_val-97
#     dict[ch] = hash_list[index]
# print(dict)









