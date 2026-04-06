class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s_nums = sorted(set(nums))
        nums[:len(s_nums)] = s_nums
        return len(s_nums)
