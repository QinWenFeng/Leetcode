class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = 0
        for i, j in enumerate(digits):
            nums += int(j) * 10 ** (len(digits) - i - 1)
        return list(str(nums + 1))