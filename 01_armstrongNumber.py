# class Solution:
#     @staticmethod
#     def isArmstrong(n : int ) -> bool:
        
#         nod= len(str(n))
#         total=0
#         chk=n
#         while(chk>0): #123
#             last = chk%10
#             total= total + last**nod
#             chk//=10
#         return True if total == n else False

# n = int(input("Enter a number : "))
# print(Solution.isArmstrong(n))


class Solution:
    
    def isArmstrong(self,n : int ) -> bool:
        
        nod= len(str(n))
        total=0
        chk=n
        while(chk>0): #123
            last = chk%10
            total= total + last**nod
            chk//=10
        return True if total == n else False

if __name__ == "__main__":
    obj = Solution()
    try:
        user_input = int(input("Enter a number : "))
        print(obj.isArmstrong(user_input))
    
    except ValueError:
        print("Enter Valid Input")