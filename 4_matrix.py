def diagonal_difference(matrix):
   n = len(matrix)
   primary_diagonal = sum(matrix[i][i] for i in range(n))
   secondary_diagonal = sum(matrix[i][n - 1 -i] for i in range(n))
   return abs(primary_diagonal - secondary_diagonal)
 
matrix = [
[1, 2, 0],
[4, 5, 6],
[7, 8, 9]
]

result = diagonal_difference(matrix)
print(result)