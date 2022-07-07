class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        min_num = 1000000
        for i in nums:
            if(abs(min_num) > abs(i)):
                min_num = i
            if(abs(min_num) == abs(i) and i > 0):
                min_num = i
        return min_num