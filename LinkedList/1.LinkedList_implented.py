class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
            return
        
        temp = self.head
        while temp.next:  
            temp = temp.next
        
        temp.next = ListNode(val)

    def pop(self):
        if not self.head:
            print('empty Linked list')
            return
        
        if not self.head.next:
            self.head = None
            return

        temp = self.head
        while temp.next.next:  
            temp = temp.next
        
        temp.next = None

    def length(self):
        l=0
        temp=self.head
        while temp:
            l+=1
            temp=temp.next
        return l
        
    def insert(self, val, index):
        if index >= self.length():  
            return self.append(val)
        new_node = ListNode(val)
        if index == 0:  
            new_node.next = self.head
            self.head = new_node
            return
        i = 0
        temp = self.head
        while i < index - 1:  
            temp = temp.next
            i += 1
        new_node.next = temp.next
        temp.next = new_node

    def remove(self,index):
        if index>=self.length():
            self.pop()
        temp=self.head
        i=1
        while i<index:
            temp=temp.next
            i+=1
        temp.next=temp.next.next

    def view(self):
        temp = self.head
        while temp:
            print(temp.val, '-->', end=' ')
            temp = temp.next
        print('None')  

    
