# https://leetcode.com/problems/design-circular-deque/description/
# 641. Design Circular Deque
from collections import deque

class MyCircularDeque:

    def __init__(self, k: int):
        self.dq = deque(maxlen=k)
        

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.dq.appendleft(value)
            return True
        else:
            return False
        
    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.dq.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        value = self.dq.popleft()
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        value = self.dq.pop()
        return True

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.dq[0]
        else:
            return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.dq[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if len(self.dq) == 0:
            return True
        else:
            return False
        

    def isFull(self) -> bool:
        length = len(self.dq)
        if length == self.dq.maxlen:
            return True
        else:
            return False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()