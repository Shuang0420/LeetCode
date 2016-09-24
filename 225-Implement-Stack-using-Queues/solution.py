from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1=deque()
        self.queue2=deque()
        
    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if not self.queue2:
            self.queue2.append(x)
            while self.queue1:
                self.queue2.append(self.queue1.popleft())
            self.queue1,self.queue2=self.queue2,self.queue1
        

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue1.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.queue1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if not self.queue1:
            return True
        return False
        