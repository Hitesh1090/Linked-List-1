# TC: O(n)
# SC: O(1)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        flag=True
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

            if slow == fast:
                break
        
        else:
            return None
        
        slow=head

        while slow!=fast:
            slow=slow.next
            fast=fast.next
            
        
        return fast
        