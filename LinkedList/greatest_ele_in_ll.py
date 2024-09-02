def find_greatest(self)->int:
    maximum=self.head.val
    temp=self.head
    while temp.next:
        maximum=max(temp.val,maximum)
        temp=temp.next
    return maximum