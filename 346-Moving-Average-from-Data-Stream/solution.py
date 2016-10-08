'''
Solution:
- maintain a deque of at most 'size' length, for each next call, enque the number, calculate average, check if the length of deque is 3, if it is, popleft, and finally return the average. Time complexity O(n); Space complexity O(size)

Follow-up:
- make it O(1), save the sum each time, that is for each next call, enque the number, add to global sum, calculate average, check if the length of deque is 3, if it is, pop left, minus popped number from sum, and finally return the average.
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
        self.sum=0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.q.append(val)
        self.sum+=val
        avg=self.sum/float(len(self.q))
        if len(self.q)==self.size:
            self.sum-=self.q.popleft()
        return avg
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)