---
title: Multilevel Riemannian optimization for low-rank problems
speaker:
  name: Bart Vandereycken
  affil: Mathematics, Universite de Geneve
  url: https://www.unige.ch/math/vandereycken/
---

Large-scale optimization problems arising from the discretization of problems involving PDEs sometimes admit solutions that can be well approximated by low-rank matrices. In this talk, we will explain how to exploit this low-rank approximation property by solving the optimization problem directly over the set of low-rank matrices. In particular, we introduce a new multilevel algorithm, where the optimization variable is constrained to the Riemannian manifold of fixed-rank matrices. In contrast to most other multilevel low-rank algorithms where the rank is chosen adaptively on each level, we can keep the ranks (and thus the computational complexity) fixed throughout the iterations. Furthermore, classical implementations of line searches based on Wolfe conditions allow computing a solution where the numerical accuracy is limited to about the square root of the machine epsilon. Here, we propose an extension to Riemannian manifolds of the line search of Hager and Zhang, which uses approximate Wolfe conditions that allow computing a solution on the order of the machine epsilon. Numerical experiments demonstrate the computational efficiency of the proposed framework. Joint work with Marco Sutti.
