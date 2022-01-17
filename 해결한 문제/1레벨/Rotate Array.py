''' 
leetcode 문제 
'''

from collections import deque

# deque().rotate를 구현
class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        q = deque(reversed(nums))

        for i in range(k):
            q.append(q.popleft())
        
        nums[:] = list(reversed(q))

# rotate 사용
class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        q = deque(nums)

        for i in range(k):
            q.rotate(1)
        
        nums[:] = list(reversed(q))

# rotate 없이 사용
class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
