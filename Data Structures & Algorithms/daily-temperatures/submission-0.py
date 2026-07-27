class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            for n,j in enumerate(temperatures[i:]):
                current = temperatures[i]
                if j > current:
                    result.append(n)
                    break
            else:
                result.append(0)
        return result
        