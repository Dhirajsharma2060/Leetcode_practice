# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not  head.next:
            return head
        slow=head # odd
        fast=head.next #even 
        evenhead=head.next
        while fast and fast.next:
            slow.next=fast.next
            slow=slow.next
            fast.next = slow.next
            slow.next = evenhead
            fast=fast.next
        return head




        
        
        