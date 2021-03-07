import functools
from typing import List


class JobSchedule:

    def minimum_difficulty_bottom_up(self, job_difficulty: List[int], days: int) -> int:
        """
        Approach: DP Table (bottom up)
        Time Complexity: O(N^2 * D)
        Space Complexity: O(ND)
        :param job_difficulty:
        :param days:
        :return:
        """
        # base case
        jobs = len(job_difficulty)
        if jobs < days:
            return -1

        # build dp table
        dp = [[float("inf")] * jobs + [0] for _ in range(days + 1)]

        for day in range(1, days + 1):
            right = jobs - day + 1
            for cut in range(right):
                max_so_far, ans = 0, float("inf")
                for job_rate in range(cut, right):
                    max_so_far = max(max_so_far, job_difficulty[job_rate])
                    ans = min(ans, max_so_far + dp[day - 1][job_rate + 1])
                dp[day][cut] = ans
        return dp[days][0]

    def minimum_difficulty_top_down(self, job_difficulty: List[int], days: int) -> int:
        """
        Approach: DP (Memoization - top down)
        Time Complexity: O(N^2 * D)
        Space Complexity: O(ND)
        :param job_difficulty:
        :param days:
        :return:
        """
        # base case
        jobs = len(job_difficulty)
        # cannot be equally divided
        if jobs < days:
            return -1

        # hash table for memoization
        # memo = {}

        # recurrence function
        @functools.lru_cache(None)
        def dp(day: int, cut: int) -> int:
            # if (day, cut) in memo:
            #   return memo[(day, cut)]
            # base case
            # if it is a single day jus return the max
            if day == 1:
                return max(job_difficulty[cut:])
            # apply the recurrence function designed
            max_so_far, ans = 0, float("inf")
            for rate_idx in range(cut, jobs - day + 1):
                max_so_far = max(max_so_far, job_difficulty[rate_idx])
                ans = min(ans, max_so_far + dp(day - 1, rate_idx + 1))
            # memo[(day, cut)] = ans
            return ans
        return dp(days, 0)


if __name__ == "__main__":
    job_schedule = JobSchedule()
    print(job_schedule.minimum_difficulty_top_down([6, 5, 4, 3, 2, 1], 2))
    print(job_schedule.minimum_difficulty_bottom_up([6, 5, 4, 3, 2, 1], 2))
    print(job_schedule.minimum_difficulty_top_down([6, 5, 4, 3, 2, 1], 3))
    print(job_schedule.minimum_difficulty_bottom_up([6, 5, 4, 3, 2, 1], 3))
    print(job_schedule.minimum_difficulty_top_down([6, 5, 4, 3, 2, 1], 4))
    print(job_schedule.minimum_difficulty_bottom_up([6, 5, 4, 3, 2, 1], 4))
    print(job_schedule.minimum_difficulty_top_down([6, 5, 4, 3, 2, 1], 9))
    print(job_schedule.minimum_difficulty_bottom_up([6, 5, 4, 3, 2, 1], 9))