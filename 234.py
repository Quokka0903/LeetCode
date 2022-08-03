class Solution(object):
    def isPalindrome(self, head):
        q = []
        temp = head
        while temp is not None :
            q.append(temp.val)
            temp = temp.next
        for i in range(len(q)//2) :
            if q.pop(0) != q.pop():
                return False
        return True