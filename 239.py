class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        que = []
        i = j = 0
        ans = []
        while j < len(nums):
            while len(que) > 0 and que[-1] < nums[j]:
                
                que.pop()
                
            que.append(nums[j])
            
            if j < k-1:
                
                j += 1
                
            elif j - i + 1 == k:
                
                ans.append(que[0])
                
                if nums[i] == que[0]:
                    
                    que.pop(0)
                    
                i += 1
                j += 1
                
        return ans

# class Solution(object):
#     def maxSlidingWindow(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: List[int]
#         """
#         max_temp = float('-inf')                # -(10 ** 4)로 했는데 시간초과남
#         window = collections.deque()            # 슬라이싱으로 3개 채우고 시작하려고 했는데 시간초과남
#         res = []
        
#         for i, val in enumerate(nums):
#             window.append(val)
            
#             if i < k - 1:
#                 continue
            
#             if max_temp == float('-inf'):
#                 max_temp = max(window)
#             elif max_temp < val:
#                 max_temp = val
                
#             res.append(max_temp)
            
#             if max_temp == window.popleft():
#                 max_temp = float('-inf')
                
        
#         return res
        