def solve(nums, target):
    d={}
    for i ,item in enumerate((nums)):
        if target-item in d:
            return [d[target-item], i]
        d[item] = i
