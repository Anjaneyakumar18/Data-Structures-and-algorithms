def level_order(self):
        lst=[]
        queue=[self.root]
        while queue:
            ele=queue.pop(0)
            lst.append(ele.val)
            if ele.left:
                queue.append(ele.left)
            if ele.right:
                queue.append(ele.right)
        return lst