# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        row_big=[]
        queue=[[root]]
        while queue:
            next_level=[]
            current=float(-inf)
            c=queue.pop(0)
            for node in c:
                current=max(current,node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            row_big.append(current)
            if next_level:
                queue.append(next_level)
        return row_big
        
