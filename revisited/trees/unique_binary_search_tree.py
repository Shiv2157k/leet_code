class TreeNode:
    def __init__(self, val: int, left:int=None, right: int=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:

    def determine_unique_(self, n: int) -> int:
        """
        Approach: Mathematical Deduction
        Time Complexity: O(N)
        Space Complexity: O(1)
        Formulae: Catalan Number
        Cn = 2 * (2n + 1) / n + 2
        :param n:
        :return:
        """
        C = 1
        for i in range(n):
            C = C * 2 * (2 * i + 1)/ (i + 2)
        return int(C)

    def determine_unique(self, n: int) -> int:

        memo = {-1: 1, 0: 1}

        def bst(left, right):

            if right - left + 1 in memo:
                return memo[right - left + 1]

            sum = 0
            for i in range(left, right + 1):
                left_count = bst(left, i - 1)
                right_count = bst(i + 1, right)

                sum += left_count * right_count
            memo[right - left + 1] = sum
            return sum

        return bst(0, n - 1)


if __name__ == "__main__":

    bst = BinaryTree()
    print(bst.determine_unique(3))
    print(bst.determine_unique_(3))