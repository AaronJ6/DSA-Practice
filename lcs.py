# A Naive recursive Python implementation of LCS problem
def lcs(X, Y, m, n):

	if m == 0 or n == 0:
		return 0
	elif X[m-1] == Y[n-1]:
		return 1 + lcs(X, Y, m-1, n-1);
	else:
		return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n));


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print ("Length of LCS is ", lcs(X , Y, len(X), len(Y)) )

# A Top-Down DP implementation of LCS problem

# Returns length of LCS for X[0..m-1], Y[0..n-1]
def lcs(X, Y, m, n, dp): #!with memorization

	if (m == 0 or n == 0):
		return 0

	if (dp[m][n] != -1):
		return dp[m][n]

	if X[m - 1] == Y[n - 1]:
		dp[m][n] = 1 + lcs(X, Y, m - 1, n - 1, dp)
		return dp[m][n]

	dp[m][n] = max(lcs(X, Y, m, n - 1, dp),lcs(X, Y, m - 1, n, dp))
	return dp[m][n]

# Driver code

X = "AGGTAB"
Y = "GXTXAYB"

m = len(X)
n = len(Y)
dp = [[-1 for i in range(n + 1)]for j in range(m + 1)]

print(f"Length of LCS is {lcs(X, Y, m, n, dp)}")

# This code is contributed by shinjanpatra
