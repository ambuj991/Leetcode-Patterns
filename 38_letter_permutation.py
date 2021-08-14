
def letterCasePermutation(s):
        output = ['']
        for c in s:
            t = []
            if c.isalpha():
                    t.append(o+c.lower())
                    t.append(o+c.upper())
                    
            else:
                for o in output:
                    t.append(o+c)
            print(t)
            output = t
        return output


print (letterCasePermutation("a1b2"))