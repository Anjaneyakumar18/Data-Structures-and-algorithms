'''
linked list must have even numbers
in even positions and odd nuumbers in odd positions
'''
#example
# 1->2->3->4->5

def even_add_odd(self)->bool:
    if not self.head:
        return True
    
    odd=self.head
    even=self.head.next

    while odd and even:

        if odd%2==0 or even%2!=0:
            return False
        
        odd=odd.next.next
        even=even.next.next

    return True