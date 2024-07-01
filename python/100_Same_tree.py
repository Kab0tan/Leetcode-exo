# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        M = True
        def dfs(root,root2):
            nonlocal M
            # print(root)
            # print(root2)
            # print("M is currently",M)
            # print()
            if (root is None and root2 is not None) or (root is not None and root2 is None):
                # print("youpi")
                M = False
                # print(M)
                return
            elif root is None and root2 is None:
                return
            else:
                if root.val != root2.val:
                    M = False
            dfs(root.left,root2.left)
            dfs(root.right,root2.right)
            return 
        dfs(p,q)
        print("M is ",M)
        return M
        
