# Approach: walk the list with 3 pointers: prev, curr, nxt.
# Each pass:
#   nxt = curr.next   -> save the rest of the list before flipping
#   curr.next = prev  -> flip the arrow backwards
#   prev = curr       -> move prev first (so it grabs the old curr)
#   curr = nxt        -> then move curr forward
# At the end curr is None and prev is the old last node,
# which is the new head, so return prev.
# Time O(n): one pass, one step per node.
# Space O(1): only 3 pointers, arrows flipped in place.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
