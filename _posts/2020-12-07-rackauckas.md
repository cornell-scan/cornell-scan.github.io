---
title: Stiffness in Scientific Machine Learning
speaker:
  name: Chris Rackauckas
  affil: Mathematics, MIT
  url: https://chrisrackauckas.com/
---

Scientific machine learning is a burgeoning discipline for mixing machine learning into scientific simulation. Use cases of this field include automated discovery of physical equations and accelerating physical simulators. However, making the analyses of this field automated will require building a set of tools that handle stiff and ill-conditioned models without requiring user tuning. The purpose of this talk is to demonstrate how the methods and tools of scientific machine learning can be consolidated to give a single high performance and robust software stack. We will start by describing universal differential equations, a flexible mathematical object which is able to represent methodologies for equation discovery, 100-dimensional differential equation solvers, and discretizations of physics-informed neural networks. Then we will showcase how adjoint sensitivity analysis on the universal differential equation solving process gives rise to efficient and stiffly robust training methodologies for a large variety of scientific machine learning problems. With this understanding of differentiable programming we will describe how the Julia SciML Software Organization is utilizing this foundation to provide high performance tools for deploying battery powered airplanes, improving the energy efficiency of buildings, allow for navigation via the Earth's magnetic field, and more.


