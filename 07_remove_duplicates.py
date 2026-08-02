
# # Bruteforce Method
# class Array:
#     @staticmethod
#     def remove_dup(input):
#         n= len(input)
#         dict = {}
#         for i in range(0,n):
#             dict[input[i]]=0
#         j=0
#         for k in dict:
#             input[j] = k
#             j+=1
#         return j

# input = list(map(int,input("Enter Values: ").split()))
# obj= Array()
# print("The Number of unique elements are",obj.remove_dup(input))





# Optimal Solution 
class Array:
    @staticmethod
    def remove_dup(input):
        n=len(input)
        if n==1:
            return 1
        i= 0
        j= i+1
        while(j<n):
            if input[i] != input[j]:
                i+=1
                input[i],input[j] = input[j],input[i]
            j+=1
        return i+1
        

input = list(map(int,input("Enter Values: ").split()))
obj= Array()
print("The Number of unique elements are",obj.remove_dup(input))




























