# # This is normal approach 2^n both 
# def fib(n):
#     a,b=0,1
#     print(a,b,end=" ")
#     for i in range(n-2):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c
# fib(9)





# # Recursion
# def fib(n): # 0 1 1 2 3 5 8 13 21 
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return fib(n-1) + fib(n-2)
    
# fib(9)