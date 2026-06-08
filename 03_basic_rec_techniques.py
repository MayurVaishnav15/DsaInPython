# def func(n,i):
#     if(i>n):
#         return   
#     print(i)
#     func(n,i+1)
# func(5,1) 

def func(n):
    if(n==0):
        return 
    func(n-1)
    print(n)
func(9)