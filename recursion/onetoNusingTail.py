# def func(n):
#     if(n<0):
#         return
#     func(n-1)
#     print(n)
# func(5)


def func(n):
    if(n>5):
        return
    func(n+1)
    print(n)
func(1)