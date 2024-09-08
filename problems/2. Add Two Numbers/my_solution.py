# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a new linked list to store the result
        l3 = ListNode(0, None)

        # Pointers for traversing the input lists and constructing the result list
        p3 = l3
        p1 = l1
        p2 = l2
        carry = 0

        # Loop through both lists until both are fully processed
        while p1 is not None or p2 is not None:
            p3.next = ListNode(0, None)
            p3 = p3.next

            # When list l1 is fully traversed
            if p1 is None:
                p3.val = (0 + p2.val + carry) % 10
                carry = 1 if 0 + p2.val + carry > 9 else 0
                p2 = p2.next

            # When list l2 is fully traversed
            elif p2 is None:
                p3.val = (p1.val + 0 + carry) % 10
                carry = 1 if p1.val + 0 + carry > 9 else 0
                p1 = p1.next

            # When both lists have nodes remaining
            else:
                p3.val = (p1.val + p2.val + carry) % 10
                carry = 1 if p1.val + p2.val + carry > 9 else 0
                p1 = p1.next
                p2 = p2.next

        # If there's a carry left after the final nodes, add it to the result list
        if carry == 1:
            p3.next = ListNode(1, None)

        # Return the result linked list, excluding the dummy head
        return l3.next