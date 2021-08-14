def generateAbbreviations( word):
        res=[]
        n = len(word)
        def dfs(path, pos, cnt):
            if pos == n:
                path = path +(str(cnt) if cnt else '')
                res.append(path)
                return
            dfs(path +(str(cnt) if cnt else '') + word[pos], pos+1, 0)
            dfs(path, pos+1, cnt+1)
        dfs('', 0, 0)
        return res
        
print(generateAbbreviations('word'))