class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return list(map(s.find, s)) == list(map(t.find, t))        