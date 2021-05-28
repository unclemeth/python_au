class MyQueue:

    def __init__(self):
        self.stack_f = []
        self.stack_s = []

    def shift(self):
        while self.stack_f:
            self.stack_s.append(self.stack_f.pop())

    def push(self, x: int) -> None:
        self.stack_f.append(x)

    def pop(self) -> int:
        if len(self.stack_s) != 0:
            return self.stack_s.pop()
        self.shift()
        return self.stack_s.pop()

    def peek(self) -> int:
        if len(self.stack_s) == 0:
            self.shift()
        return self.stack_s[-1]

    def empty(self) -> bool:
        if len(self.stack_f) + len(self.stack_s) == 0:
            return True
        return False