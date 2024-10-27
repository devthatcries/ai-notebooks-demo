def dotProduct(vectorX, vectorY):
  if (len(vectorX) != len(vectorY)):
    return "Please use same length vectors"

  product = 0
  for i in range(0, len(vectorX)):
    product += (vectorX[i] * vectorY[i])
  return product