class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a_c = Counter(s)
        a_t = Counter(t)
        if a_t == a_c:
            return True
        return False