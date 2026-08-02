class Array:
    @staticmethod
    def SecLargest(input):
        n= len(input)
        secLargest = float('-inf')
        largest = float('-inf')
        for i in range(0,n):
            if input[i]>largest:
                secLargest = largest
                largest = input[i]
            if input[i]< largest and input[i]>secLargest:
                secLargest=input[i]
        return secLargest




input= list(map(int,input("Enter space saperated values: ").split()))
obj = Array()
print(obj.SecLargest(input))