from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        window = Counter()
        need = len(target)
        have = 0
        l = 0
        best_len = float('inf')
        best = (-1,-1)
        for r in range(len(s)):
            window[s[r]] += 1
            if s[r] in target and window[s[r]] == target[s[r]]:
                have += 1
            while have == need:
                if r - l +1 < best_len:
                    best_len = r - l + 1
                    best = (l, r + 1)
                window[s[l]] -= 1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -= 1
                l += 1
        return "" if best_len == float('inf') else s[best[0]:best[1]]
                