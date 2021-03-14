from collections import defaultdict


class String:

    def k_minus_one_distinct_substring(self, s: str, k: int):
        """
        Approach: Two Pointers
        I/P: s = "awaglk", k = 4
        O/ P: [awag]
        All Possible:
        [awag, wagl, aglk]
        :param s:
        :param k:
        :return:
        """
        left = right = 0
        mapper = defaultdict(int)
        ans = set()
        while right < len(s):
            char = s[right]
            mapper[char] += 1
            if right - left + 1 == k:
                if len(mapper) == k - 1:
                    ans.add(s[left: right + 1])
                mapper[s[left]] -= 1
                if mapper[s[left]] <= 0:
                    del mapper[s[left]]
                left += 1
            right += 1
        return list(ans)


if __name__ == "__main__":
    string = String()
    print(string.k_minus_one_distinct_substring("awaglk", 4))