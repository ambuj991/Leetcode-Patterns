class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        n, m = r-1, 0
        while n>=0 and m<c:
            if matrix[n][m] == target:
                return True
            elif matrix[n][m] < target:
                m=m+1
            else:
                n=n-1
        return False
        