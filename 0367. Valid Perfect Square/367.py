class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num in [x * x for x in range(1, 2 ** 16)]:
            return True
        return False