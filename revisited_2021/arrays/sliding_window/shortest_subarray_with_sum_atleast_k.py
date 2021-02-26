from typing import List


class Array:

    def shortest_sub_array_with_sum_at_least_k(self, A: List[int], K:int) -> int:
        """
        Approach: Sliding Window
        Time Complexity:
        Space Complexity:
        :param A:
        :param K:
        :return:
        """
        P = [0]
        for x in A:
            P.append(P[-1] + x)
        ans = len(A) + 1
        from collections import deque
        dq = deque()
        for y, Py in enumerate(P):
            while dq and Py <= P[dq[-1]]:
                dq.pop()
            while dq and Py - P[dq[0]] >= K:
                ans = min(ans, y - dq.popleft())
            dq.append(y)
        return ans if ans < len(A) + 1 else -1


if __name__ == "__main__":
    array = Array()
    print(array.shortest_sub_array_with_sum_at_least_k([2, -1, 2, 3], 1))
    print(array.shortest_sub_array_with_sum_at_least_k([2, -1, 2, 2], 3))