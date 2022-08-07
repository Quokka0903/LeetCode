# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None :
            return None
        
        else :
            
            hol = head
            zzac = head.next
            temp = zzac        
            
            while hol.next and zzac.next :
                
                hol.next = hol.next.next
                hol = hol.next
                
                zzac.next = zzac.next.next
                zzac = zzac.next
            
            
            hol.next = temp
        
            return head # 56ms, 17mb