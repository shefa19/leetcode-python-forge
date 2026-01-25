'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        crr1 = l1
        crr2 = l2

        ans = ListNode()
        crr3 = ans

        v, c = 0, 0

        while crr1 or crr2:
            if crr1 and crr2:
                sm = crr1.val + crr2.val + c

                v = sm % 10
                c = sm // 10

                crr1, crr2 = crr1.next, crr2.next

            elif crr1:
                sm = crr1.val + c

                v = sm % 10
                c = sm // 10

                crr1 = crr1.next
            
            else:
                sm = crr2.val + c

                v = sm % 10
                c = sm // 10

                crr2 = crr2.next

            crr3.val = v
            if crr1 or crr2:
                crr3.next = ListNode()
                crr3 = crr3.next
        if c:
            crr3.next = ListNode()
            crr3 = crr3.next
            crr3.val = c
        
        return ans