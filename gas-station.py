def canCompleteCircuit(gas, cost) -> int:
    length = len(gas)
    dp = [0] * len(gas)
    
    for i in range(length):
        dp[i] = gas[i] - cost[i]

    if sum(dp) < 0:
        return -1

    for i in range(length):
        if dp[i] >= 0:
            tank = 0
            
            for j in range(i, length):
                tank += dp[j]
                if tank < 0:
                    break
            
            if tank >= 0:
                for j in range(0, i):
                    tank += dp[j]
                    if tank < 0:
                        break

            if tank >= 0:
                return i

    return -1
    

print(canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(canCompleteCircuit([2, 3, 4], [3, 4, 3]))