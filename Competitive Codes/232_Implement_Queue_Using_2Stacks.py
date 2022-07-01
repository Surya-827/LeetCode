class MyQueue:
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, x: int) -> None:
        self.stackA.append(x)

    def pop(self) -> int:
        if self.stackB == []:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

    def peek(self) -> int:
        return self.stackA[0] if self.stackB == [] else self.stackB[-1]

    def empty(self) -> bool:
        return self.stackA == [] and self.stackB == []