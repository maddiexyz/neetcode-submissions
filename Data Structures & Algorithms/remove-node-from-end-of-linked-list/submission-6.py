# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        first=head
        while first:
            N+=1
            first=first.next
        rmIdx= N-n
        if rmIdx==0:
            return head.next
        cur=head
        for idx in range(rmIdx-1):
            cur=cur.next
        cur.next=cur.next.next
        return head
            