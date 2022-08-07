# Definition for singly-linked list.
from tempfile import tempdir


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        swp = head
        
        while swp and swp.next :
            
            swp.val, swp.next.val = swp.next.val, swp.val
            
            swp = swp.next.next
        
        return head # 19ms, 13.6mb 이거로 하는 재귀는 이해가 안된다..