# Add Two Numbers

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example 1

**Input:** 
- l1 = [2,4,3]
- l2 = [5,6,4]

**Output:** 
- [7,0,8]

**Explanation:** 
- The numbers represented by the linked lists are `342` and `465`, respectively.
- The sum is `342 + 465 = 807`.
- The output linked list `[7,0,8]` represents the number `807`.

### Example 2

**Input:** 
- l1 = [0]
- l2 = [0]

**Output:** 
- [0]

### Example 3

**Input:** 
- l1 = [9,9,9,9,9,9,9]
- l2 = [9,9,9,9]

**Output:** 
- [8,9,9,9,0,0,0,1]

**Explanation:** 
- The numbers represented by the linked lists are `9999999` and `9999`, respectively.
- The sum is `9999999 + 9999 = 10009998`.
- The output linked list `[8,9,9,9,0,0,0,1]` represents the number `10009998`.

## Constraints

- The number of nodes in each linked list is in the range `[1, 100]`.
- `0 <= Node.val <= 9`
- It is guaranteed that the list represents a number that does not have leading zeros.


<hr>


# Add Two Numbers - Solution Explanation

## Problem Overview

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. The task is to add the two numbers and return the sum as a linked list, with the result also being stored in reverse order.

## Solution Explanation

### Approach

The solution follows a straightforward approach to iterate through the linked lists `l1` and `l2`, digit by digit, adding corresponding digits along with any carry from the previous addition. The resulting sum is stored in a new linked list `l3`.

### Steps

1. **Initialization:**
   - A dummy node `l3` is created to serve as the starting point of the result linked list.
   - Three pointers are used:
     - `p1` for iterating through `l1`.
     - `p2` for iterating through `l2`.
     - `p3` for building the result list `l3`.
   - A `carry` variable is initialized to 0 to keep track of any overflow during addition.

2. **Iteration through the Lists:**
   - The loop continues as long as there are nodes left in either `l1` or `l2`.
   - At each iteration:
     - A new node is created for `p3.next` to hold the sum of the current digits from `p1` and `p2`, along with the carry.
     - The sum of the current digits and carry is calculated.
     - If `p1` is `None`, it's treated as if it contributes a `0` to the sum.
     - If `p2` is `None`, it's treated similarly.
     - The digit for the current place value in the result is `sum % 10`, and the carry is updated to `sum // 10`.
   - The pointers `p1` and `p2` are advanced to the next nodes in their respective lists.

3. **Handling the Final Carry:**
   - After the loop, if there is still a carry left, a new node with the value `1` is added to the result list.

4. **Returning the Result:**
   - The function returns `l3.next`, which points to the head of the result linked list (excluding the initial dummy node).

### Code Structure

```python
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
```

## Complexity Analysis

- **Time Complexity:** `O(max(m, n))`
  - The algorithm iterates through both linked lists `l1` and `l2`, processing each node exactly once.
  - `m` is the number of nodes in `l1`, and `n` is the number of nodes in `l2`.
  - The loop runs `max(m, n)` times, as it continues until both lists are fully traversed.

- **Space Complexity:** `O(max(m, n))`
  - The space complexity is also `O(max(m, n))` due to the storage needed for the resulting linked list.
  - In the worst case, the result linked list will have `max(m, n) + 1` nodes, where the extra node is due to a final carry (e.g., when both linked lists represent numbers like `999...999`).


