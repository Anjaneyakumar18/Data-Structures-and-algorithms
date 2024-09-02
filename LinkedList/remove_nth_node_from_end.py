"""
n=2
1->2->3->4->5->6->7->none
               ^
               |
        delete this node 
"""


def remove_nth_node_from_end(self, num):
    fast = self.head
    slow = self.head
    
    for _ in range(num):
        if fast is None:
            return self.head
        fast = fast.next

    if fast is None:
        self.head = self.head.next
        return self.head

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return self.head
