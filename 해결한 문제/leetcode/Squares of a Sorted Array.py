class Solution:
    def sortedSquares(self, nums):
        return sorted([ x**2 for x in nums])
        