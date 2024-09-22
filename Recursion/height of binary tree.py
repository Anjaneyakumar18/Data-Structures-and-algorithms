'''


        1
     2    2
   3  3  3  3
 4  4 

'''

def height_of_binary_tree(self,TreeNode,num=1):
    if not TreeNode.left and not TreeNode.right:
        return num
    if TreeNode.left:
        leftheight=self.height_of_binary_tree(TreeNode.left,num+1)
    if TreeNode.right:
        rightheight=self.height_of_binary_tree(TreeNode.right,num+1)

    return max(leftheight,rightheight)

    