class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)
        count = 0
        for i in str(bin_n):
            if(i == '1'):
                count = count + 1 
        return count