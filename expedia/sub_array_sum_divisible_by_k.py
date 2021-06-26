from typing import List


class Array:

    def total_sub_array_sum_div_by_k_(self, nums: List[int], k: int) -> int:
        """
        Approach: Prefix Sum
        Time Complexity: O(N)
        Space Complexity: O(N)
        Formulae:
        nC2 = n (n - 1) / 2
        :param nums:
        :param k:
        :return:
        """

        prefix_sum = 0
        counts = [0] * k

        for num in nums:
            prefix_sum += num
            counts[prefix_sum % k] += 1

        result = counts[0]
        for count in counts:
            result += (count * (count - 1)) // 2
        return result

    def total_sub_array_sum_div_by_k(self, nums: List[int], k: int) -> int:
        """
        Approach: Prefix Sum + Hash Map
        Time Complexity: O(N)
        Space Complexity: O(N)
        :param nums:
        :param k:
        :return:
        """

        prefix_sum = 0
        result = 0
        key_mapper = {0: 1}

        for num in nums:

            prefix_sum += num
            key = prefix_sum % k

            if key in key_mapper:
                result += key_mapper[key]
                key_mapper[key] += 1
                continue
            key_mapper[key] = 1
        return result


if __name__ == "__main__":
    array = Array()
    print(array.total_sub_array_sum_div_by_k([1, 2, 3, 4], 5))
    print(array.total_sub_array_sum_div_by_k([4, 5, 0, -2, -3, 1], 5))
    print(array.total_sub_array_sum_div_by_k_([1, 2, 3, 4], 5))
    print(array.total_sub_array_sum_div_by_k_([4, 5, 0, -2, -3, 1], 5))