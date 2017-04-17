---
title: Dynamic "factoring" techniques
speaker:
  name: Alex Vladimirsky
  affil: Math, Cornell
  url: http://www.math.cornell.edu/~vlad/
---

Theoretical results on accuracy of numerical schemes for differential
equations are built on specific assumptions about the level of
solution smoothness/regularity.  But if a physically relevant solution
is singular, this can severely degrade the convergence rates of
"standard" numerical methods.  When the exact location & type of
singularity are known in advance, we can use the "factoring"
techniques to circumvent this difficulty.  The idea is to rewrite the
original solution as a product (or a sum) of two functions: the first
is chosen to have the exact right type of singularity at that
location; the second is (at least locally) smooth but unknown and we
recover it by solving a modified equation.

We will illustrate this idea for ODE initial value problems and
Eikonal PDEs with a point source.  In the latter case, the
"rarefaction fan" of characteristics yields a localized blow-up in
second derivatives of the solution and decreases the rate of
convergence even for simple (first-order upwind) discretizations.

However, rarefaction fans can also result from general (inhomogeneous)
boundary conditions or discontinuities in coefficients of the
equation.  This talk will present a method for "dynamic factoring" in
2-dimensional Eikonal problems.  The goal is to treat rarefaction fans
as they are discovered in the process of solving the PDE on the grid.

Joint work with Dongping Qi (SJTU-Cornell).
