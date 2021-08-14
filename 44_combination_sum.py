class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(curr, i , total):
            if total == target:
                res.append(curr[:])
                return
            if (i >= len(candidates)) or total > target:
                return
            curr.append(candidates[i])
            dfs(curr, i, total+ candidates[i])
            curr.pop()
            dfs(curr, i+1 , total)
        dfs([], 0, 0)
        return res
            