''' 
leetcode 문제 

평균적으로 속도 빠른 순서 : firstBadVersion2 -> firstBadVersion1

firstBadVersion1 : 기존의 값에 이동값(절반값)을 +-해서 찾는 방식
firstBadVersion2 : 기본적인 이진탐색

추가적인 연산으로 인해 느려지는 것. 이진탐색이 깔끔하고 빠른것을 확인.
'''
import math
from time import time

first_err_version = 0
class Solution:
    def isBadVersion(self, n):
        if n < first_err_version:
            return False
        else:
            return True

    def firstBadVersion1(self, n):
        half_len = n//2
        curr = n//2
        while True:
            half_len = math.ceil(half_len/2)
            # 안좋은 버전이 아니라면. 즉, 좋은 버전이라면
            # 마지막 좋은 버전이 나올때까지 찾는다.
            if not self.isBadVersion(curr):
                # 다음 버전이 안 좋은 버전일 경우 다음 버전을 출력.
                if self.isBadVersion(curr+1):
                    return curr + 1
                curr += half_len
            # 현재가 안 좋은 버전이라면 앞에서 찾는다.
            else:
                curr -= half_len
                
    def firstBadVersion2(self, n):
        l , r = 1 , n        
        while l < r:            
            mid = l + (r-l) // 2
            if self.isBadVersion(mid):
                r = mid 
            else:
                l = mid + 1                
        return l




print('큰 수에서 구하기1')
first_err_version = 1702766719
st = time()
for i in range(100000):
    Solution().firstBadVersion1(2126753390)
print('first_time = ', time()-st)    
st = time()
for i in range(100000):
    Solution().firstBadVersion2(2126753390)
print('second_time = ', time()-st)


print('큰 수에서 구하기2')
first_err_version = 170276671
st = time()
for i in range(100000):
    Solution().firstBadVersion1(2126753390)
print('first_time = ', time()-st)    
st = time()
for i in range(100000):
    Solution().firstBadVersion2(2126753390)
print('second_time = ', time()-st)


print('작은 수에서 구하기')
first_err_version = 100
st = time()
for i in range(100000):
    Solution().firstBadVersion1(3390)
print('first_time = ', time()-st)    
st = time()
for i in range(100000):
    Solution().firstBadVersion2(3390)
print('second_time = ', time()-st)


print('맨 앞 버전이 에러일 경우')
first_err_version = 1
st = time()
for i in range(100000):
    Solution().firstBadVersion1(3390)
print('first_time = ', time()-st)    
st = time()
for i in range(100000):
    Solution().firstBadVersion2(3390)
print('second_time = ', time()-st)


print('맨 끝 버전이 에러일 경우')
first_err_version = 1
st = time()
for i in range(100000):
    Solution().firstBadVersion1(3390)
print('first_time = ', time()-st)    
st = time()
for i in range(100000):
    Solution().firstBadVersion2(3390)
print('second_time = ', time()-st)