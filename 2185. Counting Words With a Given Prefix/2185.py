class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len(re.findall('\s' + pref, ' ' + ' '.join(words)))