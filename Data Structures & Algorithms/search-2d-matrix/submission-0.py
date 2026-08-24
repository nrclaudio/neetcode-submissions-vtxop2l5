class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first find the row, then find the column

        L, R = 0, len(matrix) - 1
        while L <= R:
            M = int((R + L) / 2)
            if matrix[M][0] > target:
                for num in matrix[M]:
                    if num == target:
                        return True
                R = M - 1
            elif matrix[M][0] < target:
                for num in matrix[M]:
                    if num == target:
                        return True
                L = M + 1
            else:
                return True
        return False
        