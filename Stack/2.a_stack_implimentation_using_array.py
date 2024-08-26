class Stack:
    def __init__(self,limit)->None:
        self.stack=[]
        self.top=-1
        self.limit=limit
    def push(self,item:int)-> None:
        if self.top==self.limit:
            return 'Stack overflow!'
        self.stack.append(item)
        self.top+=1
    def pop(self)->int:
        if self.top>=0:
            k=self.stack.pop()
            self.top-=1
            return k
        return 'Empty Stack!!'
    def Top(self)->int:
        return self.stack[self.top]
    
    def isEmpty(self):
        return self.top==-1
    
    def view_stack(self):
        k=len(self.stack)-1
        while k>=0:
            print(self.stack[k])
            k-=1
        


if __name__=="__main__":
    mystack=Stack(10)
    mystack.push(10)
    mystack.push(20)
    mystack.push(30)
    mystack.view_stack()
    mystack.pop()
    mystack.Top()
    mystack.isEmpty()