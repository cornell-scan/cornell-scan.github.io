---
title: Animating elastic rods with sound
speaker:
  name: Eston Schweickart
  affil: CS, Cornell
  url: http://www.cs.cornell.edu/~ers/
---

In virtual environments, creating realistic animations of objects encompasses not only generating plausible motions and visualizations, but often obtaining synchronized sounds as well. Within the field of computer graphics, modern sound generation methods can sonify a wide range of physics-based animation of solid objects, resolving vibrations and sound radiation from various structures. However, long and thin objects, commonly referred to as elastic rods, are an important computer animation primitive for which prior sound synthesis methods are ill-suited for several reasons: large displacements, nonlinear vibrations, dispersion effects, and the geometrically singular nature of rods. 

In this talk, I will describe physically based methods for simultaneous generation of animation and sound for deformable rods. I will introduce an efficient acoustic radiation method based on dipoles, and show how to tie it to existing elastic rod simulation frameworks that are commonly used within computer graphics. I will present several examples of our results, including challenging scenes involving thousands of highly coupled frictional contacts.
