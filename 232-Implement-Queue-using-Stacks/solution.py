class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1=list()
        self.stack2=list()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.helper()
        return self.stack2.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.helper()
        element=self.stack2.pop()
        self.stack2.append(element)
        return element
    
    def empty(self):
        """
        :rtype: bool
        """
        if self.stack1 or self.stack2:
            return False
        return True
        
    def helper(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        