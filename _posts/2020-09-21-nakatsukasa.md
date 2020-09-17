---
title: Fast and stable randomized low-rank matrix approximation
speaker: 
  name: Yuji Nakatsukasa
  affil: Mathematics, University of Oxford
  url: https://people.maths.ox.ac.uk/nakatsukasa/
---

Randomized SVD has become an extremely successful approach for efficiently computing a low-rank approximation of matrices. In particular the paper by Halko, Martinsson, and Tropp (SIREV 2011) contains extensive analysis, and has made it a very popular method. The typical complexity for a rank-r approximation of mxn matrices is O(mnlog n+(m+n)r^2) for dense matrices. The classical Nystrom method is much faster, but only applicable to positive semidefinite matrices. This work studies a generalization of Nystrom's method applicable to general matrices, and shows that (i) it has near-optimal approximation quality comparable to competing methods, (ii) the computational cost is the near-optimal O(mnlog n+r^3) for dense matrices, with small hidden constants, and (iii) crucially, it can be implemented in a numerically stable fashion despite the presence of an ill-conditioned pseudoinverse. Numerical experiments illustrate that generalized Nystrom can significantly outperform state-of-the-art methods, especially when r>>1, achieving up to a 10-fold speedup. The method is also well suited to updating and downdating the matrix. 

