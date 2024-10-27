from vector import dotProduct

__all__ = "multiply"

def multiply(A, B):
  if (not areMatricesValid(A, B)):
    return "Please enter valid matrices"

  columns = matrixColumns(B)
  matrix = []
  for x in range(0, len(A)):
    vector = []
    for y in range(0, len(columns)):
        vector.append(dotProduct(A[x], columns[y]))
    matrix.append(vector)

  return matrix

def areMatricesValid(A, B) -> bool:
  areValid = True
  for x in range(0, len(A)):
    if (len(A[x]) != len(B)):
      areValid = False
  return areValid

def matrixColumns(A):
  columns = []
  for x in range(0, len(A)):
    for y in range(0, len(A[x])):
      vector = []
      for z in range(0, len(A)):
        vector.append(A[z][y])
      columns.append(vector)
    break
  return columns