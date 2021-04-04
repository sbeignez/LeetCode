class MyCircularQueue:

    # MyCircularQueue(k) Initializes the object with the size of the queue to be k.
    def __init__(self, k: int):
        self.size = k
        self.empty = -1

        # create a list with -1 as default value
        self.data = [self.empty for n in range(k)]
    
        self.head = 0
        self.tail = 0


    # boolean enQueue(int value) Inserts an element into the circular queue. Return true if the operation is successful.
    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False
        elif self.isEmpty():
            self.data[self.tail % self.size] = value
        else:
            self.tail += 1
            self.data[self.tail % self.size] = value
        return True
        
    # boolean deQueue() Deletes an element from the circular queue. Return true if the operation is successful.
    def deQueue(self) -> bool:
      
        if self.isEmpty():
            return False
        else:
            self.data[self.head % self.size] = self.empty
            if not self.head == self.tail:
                self.head += 1
            return True
        
    # int Front() Gets the front item from the queue. If the queue is empty, return -1.
    def Front(self) -> int:

        if self.isEmpty():
            return self.empty
        else:
            return self.data[self.head % self.size]
        
    # int Rear() Gets the last item from the queue. If the queue is empty, return -1.
    def Rear(self) -> int:

        if self.isEmpty():
            return self.empty
        else:
            return self.data[self.tail % self.size] 


    # boolean isEmpty() Checks whether the circular queue is empty or not.
    def isEmpty(self) -> bool:

        return self.data[self.head % self.size] == self.empty


    # boolean isFull() Checks whether the circular queue is full or not.
    def isFull(self) -> bool:
        return ((self.tail + 1) % self.size) == (self.head % self.size)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()