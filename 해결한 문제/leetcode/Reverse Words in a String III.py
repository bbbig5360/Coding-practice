''' 
짧은 리스트에서 빠른 순서 : 1 -> 2 
  긴 리스트에서 빠른 순서 : 2 -> 1

reverseWords1 : 입력받은 문자열을 띄어쓰기 단위로 나눈 후 순서대로 새로운 리스트에 저장. 저장하기 전에 단어의 순서를 거꾸로 만듭니다.
reverseWords2 : reverseWords1을 list comprehension을 사용해서 처리

결과 : 입력값이 커질수록 comprehension을 사용했을 경우 속도가 빠릅니다.
'''

class Solution:
    def reverseWords1(self, s):
        ret = []
        for word in s.split():
            ret.append(word[::-1])
        return ' '.join(ret)

    def reverseWords2(self, s):
        return ' '.join([ x[::-1] for x in s.split(" ") ])


from time import time
inputData = 'God Ding'
print(f'{len(inputData)}크기의 문자열 처리 비교')
st = time()
for i in range(1000000):
    Solution().reverseWords1(inputData)
print('1st time = ',time()-st)

st = time()
for i in range(1000000):
    Solution().reverseWords2(inputData)
print('2nd time = ',time()-st)
print()


inputData = 'God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding God Ding '
print(f'{len(inputData)}크기의 문자열 처리 비교')
st = time()
for i in range(100000):
    Solution().reverseWords1(inputData)
print('1st time = ',time()-st)

st = time()
for i in range(100000):
    Solution().reverseWords2(inputData)
print('2nd time = ',time()-st)
print()

inputData = """Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest 
Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take Lee
tCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest 
Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take Lee
tCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest 
Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take Lee
tCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest Let's take LeetCode contest """

print(f'{len(inputData)}크기의 문자열 처리 비교')
st = time()
for i in range(100000):
    Solution().reverseWords1(inputData)
print('1st time = ',time()-st)

st = time()
for i in range(100000):
    Solution().reverseWords2(inputData)
print('2nd time = ',time()-st)
print()