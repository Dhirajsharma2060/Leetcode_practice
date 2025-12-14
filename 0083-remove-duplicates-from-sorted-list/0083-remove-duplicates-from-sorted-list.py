# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        mapped=set()
        while head:
            if head.val not in mapped:
                curr.next=head
                curr=curr.next
                mapped.add(head.val)
            # we need to move the head so that we can check and traverse the list 
            head=head.next
        curr.next=None       
        return dummy.next

        