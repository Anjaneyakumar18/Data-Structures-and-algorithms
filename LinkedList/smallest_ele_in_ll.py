def smallest(self)->int:
    minimum=self.head.val
    temp=self.head

    while temp.next:
        minimum=min(minimum,temp.val)
        temp=temp.next
        
    return minimum
