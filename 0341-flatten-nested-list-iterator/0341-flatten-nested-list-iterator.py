class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = []
        for item in reversed(nestedList):
            self.stack.append(item)

    def next(self):
        self._flatten()
        return self.stack.pop().getInteger()

    def hasNext(self):
        self._flatten()
        return bool(self.stack)

    def _flatten(self):
        while self.stack and not self.stack[-1].isInteger():
            nested_list = self.stack.pop()
            for item in reversed(nested_list.getList()):
                self.stack.append(item)
