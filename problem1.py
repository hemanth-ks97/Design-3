# Time Complexity : 
    # next() -> O(1)
    # hasNext() -> O(h) h: max depth of nesting in input

# Space Complexity : O(n)

# Did this code successfully run on Leetcode : YES
# Any problem you faced while coding this : NO



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
        self.next_el = None
        self.stack = []
        it = iter(nestedList)
        self.stack.append(it)
    
    def next(self) -> int:
        return self.next_el.getInteger()
    
    def hasNext(self) -> bool:
        if not self.stack:
            return False
        try:
            self.next_el = next(self.stack[-1])
            if self.next_el.isInteger():
                return True
            else:
                it = iter(self.next_el.getList())
                self.stack.append(it)
                return self.hasNext()
        
        except StopIteration:
            self.stack.pop()
            return self.hasNext()

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())