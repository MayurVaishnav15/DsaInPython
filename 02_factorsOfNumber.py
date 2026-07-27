# class Solution:
#     def checkPerfectNumber(self, num: int) -> bool:
#         sum = 0
#         for i in range(1,num):
#             if(num%i==0):
#                 sum=sum+i
#         print(sum)
#         return True if sum==num else False

# obj=Solution()
# print(obj.checkPerfectNumber(28))    

# class Solution:
#     def checkPerfectNumber(self, num: int) -> bool:
#         sum = 1
#         result = []
#         if num==1:
#             return result
#         for i in range(2,int(num**.5)+1):
#             if(num%i==0):
#                 sum+=i+(num//i)
#                 result.append(i)
#                 if i !=(num//i):
#                     result.append((num//i))
#         print(result)
#         return True if sum==num else False
            
# obj=Solution()
# print(obj.checkPerfectNumber(1))   





# # BruteForce
# class factors:
#     @staticmethod
#     def func(input:int):
#         result = []
#         for i in range(1,input+1):
#             if input % i == 0:
#                 result.append(i)
#         return result
# obj = factors()
# print(obj.func(20))
# TC = SC = O(N)


# Little Better 
# class factors:
#     @staticmethod
#     def func(input:int):
#         results = []
#         for i in range(1,input//2):
#             if input % i == 0:
#                 results.append(i)
#         results.append(input)
#         return results

# obj = factors()
# print(obj.func(20))
# TC = O(n/2) which is equal to O(n)
# Sc = (K) -> number of factors 



# Optimal  25
# import math
# class factors:
#     @staticmethod
#     def func(input:int):
#         results = []
#         n = int(math.sqrt(input))
#         for i in range(1,n+1):
#             if input%i==0:
#                 results.append(i)
#                 results.append(input//i)
#         results.remove(math.sqrt(input)) # BECAUSE this comes twice
#         return results
    
# input = int(input("Enter a Number for Calculating Factors: "))
# obj = factors()
# print(obj.func(input))
