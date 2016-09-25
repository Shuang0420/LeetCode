import collections
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dictionary=collections.defaultdict(set)
        dic=zip([self.helper(key) for key in dictionary],dictionary)
        for key,value in dic:
            self.dictionary[key].add(value)

    def helper(self,key):
        if len(key)<3:
            return key
        return key[0]+str(len(key)-2)+key[-1]

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbrev=self.helper(word)
        if len(self.dictionary[abbrev])==0:
            return True
        return len(self.dictionary[abbrev])==1 and word==list(self.dictionary[abbrev])[0]
        


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")