class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.hashmap=dict()

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.hashmap[number]=self.hashmap.get(number,0)+1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if not self.hashmap:
            return False
        for v in self.hashmap:
            if value-v in self.hashmap:
                if self.hashmap[v]>1 or v!=value-v:
                    return True
        return False
        

# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)