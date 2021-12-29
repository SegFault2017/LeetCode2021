#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:

    def sorting(self, s1: str, s2: str) -> bool:
        """ Strategy 1: one string will be a permutation of another if both 
        strings contain the same characters and the same frequency of characters.
        Runtime: O(nlogn + (m -n)mlog(m)), where n is the length of s1, and m is 
        the length of s2.
        Space:O(max(n,m))

        Args:
            s1 (str): list of characters
            s2 (str): list of characters

        Returns:
            bool: determine whether the permutation of s1 is a substring of s2.
        """

        n, m = len(s1), len(s2)
        if n > m:
            return False

        sorted_s1 = sorted(s1)
        for i in range(m-n+1):
            if sorted_s1 == sorted(s2[i:i+n]):
                return True
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.sorting(s1, s2)

# @lc code=end
