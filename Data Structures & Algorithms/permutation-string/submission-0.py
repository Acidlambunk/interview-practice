from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = Counter()
        counter = Counter(s1)
        l = 0
        for r in range(len(s2)):
            window[s2[r]] += 1
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                l += 1
            if r - l + 1 == len(s1) and window == counter:
                return True
        return False