from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        output = []
        finished = []
        for num, freq in counter.items():
            output.append((num,freq))
        sorted_s = sorted(output, key = lambda x: x[1],reverse = True)
        for num, freq in sorted_s[:k]:
            finished.append(num)
        return finished

           

            
            