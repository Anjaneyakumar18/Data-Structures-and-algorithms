class item:
    def __init__(self,val):
        self.val=val
        self.next=None

class Stack_using_linkedlist:

    def __init__(self):
        self.head=None
        self.length=0
        self.top=-1
    
    def push(self,val):
        self.length+=1
        self.top+=1
        if not self.head:
            self.head=item(val)
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=item(val)
        return
    
    def pop(self):
        self.length-=1
        self.top-=1
        current=self.head
        while current.next.next:
            current=current.next
        print(current.next.val)
        current.next=None
        return
    
    def top(self):
        current=self.head
        while current.next:
            current=current.next
        print(current.val)
        return
    
    def view_stack(self):
        current=self.head
        while current:
            print(current.val)
            current=current.next
        return
    
    def isEmpty(self):
        return print(not self.length>0)


if __name__ == "__main__":
    mystack=Stack_using_linkedlist()
    mystack.isEmpty()
    mystack.push(10)
    mystack.push(20)
    mystack.view_stack()
    mystack.pop()
    mystack.view_stack()
    mystack.top()
    mystack.isEmpty()
    print(mystack.length)