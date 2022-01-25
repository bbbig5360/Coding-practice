class Solution:
    def reverseString1(self, s):
        s.reverse()
        return s
    def reverseString2(self, s):
        return s[::-1]
    def reverseString3(self, s):
        return list(reversed(s))
        

# print( Solution().reverseString1(cmp_list) )
# print(list(reversed(cmp_list)))

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