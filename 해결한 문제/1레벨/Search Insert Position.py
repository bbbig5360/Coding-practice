''' 
leetcode 문제 

평균적으로 속도 빠른 순서 : searchInsert2 -> searchInsert1

searchInsert1 : 기존의 이진탐색 + 후처리
searchInsert2 : 한번에 마치는 조건으로 변경

당연하게도 한번에 마치는 조건이 더 빠르게 끝납니다.
'''

class Solution:
    def searchInsert1(self, nums, target):
        l, r = 0, len(nums)
                
        while l < r:
            mid = (r+l)//2
            val = nums[mid]
            if val > target:
                r = mid
            elif val == target:
                return mid
            else:
                l = mid+1

        if nums[mid] < target:
            mid += 1        
        elif nums[mid-1] < target:
            pass
        else:
            mid = mid -1 if mid > 0 else 0
        return mid

    def searchInsert2(self, nums, target):
        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            if val < target:
                l = mid + 1
            elif val > target:
                r = mid - 1
            else:
                return mid
            
        return l     


from time import time

cmp_list = range(1,1000, 3)

print('가장 앞 숫자')
st = time()
for i in range(1000000):
    Solution().searchInsert1(cmp_list,0)
print('first_time = ', time()-st)    

st = time()
for i in range(1000000):
    Solution().searchInsert2(cmp_list,0)
print('sec_time = ', time()-st)    


print()
print('가장 뒷 숫자')
st = time()
for i in range(1000000):
    Solution().searchInsert1(cmp_list,1000)
print('first_time = ', time()-st)    

st = time()
for i in range(1000000):
    Solution().searchInsert2(cmp_list,1000)
print('sec_time = ', time()-st)    


print()
print('중간 숫자1')
st = time()
for i in range(1000000):
    Solution().searchInsert1(cmp_list,500)
print('first_time = ', time()-st)    

st = time()
for i in range(1000000):
    Solution().searchInsert2(cmp_list,500)
print('sec_time = ', time()-st)    


print()
print('중간 숫자2')
st = time()
for i in range(1000000):
    Solution().searchInsert1(cmp_list,548)
print('first_time = ', time()-st)    

st = time()
for i in range(1000000):
    Solution().searchInsert2(cmp_list,548)
print('sec_time = ', time()-st)    