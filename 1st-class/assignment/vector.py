def dot_product(vector_x, vector_y):
  if len(vector_x) != len(vector_y):
    return "Please use same length vectors"

  product = 0
  for i in range(0, len(vector_x)):
    product += (vector_x[i] * vector_y[i])
  return product