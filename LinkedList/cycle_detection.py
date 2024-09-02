def detect_cycle(self):
    slow=self.head
    fast=self.head
    
    while fast or fast.next:
        slow=slow.next
        fast=fast.next.next
        if fast==slow:
            return True

    return False