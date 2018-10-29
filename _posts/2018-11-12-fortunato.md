---
title: Efficient operator-coarsening multigrid schemes for local discontinuous Galerkin methods
speaker:
  name: Daniel Fortunato
  affil: SEAS, Harvard
  url: 
---

An efficient hp-multigrid scheme is presented for local discontinuous Galerkin (LDG) discretizations of elliptic problems, formulated around the idea of separately coarsening the underlying discrete gradient and divergence operators. We show that traditional multigrid coarsening of the primal formulation leads to poor and suboptimal multigrid performance, whereas coarsening of the flux formulation leads to optimal convergence and is equivalent to a purely geometric multigrid method. The resulting operator-coarsening schemes do not require the entire mesh hierarchy to be explicitly built, thereby obviating the need to compute quadrature rules, lifting operators, and other mesh-related quantities on coarse meshes. We show that good multigrid convergence rates are achieved in a variety of numerical tests on 2D and 3D uniform and adaptive Cartesian grids, as well as for curved domains using implicitly defined meshes and for multi-phase elliptic interface problems with complex geometry. Extension to non-LDG discretizations is briefly discussed.
