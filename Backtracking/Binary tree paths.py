class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        
        def dfs(node, path):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                ans.append("->".join(path))
            else:
                dfs(node.left, path)
                dfs(node.right, path)
            path.pop()
        
        dfs(root, [])
        return ans
