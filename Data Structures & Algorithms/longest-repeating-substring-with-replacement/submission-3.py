from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        max_f , l = 0, 0
        output = 0
        for r , j in enumerate(s):
            counter[j] += 1
            max_f = max(max_f, counter[j])
            print(max_f)
            while (r - l + 1) - max_f > k:
                counter[s[l]] -= 1
                l += 1
            output = max(output, r - l +1)
            print(output)
        return output

