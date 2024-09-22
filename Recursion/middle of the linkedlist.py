def linked_list_middle(self,node):
    def middle(slow,fast):
        if not fast or fast.next:
            return slow
        middle(slow.next,fast.next.next)

    return middle(node,node)