'''
속도 : middleNode2가 조금 더 빠름

middleNode1 : 노드 끝까지 가서 노드의 개수 확인 후 절반의 노드만 이동 후 반환
middleNode2 : 1스텝, 2스텝 노드를 만들어 2스텝 노드가 끝날 때 1스텝 노드를 반환. 1스텝씩 이동하면 절반만 이동해 절반의 값이 나옴

middleNode1는 (N + N/2) 만큼 걸리고, middleNode2는 N/2 만큼 걸리기 때문에 개수가 많아진다면 확실한 차이가 날 것으로 예상됩니다.

'''

import math
from copy import deepcopy

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode1(self, head):
        cnt = 0
        tmp_head = deepcopy(head)
        while tmp_head.next != None:
            cnt += 1
            tmp_head = tmp_head.next
            
        for i in range(math.ceil(cnt//2)):
            head = head.next
            
        return head

    def middleNode2(self, head):
        fast = head
        slow = deepcopy(fast)
                
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next    
        return slow

from time import time

start =ListNode(1)
tmp1 = ListNode(2)
tmp2 = ListNode(3)
tmp3 = ListNode(4)
tmp4 = ListNode(5)

start.next = tmp1
tmp1.next = tmp2
tmp2.next = tmp3
tmp3.next = tmp4

st = time()
for i in range(50000):
    Solution().middleNode1(start)
print('1st time = ',time()-st)

st = time()
for i in range(50000):
    Solution().middleNode2(start)
print('2cd time = ',time()-st)
print()

tmp5 = ListNode(6)
tmp6 = ListNode(7)
tmp7 = ListNode(8)
tmp8 = ListNode(9)
tmp9 = ListNode(10)
tmp10 = ListNode(11)

tmp4.next = tmp5
tmp5.next = tmp6
tmp6.next = tmp7
tmp7.next = tmp8
tmp8.next = tmp9
tmp9.next = tmp10

print('노드 개수 추가')
st = time()
for i in range(50000):
    Solution().middleNode1(start)
print('1st time = ',time()-st)

st = time()
for i in range(50000):
    Solution().middleNode2(start)
print('2cd time = ',time()-st)