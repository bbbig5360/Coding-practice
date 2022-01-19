'''
    속도 : rotate3 -> rotate2 -> rotate1

    rotate1
    : deque의 내장함수 rotate를 reverse와 append, popleft로 구현
    
    roatete2
    : rotate를 이용

    rotate3
    : 위치만큼 이동시키는 것이기 떄문에 잘라서 붙이는 방식(slicing)으로 해결

'''

from collections import deque
from time import time

class Solution:
    # deque().rotate를 구현
    def rotate1(self, nums, k):
        k = k % len(nums)
        q = deque(reversed(nums))

        for i in range(k):
            q.append(q.popleft())
        
        nums[:] = list(reversed(q))

    # rotate 사용
    def rotate2(self, nums, k):
        k = k % len(nums)
        q = deque(nums)

        for i in range(k):
            q.rotate(1)
        
        nums[:] = list(reversed(q))

    # rotate 없이 사용
    def rotate3(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]

st = time()
for i in range(1000000):
    Solution().rotate1([1,2,3,4,5,6,7],3)
print('rotate1 = ', time()-st)    


print()
st = time()
for i in range(1000000):
    Solution().rotate2([1,2,3,4,5,6,7],3)
print('rotate2 = ', time()-st)    

st = time()
for i in range(1000000):
    Solution().rotate3([1,2,3,4,5,6,7],3)
print('rotate3 = ', time()-st)    