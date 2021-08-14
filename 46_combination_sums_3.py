def combinationSum3( k: int, n: int):
        res = []
        def backtrack(num, curr, target):
            if len(curr) == k and target == 0:
                res.append(curr[:])
                return
            if target < 0 or len(curr) == k:
                return 
            for i in range(num+1, 10 ):
                curr.append(i)
                backtrack(i, curr, target - i)
                curr.pop()
        backtrack(0, [], n)
        return res

print(combinationSum3(3, 9))