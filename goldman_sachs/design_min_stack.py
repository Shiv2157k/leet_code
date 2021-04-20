class MinStack:

    """
    Approach: Two Stack Optimized
    Time Complexity: O(1) for all operations
    Space Complexity: O(N)
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val < self.min_stack[-1][0]:
            self.min_stack.append([val, 1])

        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] += 1

    def pop(self) -> None:

        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1] -= 1

        if self.min_stack[-1][-1] == 0:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def get_min(self) -> int:
        return self.min_stack[-1][0]


if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-1)
    min_stack.push(9)
    print(min_stack.get_min())
    print(min_stack.top())

