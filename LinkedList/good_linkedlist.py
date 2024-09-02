'''
A linked list is a good linked list if it is strictly increasing
'''
#1->2->3->4->5
def good_linkedlist(self)->bool:
    prev=self.head.val
    temp=self.head.next
    while temp.next:
        if prev<=temp.val:
            return False
        temp=temp.next
    return True