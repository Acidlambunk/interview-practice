class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #hash set
        #sliding window
        l, total = 0,0
        length = []
        for r , j in enumerate(s):
            
            while j in set(length):
                length.remove(s[l])
                l += 1
            length.append(j)
            total = max(total, r - l +1)
        return total

