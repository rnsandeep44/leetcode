# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is not None:
            if root.val == targetSum and root.left is None and root.right is None:
                return True
            status_left = self.hasPathSum(root.left, targetSum- root.val)
            status_right = self.hasPathSum(root.right, targetSum- root.val)
            return status_left or status_right

        else:
            return False



