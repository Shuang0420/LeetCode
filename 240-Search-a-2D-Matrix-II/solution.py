class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        return self.helper(matrix,target,0,0,len(matrix)-1,len(matrix[0])-1)
        
        
    def helper(self,matrix,target,startX,startY,endX,endY):
        if startX>endX or startY>endY:
            return False
        midX=(startX+endX)/2
        midY=(startY+endY)/2
        mid = matrix[midX][midY]
        if mid == target:
            return True
        if mid > target:
            return self.helper(matrix,target,startX,midY,midX-1,endY) or self.helper(matrix,target,startX,startY,endX,midY-1)
        else:
            return self.helper(matrix,target,midX+1,startY,endX,midY) or self.helper(matrix,target,startX,midY+1,endX,endY)
        return False