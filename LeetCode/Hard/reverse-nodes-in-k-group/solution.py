class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        def getKth(node, k):
            while node and k > 0:
                node = node.next
                k -= 1
            return node
        
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        
        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            
            # reverse group
            prev, curr = kth.next, groupPrev.next
            
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        
        return dummy.next