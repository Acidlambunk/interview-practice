class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        snums = set(nums)
        if len(snums) < len(nums):
            return True
        else:
            return False