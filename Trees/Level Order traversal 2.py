# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=[[root]]
        ans=[[root.val]]
        while queue:
            level=queue.pop()
            next_lev=[]
            next_lev_val=[]
            for n in level:
                if n.left:
                    next_lev.append(n.left)
                    next_lev_val.append(n.left.val)
                if n.right:
                    next_lev.append(n.right)
                    next_lev_val.append(n.right.val)
            if next_lev:
                queue.append(next_lev)
                ans.append(next_lev_val)
        return ans[::-1]

        
