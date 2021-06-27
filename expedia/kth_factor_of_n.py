from heapq import heappush, heappop


class KthFactor:

    def _of_n(self, n: int, k: int) -> int:
        """
        Approach: Math, O(sqrt(N)) time
        Time Complexity: O(sqrt(N))
        Space Complexity: O(min(k, sqrt(N))
        :param n:
        :param k:
        :return:
        """
        divisors = []
        sqrt_n = int(n**0.5)

        for x in range(1, sqrt_n + 1):
            if n % x == 0:
                k -= 1
                divisors.append(x)
                if k == 0:
                    return x

        # special case
        if sqrt_n * sqrt_n == n:
            k += 1

        return n // divisors[len(divisors) - k] if k <= len(divisors) else -1

    def of_n_(self, n: int, k: int) -> int:
        """
        Approach: Heap
        Time Complexity: O(sqrt(N) * log k)
        Space Complexity: O(min(k, sqrt(N))
        :param n:
        :param k:
        :return:
        """

        def heappush_k(num):
            heappush(heap, -num)
            if len(heap) > k:
                heappop(heap)

        heap = []
        for x in range(1, int(n**0.5) + 1):
            if n % x == 0:
                heappush_k(x)
                if x != n // x:
                    heappush_k(n // x)
        return -heappop(heap) if k == len(heap) else -1

    def of_n__(self, n: int, k: int) -> int:
        """
        Approach: Brute Force
        Time Complexity: O(N)
        Space Complexity: O(1)
        :param n:
        :param k:
        :return:
        """

        for i in range(1, n // 2 + 1):

            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        return n if k == 1 else -1


if __name__ == "__main__":
    kth_factor = KthFactor()
    print(kth_factor.of_n_(25, 3))
    print(kth_factor.of_n__(25, 3))
    print(kth_factor._of_n(25, 3))