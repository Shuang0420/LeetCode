'''
About hashmap:
- Do not use dict.keys! 
In Python 2 dict.keys() creates the whole list of keys first that's why it is an O(N) operation, while key in dict is an O(1) operation.
>>> dic = dict.fromkeys(range(10**5))
>>> %timeit 10000 in dic
1000000 loops, best of 3: 170 ns per loop
>>> %timeit 10000 in dic.keys()
100 loops, best of 3: 4.98 ms per loop
>>> %timeit 10000 in dic.iterkeys()
1000 loops, best of 3: 402 us per loop
>>> %timeit 10000 in dic.viewkeys()
1000000 loops, best of 3: 457 ns per loop
'''
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
        if self.hashmap.has_key(number):
            self.hashmap[number]+=1
        else:
            self.hashmap[number]=1
        # self.hashmap[number]=self.hashmap.get(number,0)+1

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