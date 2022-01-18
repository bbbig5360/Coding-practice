''' 
leetcode 문제 

속도 빠른 순서 : solution3 -> solution2 -> solution1

solution1 : 왼쪽, 오른쪽을 따로 가져가지 않고 카운트를 주어 현재 위치를 찾는 방식으로 이진탐색
solution2 : 기본적인 이진탐색
solution3 : list의 내장함수 index 사용

정렬된 값이라면, index를 사용해서 찾는 것이 빠른 것을 확인
'''
from time import time
class Solution1:    
    def b_search(self, nums, target, curr):
        half_len = len(nums)//2
        mid = nums[half_len]
        if mid == target:
            return curr + half_len
        elif mid < target:
            return self.b_search(nums[half_len:], target, curr+half_len)
        else:
            if half_len <= 2 :
                try:
                    return curr + nums.index(target)
                except:
                    return -1
            return self.b_search(nums[:half_len], target, curr)
    
    def search(self, nums, target) :
        try:
            # return nums.index(target)
            ans = self.b_search(nums, target, 0)
            return ans
        except:
            return -1

class Solution2:
    def search(self, nums, target):        
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l+r)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
        return -1
class Solution3:
    def search(self, nums, target) :
        return nums.index(target)
    
        
st = time()
for i in range(1000000):
    Solution1().search([-1,0,1,2,3,4,5,10,11,123,124,151,1612,1613,1615,1645,1648],10)
print('first_time = ', time()-st)    

st = time()
for i in range(1000000):
    Solution2().search([-1,0,1,2,3,4,5,10,11,123,124,151,1612,1613,1615,1645,1648],10)
print('sec_time = ', time()-st)    

st = time()
for i in range(1000000):
    Solution3().search([-1,0,1,2,3,4,5,10,11,123,124,151,1612,1613,1615,1645,1648],10)
print('third_time = ', time()-st)    
