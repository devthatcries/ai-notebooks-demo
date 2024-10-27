from vector import dotProduct

__all__ = "multiply"

def multiply(A, B):
  if (not areMatricesValid(A, B)):
    return "Please enter valid matrices"

  matrix = []
  for x in range(0, len(A)):
    vector = []
    for y in range(0, len(A)):
      column = []
      for z in range(0, len(B)):
        column.append(B[z][y])
      vector.append(dotProduct(A[x], column))
    matrix.append(vector)

  return matrix

def areMatricesValid(A, B) -> bool:
  areValid = True
  for x in range(0, len(A)):
    if (len(A[x]) != len(B)):
      areValid = False
  return areValid