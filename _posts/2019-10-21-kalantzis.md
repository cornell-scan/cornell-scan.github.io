---
title: Domain decomposition Rayleigh-Ritz approaches for symmetric generalized eigenvalue problems
speaker:
  name: Vassilis Kalantzis
  affil: IBM Research
  url:  https://www-users.cs.umn.edu/~kalan019/
---

In this talk we discuss a parallel domain decomposition Rayleigh-Ritz
projection scheme to compute a selected number of eigenvalues (and, optionally,
associated eigenvectors) of large and sparse symmetric pencils.  The projection
subspace associated with interface variables is built by computing a few of the
eigenvectors and associated leading derivatives of a zeroth-order approximation
of the non-linear matrix-valued interface operator. On the other hand, the
projection subspace associated with interior variables is built independently
in each subdomain by exploiting local eigenmodes and matrix resolvent
approximations. The sought eigenpairs are then approximated by a Rayleigh-Ritz
projection onto the subspace formed by the union of these two subspaces. Our
numerical experiments demonstrate the efficiency of the proposed technique on
sequential/distributed memory architectures as well as its competitiveness
against schemes such as shift-and-invert Lanczos, and Automated MultiLevel
Substructuring combined with p-way vertex-based partitionings.
