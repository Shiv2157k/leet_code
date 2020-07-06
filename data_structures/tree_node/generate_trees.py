from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Trees:

    def generate_trees(self, n: int) -> List[TreeNode]:

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


if __name__ == "__main__":
    tree = Trees()
    print(tree.generate_trees(3))