
def setZeroes( matrix):
        row = [False]*len(matrix)
        col = [False] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
             
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == True or col[j] == True:
                    matrix[i][j] = 0
        return matrix
        

arr =[
  [0, 0],
  [1, 0]
]

print( setZeroes(arr))