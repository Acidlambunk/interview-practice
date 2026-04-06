class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s_nums = sorted(nums)
        while val in s_nums:
            s_nums.remove(val)
        nums[:len(s_nums)] = s_nums
        return len(s_nums)