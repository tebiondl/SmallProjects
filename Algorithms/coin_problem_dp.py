# We have diffeent types of coins = [1,4,5]
# And we have an amount = 13
# I have to find the combination with the lowest amount of coins that sum up the amount required

import copy

def coin_problem(amount, coins):
    
    memo = {}
    memo[0] = []
    
    for i in range (1, amount + 1):
        # Solve sub problem i
        for coin in coins:
            val = i - coin
            if val < 0:
                continue
            else:
                change = -1
                if i not in memo.keys():
                    change = float('inf')
                else:
                    change = len(memo[i])
                
                if len(memo[val]) + 1 < change:
                    memo[i] = memo[val][:]
                    memo[i].append(coin)
                
    return memo[amount]
    
print(coin_problem(13, [1,4,5]))