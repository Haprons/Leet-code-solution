# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        decimal_value = 0  # Initialize the decimal value to 0
        current = head     # Start from the head of the linked list

        # Traverse the linked list
        while current:
            # For each bit, shift the current decimal value one position to the left
            # (equivalent to multiplying by 2) and then add the current bit's value.
            # This effectively builds the decimal number as we move from MSB to LSB.
            decimal_value = (decimal_value * 2) + current.val
            current = current.next  # Move to the next node

        return decimal_value