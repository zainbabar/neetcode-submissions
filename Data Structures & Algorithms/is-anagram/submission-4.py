from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_seen = defaultdict(int)
        t_seen = defaultdict(int)
        if len(s) != len(t):
            return False
        
        for c1, c2 in zip(s, t):
            s_seen[c1] += 1
            t_seen[c2] += 1
        
        return s_seen == t_seen

