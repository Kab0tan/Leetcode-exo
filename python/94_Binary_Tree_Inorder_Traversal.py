# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        def dfs(root, M):
            if root is None:
                return 
            
            dfs(root.left,M)
            M.append(root.val)
            dfs(root.right,M)
            
            return M
        
        return dfs(root,[])
