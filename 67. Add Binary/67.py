class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = 0
        num2 = 0
        for i, j in enumerate(a):
            num1 += int(j) * 2 ** (len(a) - i - 1)
        for i, j in enumerate(b):
            num2 += int(j) * 2 ** (len(b) - i - 1)    
        sol = bin(num1 + num2).split("0b")
        return str(sol[1])