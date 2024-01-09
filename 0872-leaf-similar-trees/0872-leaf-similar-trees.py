# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        get=[]
        teg=[]
        def dfs(root):
            
            if not root:
                return
            if root.left is None and root.right is None:
                get.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        def dfss(root):
            
            if not root:
                return
            if root.left is None and root.right is None:
                teg.append(root.val)
            dfss(root.left)
            dfss(root.right)
        
        dfs(root1)
        dfss(root2)
        return get==teg