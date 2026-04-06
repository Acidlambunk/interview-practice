from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s_map = defaultdict(list)
        output = []
        for i in strs:
            key = tuple(sorted(i))
            s_map[key].append(i)
        
        for j in s_map.values():
            output.append(j)
        return output
