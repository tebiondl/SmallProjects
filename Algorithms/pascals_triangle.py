# The problem is here: https://leetcode.com/problems/pascals-triangle/description/?envType=problem-list-v2&envId=dynamic-programming

def generate(numRows):

    memo = {}
    memo[1] = [1]
    memo[2] = [1,1]
    
    for i in range(3,numRows+1):
        new_list = []
        new_list.append(1)
        for j in range(1,len(memo[i-1])):
            new_list.append(memo[i-1][j-1] + memo[i-1][j])
        new_list.append(1)
        memo[i] = new_list
    print(memo)
    
generate(7)