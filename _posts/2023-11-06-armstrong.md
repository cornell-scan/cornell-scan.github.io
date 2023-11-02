---
title: The Randomized Golub-Klema-Stewart Algorithm
speaker:
  name: Robin Armstrong
  affil: Cornell Center for Applied Mathematics 
  url: 
---

Modern problems in scientific computing often give rise to matrices which are too large to be manipulated using the classical algorithms of numerical linear algebra. Low-rank approximation is a technique wherein a large matrix is compressed into a much smaller subspace, thereby enabling computations which would otherwise be prohibitively expensive. Interpolative decompositions, which compress a matrix into the span of a small row or column subset, are particularly useful for computing low-rank approximations that preserve matrix structures such as sparsity or nonnegativity. This talk introduces the randomized Golub-Klema-Stewart (RGKS) algorithm, an efficient randomized procedure for computing interpolative decompositions of large matrices. RGKS combines two well-studied algorithmic primitives, namely the randomized SVD and rank-revealing QR factorizations. After motivating and explaining the details of RGKS, we will show numerical experiments which compare its accuracy and efficiency to that of preexisting low-rank approximation algorithms. We will also present an error analysis of RGKS, where the main challenge is to account for the effects of randomization.

