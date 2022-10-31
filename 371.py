class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        while b:
            sums = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = sums
            b = carry
            print(a)
            print(b)
        
        if (a>>31) & 1: # If a is negative in 32 bits sense
            return ~(a^mask)
        
        return a

        # https://leetcode.com/problems/sum-of-two-integers/discuss/776952/python-best-leetcode-371-explanation-for-python