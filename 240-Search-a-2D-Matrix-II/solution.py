class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        i,j = 0,len(matrix[0])-1
        while True:
            if j<0 or i>len(matrix)-1:
                return False
            curr = matrix[i][j]
            if curr == target:
                return True
            if curr > target:
                j -= 1
            else:
                i += 1
            