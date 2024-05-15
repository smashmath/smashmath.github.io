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
  - name: Why is it the closest solution
---

\newcommand{\norm}[1]{\left\lVert#1\right\rVert}

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

This means that $$b$$ can be written *uniquely* as $$b=w+w_\perp$$, where $$w$$ is $$W$$ and $$w_\perp$$ is orthogonal to everything in $$W$$. Conceptually this can be understood as writing $$b$$ as a sum of a vector which does make a consistent system, and a vector which can knock us out of being consistent (i.e. the system is consistent if and only if $$w_\perp=0$$).

But what does it mean to be orthogonal in $$\mathbb{C}^n$$? What is the inner product? Well, like we said before, it's not as simple as just $$w\cdot v=v^Tw$$. Instead, it is $$w\cdot v=v^*w$$, which means the complex dot product is not commutative, but conjugate commutative ($$v\cdot w=\overline{w\cdot v}$$). Though, since we are only interested in orthogonality and dot products of zero, we get a sort of orthogonal symmetry/commutativity ($$v\cdot w=0\iff w\cdot v=0$$).

This does add one complication. While in $$\mathbb{R}^n$$, $$An=0$$ implies that $$n$$ is orthogonal to the rows of $$A$$, that isn't quite so in $$\mathbb{C}^n$$, since the inner product requires one vector to be conjugated. That is, while in $$\mathbb{R}^n$$, the row space is the orthogonal complement of the null space, in $$\mathbb{C}^n$$, the null space is the orthogonal complement of the conjugated row space ($$\ker(B)^\perp=\operatorname{row}(\overline{B})$$). Note that if $$B$$ is real, we do recover the result that the kernel is orthogonal to the row space.

But if we let $$B=A^*$$ in the expression above, this means the orthogonal complement of the null space of $$A^*$$ is the column space of $$A$$. That is, if a vector $$u$$ is orthogonal to the column space of $$A$$, then $$A^*u=0$$.

Thus, $$A^*w_\perp=0$$ and $$A^*b=A^*w$$. Essentially, this means that multiplying by the adjoint *sort of* projects us into the column space of $$A$$ (or, at least, zeros out the part that isn't in the column space).

Since $$w$$ is by definition in the column space of $$A$$, we know $$Ax=w$$ is consistent. Let $$x=c$$ be the solution (that is, $$w=Ac$$).

So let's write out what happens when we multiply $$Ax=b$$ by $$A^*$$.

$$A^*Ax=A^*b=A^*w=A^*Ac$$

This clearly has a solution: $$x=c$$, which actually implies that the solution to $$A^*Ax=A^*b$$ is the same as the solution to $$Ax=w$$.

That is, the least squares solution is the solution to the system projected onto the column space. Which actually makes some sense intuitively. If we want the closest solution, we want it to be the solution to the system where the vector is projected orthogonally to the column space. Which actually answers both our questions.

## Why is it the closest solution

Now, I said it answers both of our questions, but perhaps you aren't quite convinced that just because it's the solution to the system where $$b$$ has been projected into the column space. Let's see if I can change your mind.

We "measure" the "closest" solution using $$\norm{b-Ax}^2$$ (minimizing the squares of error: hence, 'least squares').

Note that by orthogonality, we can say that $$\norm{w+w_\perp}^2=\norm{w}^2+\norm{w_\perp}^2$$. But, if we rewrite

$$\norm{b-Ax}^2=\norm{w+w_\perp-Ax}^2=\norm{w-Ax}^2+\norm{w_\perp}^2$$

Notice that no matter *what* $$x$$ is, our squared error will always be $$\geq\norm{w_\perp}^2$$. This is hopefully somewhat intuitive. Since $$w_\perp$$ in a sense measures *how* inconsistent our system is, it acts as a lower bound for our error. Cool, right?

Thus, the only thing we *can* do to minimize error, is to minimize $$\norm{w-Ax}^2$$. The best we can do is making it zero. But... like we said before, $$w=Ac$$ for some $$c$$. Then, $$x=c$$ will give us zero. So $$x=c$$, the solution to $$Ax=w$$, really *is* the solution that minimizes the error!

[hyperlink](https://youtu.be/M5CeQG1YfEQ?si=2J5M9Tdyq01GVAsc){:target="_blank"}
