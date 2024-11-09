import time
# Dynamic Programming

def fib_dp(num):
    
    memo = {}
    
    for i in range(1,num+1):
        if i <= 2:
            memo[i] = 1
        else:
            memo[i] = memo[i-1] + memo[i-2]
            
    return memo[num]
 
start = time.time()   
print(fib_dp(50))
finish = time.time()

print(finish-start)