class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # for each car check how many turns it takes for it to reach destination
        # cars with the same number of turns become a fleet
        # 
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)