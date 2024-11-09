# the problem is here: https://leetcode.com/problems/climbing-stairs/description/?envType=problem-list-v2&envId=dynamic-programming

def climbStairs(n):
    
    memo = {}
    memo[0] = 0
    memo[1] = 1
    
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
        
    return memo[n]

print(climbStairs(6))
            