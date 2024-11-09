import time
# Recursive with memoization

memo = {}

def fib_recursive(num):
    if num in memo.keys():
        return memo[num]
    
    if num<=2:
        res = 1
    else:
        res = fib_recursive(num-1) + fib_recursive(num-2)
    
    memo[num] = res
    return res
 
start = time.time()   
print(fib_recursive(50))
finish = time.time()

print(finish-start)