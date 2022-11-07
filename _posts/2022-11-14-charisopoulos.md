---
title: Communication-efficient distributed eigenspace estimation
speaker:
  name: Vasileios Charisopoulos
  affil: Cornell University
  url: https://vchariso.com
---

Machine learning algorithms are often deployed in *federated* environments,
where multiple machines are connected with a central coordinator and minimizing
communication is essential for high performance. To achieve this, a standard
strategy is to compute local solutions or parameter estimates on each machine
and average the results at the "central" node.

In this talk, I will focus on the task of distributed eigenspace estimation.
I will explain how naive averaging strategies break down due to the presence of
symmetries in local solutions and introduce a novel aggregation scheme resolving
these issues in a single round of communication. Building on this aggregation
scheme, I will present a communication-efficient and statistically-efficient
algorithm for distributed principal component analysis (PCA).
I will also discuss robust extensions of this method for environments where
a subset of the computing nodes may fail "silently" or respond adversarially.


This work is joint with Austin Benson and Anil Damle.
