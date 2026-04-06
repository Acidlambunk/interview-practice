from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n_map = defaultdict(int)
        for i,j in enumerate(numbers):
            sisa = target - j
            if n_map[sisa]:
                return [n_map[sisa], i + 1]
            n_map[j] = i + 1
        return []