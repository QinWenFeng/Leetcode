class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if(nums[i] == 0):
                nums.append(nums[i])
                nums.remove(nums[i])
        for i in range(len(nums)):
            if(nums[i] == 1):
                nums.append(nums[i])
                nums.remove(nums[i])           
        for i in range(len(nums)):
            if(nums[i] == 2):
                nums.append(nums[i])
                nums.remove(nums[i])  
        return nums