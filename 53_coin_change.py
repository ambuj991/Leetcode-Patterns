# dp

import sys
def coinChange( coins, amount):
        arr = [0] * (amount+1)
        for i in range(1, len(arr)):
            arr[i] = (sys.maxsize)
            for j in range(len(coins)):
                if i-coins[j] >= 0:
                    res = arr[i-coins[j]]
                    if res != sys.maxsize:
                        arr[i] = min(arr[i] , res+1)

        return arr[-1] if arr[-1]!= sys.maxsize else -1
                    
print(coinChange([1,2,5], 11))