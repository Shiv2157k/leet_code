from typing import List


class Array:

    def back_track(self, candidates: List[int], index: int, target: int, path: List[int], result: List[List[int]]):
        # base case 1
        if target == 0 and path not in result:
            result.append(path)
            return # back track
        if target < 0 or index >= len(candidates):
            return # back track
        for i in range(index, len(candidates)):
            self.back_track(candidates, i, target - candidates[i], path + [candidates[i]], result)

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Back tracking
        Time Complexity: O(N^(T/M))
        Space Complexity: O(T / M)
        :param candidates:
        :param target:
        :return:
        """
        if not candidates or min(candidates) > target:
            return []
        result = []
        self.back_track(candidates, 0, target, [], result)
        return result


if __name__ == "__main__":
    array = Array()
    print(array.combination_sum([2, 3, 6, 7], 7))