class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        return list(map(pattern.find, pattern)) == list(map(words.index, words))