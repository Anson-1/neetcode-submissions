class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for array in matrix:
            if(target in array):
                return True
        return False

        