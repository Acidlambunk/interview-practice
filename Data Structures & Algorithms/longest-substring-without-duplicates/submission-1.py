class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #hash set
        #sliding window
        l, total = 0,0
        char_set = set()
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            total = max(total, r - l +1)
        return total

