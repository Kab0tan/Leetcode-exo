# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        M = True
        def dfs(root,root2):
            nonlocal M
            if (root is None and root2 is not None) or (root is not None and root2 is None):
                M = False
                return
            elif root is None and root2 is None:
                return
            else:
                if root.val != root2.val:
                    M = False
            dfs(root.left,root2.right)
            dfs(root.right,root2.left)
            return 
        dfs(root,root)
        return M
