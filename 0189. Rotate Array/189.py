class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        while(count < k):
            nums.insert(0, nums[len(nums) - count - 1])
            count = count + 1
        count = 0
        while(count < k):
            nums.pop()
            count = count + 1       