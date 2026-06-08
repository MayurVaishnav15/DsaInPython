# This is normal approach 2^n both 
# def fib(n):
#     a,b=0,1
#     print(a,b,end=" ")
#     for i in range(n-2):
#         c=a+b
#         print(c,end=" ")
#         a=b
#         b=c
# fib(9)

# This is rec TC and SC = O(2^n) 
def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(7))