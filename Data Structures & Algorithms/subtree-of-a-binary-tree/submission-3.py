# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(r1,r2):
            s=[(r1,r2)]
            while s:
                t1,t2=s.pop()
                if not t1 and not t2:
                    continue
                if not t1 or not t2 or t1.val!=t2.val:
                    return False
                s.append((t1.left,t2.left))
                s.append((t1.right,t2.right))
            return True
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
        
        