# def bubble(input:list):
#     # 3,2,1,5,9,8,7
#     i=0
#     j=1
#     n=len(input)
#     for i in range(n-2,-1,-1):
#         for j in range(0,i+1):
#             if input[j]>input[j+1]:
#                 input[j],input[j+1] = input[j+1],input[j]
#     return input

# print(bubble([3,2,1,5,9,8,7]))


class sorting:
    def __init__(self,input:list):
        self.input = input
        self.n = len(input)
    
    def BubbleSort(self):
        for i in range(self.n-2,-1,-1):
            for j in range(0,i+1):
                if self.input[j]>self.input[j+1]:
                    self.input[j],self.input[j+1] = self.input[j+1], self.input[j]
        return self.input
                    
    def SelectionSort(self):
        for i in range(0,self.n):
            min_index = i
            for j in range(i+1,self.n):
                if self.input[j] < self.input[min_index]:
                    min_index=j
                self.input[i],self.input[min_index] = self.input[min_index],self.input[i]     
        return self.input      

sort = sorting([9,8,7,6,5,4,3,2,1])
print("BubbleSort : ",*sort.BubbleSort()) # list unpacking
print("SelectionSort :", *sort.SelectionSort())