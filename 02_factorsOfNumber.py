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

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sum = 1
        result = []
        if num==1:
            return result
        for i in range(2,int(num**.5)+1):
            if(num%i==0):
                sum+=i+(num//i)
                result.append(i)
                if i !=(num//i):
                    result.append((num//i))
        print(result)
        return True if sum==num else False
            
obj=Solution()
print(obj.checkPerfectNumber(1))   