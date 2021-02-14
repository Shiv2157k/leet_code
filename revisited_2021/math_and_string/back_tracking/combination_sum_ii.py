from typing import List


class Array:

    def back_track(self, candidates: List[int], index: int, target: int, path: List[int], result: List[List[int]]):
        """
        Back tracking function
        :param candidates:
        :param index:
        :param target:
        :param path:
        :param result:
        :return:
        """
        # base case
        if target == 0 and path not in result:
            result.append(path)
            return  # back track
        if target < 0 or index >= len(candidates):
            return  # back track

        for idx in range(index, len(candidates)):
            if idx > index + 1 and candidates[idx] == candidates[idx - 1]:
                continue
            self.back_track(candidates, idx + 1, target - candidates[idx], path + [candidates[idx]], result)

    def combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Back Tracking
        Time Complexity:
        Space Complexity:
        :param candidates:
        :param target:
        :return:
        """
        if not candidates or min(candidates) > target:
            return []
        candidates.sort()
        result = []
        self.back_track(candidates, 0, target, [], result)
        return result


if __name__ == "__main__":
    array = Array()
    print(array.combination_sum([10, 1, 2, 7, 6, 1, 5], 8))
