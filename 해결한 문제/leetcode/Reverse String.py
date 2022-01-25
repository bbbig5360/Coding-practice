''' 
짧은 리스트에서 빠른 순서 : 1 -> 2 -> 3
  긴 리스트에서 빠른 순서 : 1 -> 2 -> 3

reverseString1 : 리스트 내장함수 reverse()사용
reverseString2 : 슬라이싱 사용 [::-1]
reverseString3 : reversed() 사용

리스트의 길이가 짧다면 슬라이싱도 나쁘지않지만, 리스트의 크기가 커질수록 내장함수의 성능이 압도적으로 좋음
'''

class Solution:
    def reverseString1(self, s):
        s.reverse()
        return s
    def reverseString2(self, s):
        return s[::-1]
    def reverseString3(self, s):
        return list(reversed(s))
        

from time import time
cmp_list = list('hello')

st = time()
for i in range(1000000):
    Solution().reverseString1(cmp_list)
print('1st time = ',time()-st)

st = time()
for i in range(1000000):
    Solution().reverseString2(cmp_list)
print('2nd time = ',time()-st)

st = time()
for i in range(1000000):
    Solution().reverseString3(cmp_list)
print('3rd time = ',time()-st)
print()

print('Long list')
cmp_list = list('''hellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohello
hellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohell
ohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohel
lohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohe
llohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohelloh
ellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohello
hellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohell
ohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohel
lohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohe
llohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohellohelloh''')

st = time()
for i in range(1000000):
    Solution().reverseString1(cmp_list)
print('1st time = ',time()-st)

st = time()
for i in range(1000000):
    Solution().reverseString2(cmp_list)
print('2nd time = ',time()-st)

st = time()
for i in range(1000000):
    Solution().reverseString3(cmp_list)
print('3rd time = ',time()-st)
print()