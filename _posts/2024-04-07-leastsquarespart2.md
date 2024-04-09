---
layout: distill
title: Introduction to Least Squares Part 2 (Electric Boogaloo)
date: 2024-04-7
description: Why the heck do we multiply by the transpose
comments: true
importance: 3
categories: linear-algebra
authors:  
  - name: Taylor F.
    url: ""
    affiliations:
      name: None
toc:
  - name: Why is it consistent
  - name: An Application
  - name: Further Questions
---

This is a sequel to my previous post on [least squares](../leastsquares/){:target="_blank"}.

These are the questions I left at the end of that post.

1. Why is $$\mathbf{A}^T\mathbf{A}\mathbf{x}=\mathbf{A}^T\mathbf{b}$$ guaranteed a solution?
2. Why would the solution to the normal equation actually be the "closest" solution?

## Why is it consistent

Recall that a system of equations $${A}{x}={b}$$ is consistent when $$b$$ is in the image or column space of $$A$$. So the column space, $$W$$, is going to be the main character in our story today.

We know that every vector space can be decomposed as the direct sum of any subspace and its orthogonal complement. That is,

$$\mathbb{R}^n=W\oplus W^\perp$$

This means that $$b$$ can be written as $$b=w+w_\perp$$. Conceptually this can be understood as writing $$b$$ as a sum of a vector which does make a consistent system, and a vector which can knock us out of being consistent (unless $$w_\perp=0$$).

Now, recall also that the row space of a matrix $$B$$ is the orthogonal complement of the null space of $$B$$. This can be understood intuitively as if $$Bn=0$$, that means the dot product of the rows of $$B$$ and $$n$$ must be zero.

But the column space of $$A$$ is just the row space of $$A^T$$. So the orthgogonal complement of $$W$$ is the null space of $$A^T$$. Thus, $$A^Tw_\perp=0$$ and $$A^Tb=A^Tw$$. Essentially, this means that multiplying by the transpose *sort of* projects us into the column space of $$A$$ (or, at least, zeros out the part )

Since $$w$$ is by definition in the column space of $$A$$, we know $$Ax=w$$ is consistent. Let $$x=c$$ be the solution (that is, $$w=Ac$$).

So let's write out what happens when we multiply $$Ax=b$$ by $$A^T$$.

$$A^TAx=A^Tb=A^Tw=A^TAc$$

This clearly has a solution: $$x=c$$, which actually implies that the solution to $$A^TAx=A^Tb$$ is the same as the solution to $$Ax=w$$.

That is, the least squares solution is the solution to the system projected onto the column space. Which actually makes some sense intuitively. If we want the closest solution, we want it to be the solution to the system where the vector is projected orthogonally to the column space. Which answers both our questions.