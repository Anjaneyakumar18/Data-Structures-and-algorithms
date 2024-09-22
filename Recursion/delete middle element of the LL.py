def deletemiddle(self,head):
    if not head or head.next:
        return 0
    
    def middle(prev,slow,fast):
        if not fast or not fast.next:
            if prev:
               prev.next=prev.next.next
            return head
        
        middle(prev.next,slow.next,fast.next.next)

    return middle(None,head,head)
