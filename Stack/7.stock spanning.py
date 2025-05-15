
#stock spanning using stack
'''
    given an array [15,6,3,6,8,3] find the concecutive no of decresing 
    numbers on it's left
    1.find nearest left maximum number and store it's index as well
    2.find difference between the index and indexed element in final array
                {[(i-nearest_max[i])]}
'''


def stock_spaning(arr:list[int])->list[int]:
    nearest_max=[]
    stack=[]
    for i in range(len(arr)):
        while stack and stack[-1][0]<=arr[i]:
            stack.pop()
        if not stack:
            nearest_max.append(-1)
        else:
            nearest_max.append((stack[-1][1]))
        stack.append((arr[i],i))
    for i in range(len(nearest_max)):
        nearest_max[i]=i-nearest_max[i]
    return nearest_max
    
print(stock_spaning([10,8,3,7,8,10,1,4]))





#lc 901


class StockSpanner:
    def __init__(self):
        self.stack = []
        self.i = 0

    def next(self, price: int) -> int:
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if not self.stack:
            span = self.i + 1
        else:
            span = self.i - self.stack[-1][1]
        self.stack.append((price, self.i))
        self.i += 1
        return span
