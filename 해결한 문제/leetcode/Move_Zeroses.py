''' 
짧은 리스트에서 빠른 순서 : 2 -> 4 -> 1 -> 3
  긴 리스트에서 빠른 순서 : 4 -> 3 -> 2 -> 1

moveZeroes1 : 0인 숫자의 개수를 받아 해당 개수만큼 앞에서부터 0을 지우고(remove), 뒤에 0을 채우는(append) 방식
moveZeroes2 : 위의 방법과 같은데, 0의 개수를 내장함수로(.count()) 받는 방법
moveZeroes3 : 처음부터 끝까지 1단계씩 진행하는데, 0이 아닌 숫자가 나오면 0인 자리와 값을 변경하는 방법(swap)
moveZeroes4 : 0이 아닌 숫자들만 받아오고(append), 0의 개수만큼 마지막에 추가(append)

짧은 코드에서는 2번이 가장 빨랐지만, Remove가 O(N)인만큼 0의 개수가 많아지면 속도가 느려집니다.

'''

class Solution:
    def moveZeroes1(self, nums):
        zeroes_cnt = 0
        for i in nums:
            if i == 0:
                zeroes_cnt += 1

        for i in range(zeroes_cnt):
            nums.remove(0)
            nums.append(0)
    
    def moveZeroes2(self, nums):
        for i in range(nums.count(0)):
            nums.remove(0)
            nums.append(0)

    def moveZeroes3(self, nums):
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                

    def moveZeroes4(self, nums):
        n_zero_lst = []
        for i in nums:
            if i != 0:
                n_zero_lst.append(i)

        for i in range(nums.count(0)):
            n_zero_lst.append(0)
        nums = n_zero_lst


Solution().moveZeroes4([0,1,0,3,12])

from time import time
cmp_list = [0,1,0,3,12]

st = time()
for i in range(500000):
    Solution().moveZeroes1(cmp_list)
print('1st_time = ', time()-st)    

st = time()
for i in range(500000):
    Solution().moveZeroes2(cmp_list)
print('2nd_time = ', time()-st)

st = time()
for i in range(500000):
    Solution().moveZeroes3(cmp_list)
print('3rd_time = ', time()-st)    

st = time()
for i in range(500000):
    Solution().moveZeroes4(cmp_list)
print('4th_time = ', time()-st)    

print()
print('Long List')    
cmp_list = [0,1,0,3,12,100,12,0,9,3,5,1,0,123,4,6,0,3,21,0,2,1,0,0]

st = time()
for i in range(500000):
    Solution().moveZeroes1(cmp_list)
print('1st_time = ', time()-st)    

st = time()
for i in range(500000):
    Solution().moveZeroes2(cmp_list)
print('2nd_time = ', time()-st)

st = time()
for i in range(500000):
    Solution().moveZeroes3(cmp_list)
print('3rd_time = ', time()-st)    

st = time()
for i in range(500000):
    Solution().moveZeroes4(cmp_list)
print('4th_time = ', time()-st)    