class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openclose = { ')':'(', ']':'[','}':'{'}

        for c in s:
            if c in openclose:
                if stack and stack[-1] == openclose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        