

class BST:

    def get_unique_bst_count(self, n: int) -> int:
        """
        Approach: Mathematical Deduction
        Time Complexity: O(N)
        Space Complexity: O(1)
        Formulae:
        Cn = 2(2n + 1)Cn / n + 2
        :param n:
        :return:
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i + 1) / (i + 2)
        return int(C)

    def get_unique_bst_count_(self, n: int) -> int:
        """
        Approach: DP
        Time Complexity: O(N^2)
        Space Complexity: O(N)
        Based on Catalan Number Formulae:
        Gn = n^(E)^i=0 Gi * Gn-i-1
        :param n:
        :return:
        """
        G = [0] * (n + 1)
        G[0] = G[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[-1]


if __name__ == "__main__":
    bst = BST()
    print(bst.get_unique_bst_count(3))
    print(bst.get_unique_bst_count_(3))