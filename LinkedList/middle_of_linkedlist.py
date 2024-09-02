'''  10->20->30->40->50->60->70->80->90->100->None   '''
#           middle-->^^<--middle

'''
Approach slow and fast pointers

    slow+=1
    fast+=2
    
'''


def middle(self)->int:
        
        slow=self.head
        fast=self.head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        return slow.val