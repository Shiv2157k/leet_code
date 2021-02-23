from heapq import heapify, heappush, heappop


class String:

    def re_organize(self, string: str) -> str:
        """
        Approach: Sorting using Heap Queue
        Time Complexity: O(N log A)
        N -> length of string
        A -> size of alphabet
        Space Complexity: O(A)
        :param string:
        :return:
        """
        # exhaust higher frequency 1st
        # Edge Cases:
        # 1. Make sure you have at least two items in heap queue.
        # 2. If the last item in the heap has frequency greater than 1
        # return empty string since we cannot organize it.
        if not string:
            return ""

        hq = [(-string.count(ch), ch) for ch in set(string)]
        heapify(hq)
        organized_string = ""
        while len(hq) > 1:
            f1, c1 = heappop(hq)
            f2, c2 = heappop(hq)

            organized_string += c1
            organized_string += c2

            if abs(f1) > 1:
                heappush(hq, (f1 + 1, c1))
            if abs(f2) > 1:
                heappush(hq, (f2 + 1, c2))

        if hq:
            f, c = heappop(hq)
            return "" if abs(f) > 1 else organized_string + c
        return organized_string


if __name__ == "__main__":
    st = String()
    print(st.re_organize("aba"))
    print(st.re_organize("aabbcc"))
    print(st.re_organize("bb"))

