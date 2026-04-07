class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = []
        for i,n in enumerate(operations):
            if n == '+':
                total.append(int(total[-1])+int(total[-2]))
            elif n == "D":
                total.append(total[-1]*2)
            elif n == "C":
                total.pop()
            else:
                total.append(int(n))
        return sum(total)
