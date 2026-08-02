class Array:
    @staticmethod
    def largest(input):
        # 3 2 6 9 8 4 7 
        n = len(input)
        largest = input[0]
        for i in range(0,n): 
            largest = max(largest,input[i])
        return largest

        






input = list(map(int,input("Enter Space Saperated Values: ").split()))
obj = Array()
print(obj.largest(input))





        