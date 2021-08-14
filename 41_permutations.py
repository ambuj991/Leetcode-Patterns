
def permute( nums) :
        result =  []
        if len(nums) == 1:
            return [nums[:]]
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = permute(nums)
            
            for perm in perms:
                perm.append(n)
                print(perm)
            result.extend(perms)
            print(result,'---')
            nums.append(n)
        return result
print(permute([1, 2, 3]))