class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        m = len(matrix) # row
        n = len(matrix[0]) # column
        
        start = 0
        end = m*n-1
        while start <= end:
            mid = (start+end)/2
            if matrix[mid/n][mid%n] == target:
                return True
            if matrix[mid/n][mid%n] > target:
                end = mid-1
            else:
                start = mid+1
        return False
            
        


        