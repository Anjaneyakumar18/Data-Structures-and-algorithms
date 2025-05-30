# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root,sum=0):
            if not root:
                return 
            sum+=root.val
            if (not root.left) and (not root.right):
                if sum==targetSum:
                    return True
            
            return dfs(root.left,sum) or dfs(root.right,sum)

            return False
        return dfs(root)
