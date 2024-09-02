'''

ll1=|3|->|4|->|6|->|9|

ll2=|1|->|0|->|3|->|3|

ans=|4|->|4|->|9|->|1|->|2|

'''
def add_nums(self,head1,head2):
    carry=0
    while head1 and head2:
        carry=(head1.val+head2.val)%10
        head2.val=head2.val+head1.val+carry
        head1=head1.next
        head2=head2.next

    if carry:
        head2.next=Listnode(carry)
    return
