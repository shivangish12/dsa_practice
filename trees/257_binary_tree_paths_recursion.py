# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result=[]
        def trackPaths(node,path):
            if not node:
                return
            path=path+str(node.val)
            if not node.right and not node.left:
                return result.append(path)
            left=trackPaths(node.left,path+"->")
            right=trackPaths(node.right,path+"->")

        trackPaths(root,"")   
        return result
