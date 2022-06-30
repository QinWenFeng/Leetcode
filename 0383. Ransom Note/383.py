class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rlist = []
        mlist = []
        for i in ransomNote:
            rlist.append(i)
        for j in magazine:
            mlist.append(j)   
        r_len = 0
        for k in rlist:
            if(k in mlist):
                r_len = r_len + 1
                mlist.remove(k)
        if(len(rlist) == r_len):
            return True
        else:
            return False