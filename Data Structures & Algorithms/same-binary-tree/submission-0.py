# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q:
                return True
            if p and q and p.val==q.val:
                left=same(p.left,q.left)
                right=same(p.right,q.right)
                return left and right
            else:
                return False
        return same(p,q)