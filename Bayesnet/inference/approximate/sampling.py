import numpy as np

# Generate new samples
def sampling(X=[], P=[], size=1):
  genList = np.random.uniform(0, 1, size)
  n = len(P)
  lowerP = np.dot(P, np.tri(n, n, -1).T)
  clf_matrix = genList.reshape(len(genList), 1) - lowerP.reshape(1, len(lowerP))
  clf_idx = np.apply_along_axis(lambda x: len(x[x >= 0]) - 1, 1, clf_matrix)

  return np.array(X)[clf_idx]