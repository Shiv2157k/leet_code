import functools
from typing import List


class JobScheduler:

    def minimum_difficulty_bottom_up(self, job_difficulty: List[int], days: int) -> int:
        """
        Approach: Bottom Up/ DP
        Time Complexity: O(N^2 * D)
        Space Complexity: O(ND)
        :param job_difficulty:
        :param days:
        :return:
        """
        total_jobs = len(job_difficulty)
        # base case
        if total_jobs < days:
            return -1

        dp = [[float("inf")] * total_jobs + [0] for _ in range(days + 1)]

        for day in range(1, days + 1):
            right = total_jobs - day + 1
            for cut in range(right):
                max_so_far = 0
                answer = float("inf")
                for j in range(cut, right):
                    max_so_far = max(max_so_far, job_difficulty[j])
                    answer = min(answer, max_so_far + dp[day - 1][j + 1])
                dp[day][cut] = answer
        return dp[days][0]

    def minimum_difficulty_recursive(self, job_difficulty: List[int], days: int) -> int:
        """
        Approach: Top Down
        Time Complexity: O(N^2 * D)
        Space Complexity: O(ND)
        :param job_difficulty:
        :param days:
        :return:
        """
        # dp(day, i) = from ith job difficulty,
        # we want to find minimum of sub of maximum
        # difficulties of each day i.e., each sub array

        # ans = dp(d, 0)

        # recurrence relation
        # min(max(jb[j: n - d + 1] + dp(d - 1, j + 1)))

        total_jobs = len(job_difficulty)
        # base case
        # less number of jobs than days
        # Which we can't possibly split those into each day.
        if len(job_difficulty) < days:
            return -1
        # memo = {}

        @functools.lru_cache(None)
        def dp(day: int, cut: int) -> int:
            # base case
            # if (day, cut) in memo:
            #    return memo[(day, cut)]
            if day == 1:
                return max(job_difficulty[cut:])
            max_so_far = 0
            ans = float("inf")
            for job in range(cut, total_jobs - day + 1):
                max_so_far = max(max_so_far, job_difficulty[job])
                ans = min(ans, max_so_far + dp(day - 1, job + 1))
            # memo[(day, cut)] = ans
            return ans
        return dp(days, 0)


if __name__ == "__main__":
    job_scheduler = JobScheduler()
    print(job_scheduler.minimum_difficulty_bottom_up(
        [6, 5, 4, 3, 2, 1], 2
    ))
    print(job_scheduler.minimum_difficulty_bottom_up(
        [9, 9, 9], 4
    ))
    print(job_scheduler.minimum_difficulty_bottom_up(
        [1, 1, 1], 3
    ))
    print(job_scheduler.minimum_difficulty_bottom_up(
        [7, 1, 7, 1, 7, 1], 3
    ))
    print(job_scheduler.minimum_difficulty_bottom_up(
        [11, 111, 22, 222, 33, 333, 44, 444], 6
    ))
