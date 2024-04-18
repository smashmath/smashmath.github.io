---
layout: distill
title: Introduction to Least Squares Part 2 (Electric Boogaloo)
date: 2024-04-15
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
---

This is a very short sequel to my previous post on [least squares](../leastsquares/){:target="_blank"}.

These are the questions I left at the end of that post (in the more general complex form).

1. Why is $$\mathbf{A}^*\mathbf{A}\mathbf{x}=\mathbf{A}^*\mathbf{b}$$ guaranteed a solution?
2. Why would the solution to the normal equation actually be the "closest" solution?

When I say "dot product" here, I mean the general euclidean inner product on $$\mathbb{C}^n$$, where we multiply by the *conjugate* transpose (adjoint) rather than the regular transpose. 

$$\langle w,v\rangle=v^*w=\left(\overline{v}\right)^Tw$$

Note that if we talk about $$\mathbb{R}^n$$, then the adjoint is just, of course, the regular transpose.

If you need a reminder for why we need the *conjugate*, it's because complex numbers get weird when you just square them:

$$\begin{pmatrix}1&i\end{pmatrix}\begin{pmatrix}1\\i\end{pmatrix}=1^2+i^2=0$$

So we can't just say $$w\cdot v=v^Tw$$ and call it a day if we want to be as general as possible. But you are more than welcome to just interpret $$v^*$$ as the transpose, and assume we're talking in terms of real vectors (my complex compulsion prevents me from doing so).

## Why is it consistent

Recall that a system of equations $${A}{x}={b}$$ is consistent when $$b$$ is in the image or column space of $$A$$. So the column space, $$W$$, is going to be the main character in our story today.

We know that every vector space can be decomposed as the direct sum of any subspace and its orthogonal complement. That is,

$$\mathbb{C}^n=W\oplus W^\perp$$

This means that $$b$$ can be written as $$b=w+w_\perp$$. Conceptually this can be understood as writing $$b$$ as a sum of a vector which does make a consistent system, and a vector which can knock us out of being consistent (unless $$w_\perp=0$$).

Now, recall also that the row space of a matrix $$B$$ is the orthogonal complement of the null space of $$B$$. This can be understood intuitively as if $$Bn=0$$, that means the dot product of the rows of $$B$$ and $$n$$ must be zero.

But the column space of $$A$$ is just the row space of $$A^*$$. So the orthgogonal complement of $$W$$ is the null space of $$A^*$$. Thus, $$A^*w_\perp=0$$ and $$A^*b=A^*w$$. Essentially, this means that multiplying by the adjoint (transpose) *sort of* projects us into the column space of $$A$$ (or, at least, zeros out the part )

Since $$w$$ is by definition in the column space of $$A$$, we know $$Ax=w$$ is consistent. Let $$x=c$$ be the solution (that is, $$w=Ac$$).

So let's write out what happens when we multiply $$Ax=b$$ by $$A^*$$.

$$A^*Ax=A^*b=A^*w=A^*Ac$$

This clearly has a solution: $$x=c$$, which actually implies that the solution to $$A^*Ax=A^*b$$ is the same as the solution to $$Ax=w$$.

That is, the least squares solution is the solution to the system projected onto the column space. Which actually makes some sense intuitively. If we want the closest solution, we want it to be the solution to the system where the vector is projected orthogonally to the column space. Which actually answers both our questions.

[hyperlink](https://youtu.be/M5CeQG1YfEQ?si=2J5M9Tdyq01GVAsc){:target="_blank"}