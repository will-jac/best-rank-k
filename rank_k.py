import numpy as np
import scipy.misc
import scipy.linalg as linalg

import matplotlib.pyplot as pl

X = scipy.misc.face(gray=True).astype(np.float)
pl.gray()
pl.imshow(X)
pl.show()

U, s, Vt = linalg.svd(X)
S = linalg.diagsvd(s, X.shape[0], X.shape[1])
print(U.shape, S.shape, Vt.shape)

for k in [1, 5, 10, 25, 50]:
    print('k:', k)
    UL = U[:,0:k]
    STL = S[0:k, 0:k]
    VtL = Vt[0:k,:]
    print(UL.shape, STL.shape, VtL.shape)
    pl.imshow(np.dot(np.dot(UL, STL), VtL))
    pl.xlabel('k = ' + str(k))
    pl.show()
