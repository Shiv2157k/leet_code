from typing import List


class Box:

    def optimized_weights(self, arr: List[int]) -> List[int]:
        """
        Approach: Greedy
        :param arr:
        :return:
        """
        total = sum(arr)
        arr.sort()
        right_sum = 0
        res = []
        r = len(arr) - 1
        while right_sum < total:
            right_sum += arr[r]
            total -= arr[r]
            res.append(arr[r])
            r -= 1
        reversed(res)
        return res


if __name__ == "__main__":
    box = Box()
    print(box.optimized_weights([5, 3, 2, 4, 1, 2]))