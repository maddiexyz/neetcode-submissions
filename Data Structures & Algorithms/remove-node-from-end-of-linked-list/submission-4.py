# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        N = 0
        first=head
        while first:
            N+=1
            first=first.next
        if N-n==0:
            return head.next
        pos=1
        second=head
        nxt=second.next
        while pos<N-n:
            pos+=1
            second=nxt
            nxt=nxt.next
        second.next=nxt.next
        return head
            