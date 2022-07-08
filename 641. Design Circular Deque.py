class MyCircularDeque:
    
    def __init__(self, k: int): 
        self.que = deque([])
        self.max_size = k

    def insertFront(self, value: int) -> bool:
        if len(self.que) < self.max_size:
            self.que.appendleft(value)
            return True
        else:
            return False

    def insertLast(self, value: int) -> bool:
        if len(self.que) < self.max_size:
            self.que.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.que:
            self.que.popleft()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.que:
            self.que.pop()
            return True
        else:
            return False

    def getFront(self) -> int:
        if self.que:
            return self.que[0]
        else:
            return -1 

    def getRear(self) -> int:
        if self.que:
            return self.que[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.que:
            return False
        else:
            return True

    def isFull(self) -> bool:
        return len(self.que) == self.max_size