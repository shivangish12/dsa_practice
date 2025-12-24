# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum = float('-inf')
        def heightSum(node):
            if not node:
                return 0
            left=heightSum(node.left)
            left_sum=max(left,0)
            right=heightSum(node.right)
            right_sum=max(right,0)
            self.sum=max(self.sum,node.val+left_sum+right_sum)
            return node.val+max(left_sum,right_sum)
        heightSum(root)
        return self.sum

            

