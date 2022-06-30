class Solution:
    def addDigits(self, num: int) -> int:
        result = int(num)
        while len(str(num)) >= 2:
            result = 0
            for i in str(num):
                result += int(i)
            num = result
        return result     