# https://leetcode.com/problems/flatten-nested-list-iterator/
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        """
        :type nestedList: List[NestedInteger]
        """
        def flatten(l):
            for x in l:
                if x.isInteger():
                    # the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.
                    yield x.getInteger()
                else:
                    #  it feels unnecessary to specify that we wish to iterate over generator and yield the values. This is where yield from comes in
                    # same as for i in flatten(x.getList()): yield i
                    yield from flatten(x.getList())
                    
        self.flatList = flatten(nestedList) # generator object
        self.cur = None
    
    def next(self) -> int:
        if self.cur is not None:
            ans = self.cur
            self.cur = None
            return ans
        else:
            return next(self.flatList)
    
    def hasNext(self) -> bool:
        try:
            self.cur = next(self.flatList)
            return True
        except StopIteration:
            return False
    
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())