class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_s = sorted(set(nums))
        best = 1
        curr = 1

        for i in range(1, len(sorted_s)):
            if sorted_s[i] == sorted_s[i-1] + 1:
                curr += 1
            else:
                curr = 1
            best = max(best, curr)

        return best
