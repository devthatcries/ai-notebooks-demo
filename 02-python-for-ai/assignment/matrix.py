from vector import dot_product

__all__ = "multiply"

def multiply(matrix_x, matrix_y):
  if not are_matrices_valid(matrix_x, matrix_y):
    return "Please enter valid matrices"

  columns = matrix_column(matrix_y)
  matrix = []
  for x in range(0, len(matrix_x)):
    vector = []
    for y in range(0, len(columns)):
        vector.append(dot_product(matrix_x[x], columns[y]))
    matrix.append(vector)

  return matrix

def are_matrices_valid(matrix_x, matrix_y) -> bool:
  are_valid = True
  for x in range(0, len(matrix_x)):
    if len(matrix_x[x]) != len(matrix_y):
      are_valid = False
  return are_valid

def matrix_column(matrix):
  columns = []
  for x in range(0, len(matrix)):
    for y in range(0, len(matrix[x])):
      vector = []
      for z in range(0, len(matrix)):
        vector.append(matrix[z][y])
      columns.append(vector)
    break
  return columns