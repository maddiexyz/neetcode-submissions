# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack=[]
        inorder=[]
        curr=root
        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if inorder and curr.val<inorder[-1]:
                return False
            inorder.append(curr.val)
            curr = curr.right
        return len(set(inorder))==len(inorder)
        