'''
Solution:
- maintain a deque of at most 'size' length, for each next call, enque the number, calculate average, check if the length of deque is 3, if it is, popleft, and finally return the average. Time complexity O(n); Space complexity O(size)
'''



from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.q=deque()
        self.size=size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        avg=sum(self.q)/float(len(self.q))
        if len(self.q)==self.size:
            self.q.popleft()
        return avg
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)