class Solution:
    def findMin(self, nums: List[int]) -> int:
        max_rot = len(nums)
        L , R = 0, max_rot - 1
        while L < R:
            M = (L + R) // 2
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M
        return nums[L]
                