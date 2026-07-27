class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)
        for i, n in enumerate(temperatures):
            while stack and n > temperatures[stack[-1]]:
                past_day = stack.pop()
                wait = i - past_day
                results[past_day] = wait
            stack.append(i)
        return results