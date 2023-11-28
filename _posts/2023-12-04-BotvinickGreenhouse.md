---
title: Learning Dynamics on Invariant Measures Using PDE-Constrained Optimization
speaker:
  name: Jonah Botvinick-Greenhouse
  affil: Cornell Center for Applied Mathematics
  url: 
---

Standard data-driven techniques for learning dynamical systems struggle when observational data has been sampled slowly and state derivatives cannot be accurately estimated. To address this challenge, we assume that the available measurements reliably describe the asymptotic statistics of the dynamical process in question, and we instead treat invariant measures as inference data. We reformulate the velocity learning as a PDE-constrained optimization problem by viewing invariant measures as stationary distributional solutions to the Fokker-Planck equation, which is discretized via an upwind finite volume scheme. The velocity is parameterized by fully-connected neural networks, and we use the adjoint-state method along with backpropagation to efficiently perform model identification. Numerical results for the Van der Pol Oscillator and Lorenz-63 system, as well as real-world applications to Hall-effect thrusters and temperature prediction, are presented to demonstrate the effectiveness of the proposed approach.
