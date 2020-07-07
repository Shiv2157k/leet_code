from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Trees:

    def generate_trees(self, n: int) -> List[TreeNode]:
        """
        Approach: Recursion
        Time Complexity: O(4^n / n ^ 1/2)
        Space Complexity: O(4^n / n ^ 1/2)
        :param n:
        :return:
        """

        def generate(left: int, right: int) -> List[TreeNode]:
            # Base Case
            if left > right:
                return [None, ]

            all_trees = []
            for i in range(left, right + 1):

                left_trees = generate(left, i - 1)
                right_trees = generate(i + 1, right)

                for l in left_trees:
                    for r in right_trees:
                        current_tree = TreeNode(i)
                        current_tree.left = l
                        current_tree.right = r
                        all_trees.append(current_tree)
            return all_trees

        return generate(1, n) if n else []

    def number_of_unique_bst(self, n: int) -> int:
        """
        Approach: DP
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        :param n:
        :return:
        """

        G = [0] * (n + 1)
        G[0], G[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]

    def number_of_unique_bst(self, n: int) -> int:
        """
        Approach: Mathematical Deduction
        Formulae: G(n + 1) = 2 * (2n + 1) / (n + 2)
        Time Complexity: O(n)
        Space Complexity: O(1)
        :param n:
        :return:
        """
        C = 1
        for i in range(0, n):
            C = C * 2 * (2 * i + 1) / (i + 2)
        return int(C)


if __name__ == "__main__":
    tree = Trees()
    print(tree.generate_trees(3))
    print(tree.number_of_unique_bst(3))