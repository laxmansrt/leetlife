class Solution:
    def deleteDuplicates(self, head):
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # remove duplicate
            else:
                current = current.next  # move forward
                
        return head