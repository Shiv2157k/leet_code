from typing import List


class Combination:

    def get_combination_sum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Back Tracking
        :param candidates:
        :param target:
        :return:
        """
        if not candidates or min(candidates) > target:
            return []
        candidates.sort()
        combinations = []
        self.back_track(candidates, 0, target, [], combinations)
        return combinations

    def back_track(self, candidates, index, target, path, combinations):

        # base case
        if target == 0 and path not in combinations:
            combinations.append(path)
            return  # back track
        if target < 0 or index > len(candidates):
            return  # back track

        for candidate in range(index, len(candidates)):
            self.back_track(candidates,
                            candidate,
                            target - candidates[candidate],
                            path + [candidates[candidate]],
                            combinations
                            )

    def get_combination_sum_(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Approach: Dynamic Programming
        :param candidates:
        :param target:
        :return:
        """
        cache = {0: [[]]}

        for candidate in candidates:
            for tar in range(candidate, target + 1):
                if tar - candidate in cache:
                    if tar not in cache:
                        cache[tar] = []
                    for combination in cache[tar - candidate]:
                        cache[tar].append(combination + [candidate])
        return cache[target] if target in cache else []


if __name__ == "__main__":
    combinations = Combination()
    print(combinations.get_combination_sum([2, 3, 6, 7], 7))
    print(combinations.get_combination_sum_([2, 3, 6, 7], 7))




