class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Map each position to the time it takes to reach the target
        times = {p: (target - p) / s for p, s in zip(position, speed)}
        
        fleets = 0
        slowest_time_ahead = 0.0
        
        # Sort positions in descending order (evaluate cars closest to target first)
        for p in sorted(times.keys(), reverse=True):
            time = times[p]
            
            # If this car takes longer than the fleet ahead of it, 
            # it will never catch up. It becomes the leader of a new fleet.
            if time > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time
                
        return fleets
        