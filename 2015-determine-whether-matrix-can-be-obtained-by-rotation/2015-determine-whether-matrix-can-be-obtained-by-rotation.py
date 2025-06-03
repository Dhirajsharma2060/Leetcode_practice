class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(matrix):
            n = len(matrix)
            result = [[0]*n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    result[j][n - i - 1] = matrix[i][j]
            return result
        
        for _ in range(4):  # Try all 4 rotations
            if mat == target:
                return True
            mat = rotate(mat)
        return False