# def findTargetSumWays(self, nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: int
#     """
#     dp = {} # position - (index, total) -> storing number of ways #!type(dp) = dictionary

#     def backtrack(i, total): #imp concept - backtracking, dynamic programming with caching - thats why we keep a dictionary to store the possibilities of different combinations

#         if(i == len(nums)): return 1 if total == target else 0
