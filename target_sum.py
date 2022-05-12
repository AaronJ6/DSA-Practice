from collections import defaultdict

def findTargetSumWays(nums, target): #!NEETCODE method
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    dp = {} # position - (index, total) -> storing number of ways #!type(dp) = dictionary

    def backtrack(i, total): #imp concept - backtracking, dynamic programming with caching - thats why we keep a dictionary to store the possibilities of different combinations

        if(i == len(nums)): 
            if total == target:
                return 1 
            else:
                return 0
        if(i,total) in dp:
            return dp[(i,total)]
        dp[(i,total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
        return(dp[(i,total)])

    return(backtrack(0,0))


"""     dp = defaultdict(int) #!COMMENT section answer - this builds the decision tree on a dictionary and gets the answer
    dp[0] = 1

    for num in nums:
        new_dp = defaultdict(int)
        print(dp)
        for n in dp:
            print(n)
            new_dp[n+num] += dp[n]
            new_dp[n-num] += dp[n]
            print(new_dp)
        dp = new_dp """

def main():
    nums = [1,1,1,1,1]
    target = 3
    op = findTargetSumWays(nums, target)
    print(op)

if __name__ == "__main__":
    main()