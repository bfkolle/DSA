class Stack:
    """A stack data structure"""

    _capacity = 1000

    def __init__(self):
        self._list = []

    def push(self, item):
        if len(self._list) != self._capacity:
            self._list.insert(0, item)

    def pop(self):
        self._list.remove(self._list[0])

    def peek(self):
        return None if self.isEmpty() else self._list[0]

    def isEmpty(self):
        return len(self._list) == 0

    def isFull(self):
        return len(self._list) == self._capacity