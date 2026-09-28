# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r1,r2):
            if not r1 or not r2:
                return r1 is r2
            return r1.val==r2.val and isSame(r1.left,r2.left) and isSame(r1.right,r2.right)
        if not subRoot:
            return True
        if not root:
            return False
        stack=[root]
        while stack:
            top = stack.pop()
            if top.val==subRoot.val and isSame(top,subRoot):
                return True
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return False
        
        