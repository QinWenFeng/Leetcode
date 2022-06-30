class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        nums.append(len(nums))
        for i in range(len(nums)):
            if(nums[i] != i):
                return i
        return len(nums)-1