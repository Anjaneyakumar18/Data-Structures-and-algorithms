class listnode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = listnode(val)
            return
        
        c = self.head
        while c.next:
            c = c.next
        
        node = listnode(val)
        c.next = node
        node.prev = c

    def length(self):
        length = 0
        cur = self.head
        while cur:
            length += 1
            cur = cur.next
        
        print(f"Length of linkedList is {length}")
        return length
    
    def insert(self, val, pos):
        if pos == 0:  # Insert at the beginning
            new_node = listnode(val)
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        if pos >= self.length():  # Insert at the end
            self.append(val)
            return
        
        c = self.head
        num = 0
        while num < pos:
            c = c.next
            num += 1
        
        new_node = listnode(val)
        new_node.prev = c.prev
        new_node.next = c
        
        if c.prev:
            c.prev.next = new_node
        c.prev = new_node

    def view(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

    def viewFromBack(self):
        curr = self.head
        if not curr:
            return
        
        while curr.next:
            curr = curr.next

        while curr:
            print(curr.val, end=" <- ")
            curr = curr.prev
        print("None")

# Example usage
ll = linkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.view()             # 10 -> 20 -> 30 -> None
ll.viewFromBack()     # 30 <- 20 <- 10 <- None
ll.length()           # Length of linkedList is 3
ll.insert(40, 1)      # Insert 40 at position 1
ll.view()             # 10 -> 40 -> 20 -> 30 -> None
