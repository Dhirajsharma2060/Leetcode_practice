class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_len=len(s)
        t_len=len(t)
        sp=tp=0
        while sp<s_len and tp<t_len:
            if s[sp]==t[tp]:
                sp+=1
            tp+=1

        return sp==len(s)            

        