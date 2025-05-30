# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue=[[root]]
        ans=[root.val]
        while queue:
            currentLevel=queue.pop(0)
            nextLevel=[]
            for node in currentLevel:
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if nextLevel:
                ans.append(nextLevel[-1].val)
                queue.append(nextLevel)
        return ans
