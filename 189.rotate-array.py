#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
from abc import abstractmethod
from typing import List


class Solution:

    def bruteForce(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        Strategy 1: Brute Force
        Runtime: O(n)
        Space: O(n)

        Args:
            nums (List[int]):  a list of integers
            k (int): rotate the array k times
        """
        n = len(nums)
        k %= n
        rotated = [0] * n

        for i in range(n):
            idx = (i + k) % n
            rotated[idx] = nums[i]

        nums[:] = rotated
        return

    def cyclicReplacement(self, nums: List[int], k: int):
        """
        Do not return anything, modify nums in-place instead.
        Strategy 1: Brute Force
        Runtime: O(n)
        Space: O(1)

        Args:
            nums (List[int]):  a list of integers
            k (int): rotate the array k times
        """

        n = len(nums)
        k %= n
        start = i = 0

        while i < n:
            current, prev = start, nums[start]
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                i += 1
                if start == current:
                    break
            start += 1
        return

    def rotate(self, nums: List[int], k: int) -> None:
        self.cyclicReplacement(nums, k)
        return


# @lc code=end
