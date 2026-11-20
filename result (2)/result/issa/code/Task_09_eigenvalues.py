import numpy as np

adjacency = np.array([[0.,1.,1.,0.],[1.,0.,1.,1.],[1.,1.,0.,1.],[0.,1.,1.,0.]])
values, vectors = np.linalg.eig(adjacency)
index = np.argmax(values.real)
centrality = np.abs(vectors[:, index].real)
centrality /= centrality.sum()
print("Eigenvalues:", values)
print("Dominant eigenvalue:", values[index].real)
print("Normalized eigenvector centrality:", centrality)
