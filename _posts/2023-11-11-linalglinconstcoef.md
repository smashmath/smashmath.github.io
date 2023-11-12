---
layout: distill
title: The Linear Algebra Perspective of Linear Constant Coefficient ODEs
date: 2023-11-11
description: No more "guessing". This way is intuitive.
comments: true
importance: 1
tags: best
category: differential-equations
authors:  
  - name: Taylor Grant
    url: ""
    affiliations:
      name: None
toc:
  - name: Linear Algebra Recap
    subsections:
      - name: Linear Transformations
      - name: Eigenvectors
      - name: Linear Operators and Polynomials
  - name: The Differential Operator
  - name: The Most Important ODE
  - name: Second Order. Two Independent Solutions
  - name: Repeated Roots
    subsections:
      - name: Exponential Shift
      - name: Exponential Shift Into Overdrive
  - name: Complex Stuff
---

Last year, I made a post about [this same topic](../linconstcoef/){:target="_blank"}, but since then, I have developed a new way of understanding this topic through the lens of linear algebra which makes many of the seemingly arbitrary choices seem almost stupidly obvious. As someone who loves linear algebra and differential equations, I am often talking about it with my friends. One time, I was discussing differential equations with a friend of mine who was taking a class in it at the time. He asked me, "why do we know that the solutions to these equations *have* to be exponentials?" My explanation was not great, but years later I presented the following explanation which I think was much better. In his words, it was "mindblowing". I'm hoping you will feel similarly. **It does, however, require linear algebra.**

We will address the following questions in the context of constant coefficient linear ordinary differential equations:

1. Why is our guess for the solution $$e^{rt}$$?
2. Why does a second order equation have exactly two linearly independent homogeneous solutions?
3. Why do we multiply by $$t$$ when we have a repeated root of the characteristic polynomial?

And as a bonus, I'm going to explain why the **exponential response formula** is actually absurdly trivial!

# Linear Algebra Recap

Let us review some basic linear algebra facts and terminology.

A **subspace** is a nonempty subset of a vector space that is closed under linear combinations.

## Linear Transformations

A linear transformation $$T$$, is a function that preserves linear combinations.

\begin{equation}
T(c_1x_1+\ldots+c_kx_k)=c_1T(x_1)+\ldots+c_kT(x_k)
\end{equation}

If $$T(x)=y$$, then we say that $$y$$ is the **image** of $$x$$ under $$T$$ (often, we just say the image of $$x$$). The image is unique because $$T$$ is a function. We call $$x$$ the **preimage** of $$y$$ under $$T$$. A preimage is not necessarily unique.

If the image of an element $$x$$ is $$0$$ ($$T(x)=0$$), then we say that $$x$$ is in the **kernel** of $$T$$ ($$x\in\ker(T)$$). The kernel is the set of all preimages of $$0$$. We sometimes call the kernel the set of all **homogeneous solutions** to the equation $$T(x)=0$$. The kernel is a subspace.

The **image** of $$T$$ is the set of all possible images. It is essentially the "range" of the transformation. The image is also a subspace.

### Preimage Theorem
Assume the equation $$T(x)=b$$ (which is asking the question "what are all the preimages of b?") has at least one solution, $$x=x_p$$. Then *every* solution is of the form $$x=x_p+x_h$$ where $$x_h$$ is an element in $$\ker(T)$$. That is, **all preimages of a linear transformation are off from a single particular preimage by something in the kernel**.

**Proof:** If $$x_0$$ is a vector of the form $$x_0=x_p+x_h$$, then $$T(x_0)=T(x_p+x_h)=T(x_p)+T(x_h)=b+0=b$$. Hence, $$x_0$$ is also a preimage of $$b$$, showing that any vector of this form is also a solution.

Suppose we have some other solution $$x_1$$. Then $$T(x_1-x_p)=T(x_1)-T(x_p)=b-b=0$$. Hence, $$x_1-x_p\in\ker(T)$$, so $$x_1-x_p=x_h$$ for some $$x_h\in\ker(T)$$, and thus $$x_1=x_p+x_h$$, concluding the proof.

## Eigenvectors

An **eigenvector** of $$T$$ is a nonzero vector $$v$$ for which $$T$$ just scales $$v$$. That is, $$T(v)=\lambda v$$ for some $$\lambda\in F$$. $$\lambda$$ is called the **eigenvalue** of $$v$$. Note that this means that

$$(T-\lambda I)v=0\implies v\in\ker(T-\lambda I)$$

As a very mundane but useful fact, if the eigenvalue of $$v$$ is nonzero, then we can just divide both sides of $$T(v)=\lambda v$$ by $$\lambda$$ to get that $$T\left(\frac{v}{\lambda}\right)=v\implies\frac{v}{\lambda}$$ is an easy preimage of $$v$$.

\begin{equation}\label{divide}
T(v)=\lambda v\neq0\implies T\left(\frac{v}{\lambda}\right)=v
\end{equation}

Another important fact is that $$T^n(v)=\lambda^n v$$.

We call the set of all eigenvectors with eigenvalue $$\lambda$$ the **eigenspace of $$\lambda$$**. The **generalized eigenspace of $$\lambda$$** is the set of all generalized eigenvectors which we denote $$E_\lambda$$. Recall that generalized eigenvectors are all vectors $$w$$ for which

$$(T-\lambda I)^kw=0$$

for some integer $$k$$.

## Linear Operators and Polynomials

Given a polynomial $$p(x)=a_0+a_1x+\ldots+a_nx^n$$, we define

\begin{equation}
p(T)=a_0I+a_1T+\ldots+a_nT^n\implies p(T)x=a_0x+a_1T(x)+\ldots+a_nT^n(x)
\end{equation}

Here are some insanely important facts

1. If $$v$$ is an eigenvector of $$T$$ with eigenvalue $$\lambda$$, then $$v$$ is also an eigenvector of $$p(T)$$ with eigenvalue $$p(\lambda)$$ (this is a very good thing to prove, and it's a very short proof). However, $$P(T)$$ can have eigenvectors that are not eigenvectors of $$T$$. One example is that $$\begin{pmatrix}1\\0\end{pmatrix}$$ is an eigenvector of $$J=\begin{pmatrix}\lambda&1\\0&\lambda\end{pmatrix}$$, but $$\begin{pmatrix}0\\1\end{pmatrix}$$ is an eigenvector of $$(J-\lambda I)^2=\begin{pmatrix}0&0\\0&0\end{pmatrix}$$ and not of $$J$$.
2. The kernel is just a subset of the eigenspace of $$0$$. That is, finding the kernel of an operator can be done by finding all eigenvectors with eigenvalue zero.
3. 

# The Differential Operator

We are going to focus in on the differential operator $$D$$ defined by

\begin{equation}
Dy=y'
\end{equation}

This is a linear operator by the linearity of differentiation. That is, by the fact that we can pull out constants from derivatives, and that the derivative of a sum is just the sum of derivatives.

Okay, so now, let's bring everything we talked about above together:

The differential equation

\begin{equation}
a_ny^{(n)}+\ldots+a_1y'+a_0y=g(t)
\end{equation}

is just the equation $$p(D)y=g(t)$$, where $$p(x)=a_nx^n+\ldots+a_1x+a_0$$. That is, we are looking for preimages of $$g(t)$$ under $$p(D)$$, and every solution will be of the form $$y=y_p+y_h$$ whewere $$y_p$$ is some preimage of $$g(t)$$, and $$y_h$$ is an eigenvector of $$p(D)$$ with eigenvalue zero (it is in the kernel of $$p(D)$$). Note that because the kernel is always a subspace, this gives us the superposition property of homogeneous solutions for free.

If we find an expression for $$y$$ such that it encompasses every solution, then we call it the **general solution**. To do so, we need a basis of the kernel $$\{y_1,\ldots,y_n\}$$ such that any solution $$y$$ can be written as

$$y=y_p+c_1y_1+\ldots+c_ny_n$$

So how can we start to find a basis for the kernel? Well, we can start with eigenvectors of $$D$$ with eigenvalue $$\lambda$$ such that $$p(\lambda)=0$$. And there we go: the characteristic polynomial is now something extremely obvious, and we have yet to even *mention* exponentials.

So now we are looking for functions $$y$$ such that $$Dy=\lambda y$$.

# The Most Important ODE

\begin{equation}
y'=ay
\end{equation}

Yeah, I said it.

Now, let's try to solve this. Well, this differential equation says that the rate of change is proportional to the value of the function. With proportionality constant

$$\frac{y'}{y}=a$$

If $$y=0$$, then this is trivially true. So we can accept that $$y=0$$ is a possible solution, and assume that $$y\neq0$$ to get the others. But, wait. $$\frac{y'}{y}=\frac{d}{dt}\ln\left\lvert y \right\rvert$$. So $$\frac{d}{dt}\ln\left\lvert y \right\rvert=a$$. That is,

$$\ln\left\lvert y \right\rvert=at+c\implies \left\lvert y \right\rvert=e^ce^{at}$$

$$\implies y=Ce^{at}\implies y\in\operatorname{span}(e^{at})$$

Remember, $$y\in\operatorname{span}(e^{at})$$ just means that $$y$$ is some linear combination of $$e^{at}$$, which just means $$y=c_1e^{at}$$.

We have demonstrated that $$y'=ay\implies y\in\operatorname{span}(e^{at})$$, and I encourage you to verify that $$y'=ay\impliedby y\in\operatorname{span}(e^{at})$$. However, how do we *know* this provides us with *every* solution? No, get that Picard–Lindelöf s#!% out of here (it's beautiful, yes, but not particularly intuitive). Suppose we have two solutions $$y_1,y_2$$ with $$y_1\neq0$$. Then

$$\frac{d}{dt}\left(\frac{y_2}{y_1}\right)=\frac{y_1y_2'-y_2y_1'}{y_1^2}$$

$$=\frac{y_1ay_2-y_2ay_1}{y_1^2}=0$$

So $$\frac{y_2}{y_1}$$ is just some constant $$C$$, which implies that $$y_2$$ is necessarily linearly dependent on $$y_1$$. Therefore, we've shown that the solution space of $$y'=ay$$ (which is just $$(D-a)y=0$$: the kernel of $$D-a$$) has dimension exactly 1, and it has a basis $$e^{at}$$. In other words,

\begin{equation}\label{kerda}
\ker(D-a)=\operatorname{span}(e^{at})
\end{equation}

This demonstrates that **every eigenvector of the differential operator is an exponential function $$Ce^{at}$$**.

Now, we have answered our first question:

**Why is our guess for the solution $$e^{rt}$$?**

*Because exponentials are the unique functions that can be eigenvectors of the differential operator*. Therefore, they will also be eigenvectors of the polynomial differential operator.

$$p(D)e^{rt}=p(r)e^{rt}$$

So if $$p(r)=0$$, then $$e^{rt}$$ is a solution.

Thus, because the kernel is a subspace closed under linear combinations, we can take a linear combination of exponentials $$e^{\lambda_1t},\ldots,e^{\lambda_nt}$$, where $$\lambda_1,\ldots,\lambda_n$$ are the roots of $$p(x)$$, to say

$$y=c_1e^{\lambda_1t}+\ldots+c_ke^{\lambda_nt}$$

will be a solution to $$p(D)y=0$$. Note: we do not say the *general* solution quite yet, as any repeated roots will make the set of these exponentials trivially linearly dependent.

We remark that \eqref{kerda} equivalently tells us that if $$q(x)$$ is a degree one polynomial, then $$\ker(q(D))$$ has a basis $$\{e^{at}\}$$ for $$a$$ such that $$q(a)=0$$, implying that the general solution to $$q(D)y=0$$ is $$y=Ce^{at}$$.

We actually have enough now to prove that an $$n$$th order equation has homogeneous solution space of dimension exactly $$n$$.

# Second Order. Two Independent Solutions

We can prove that \eqref{kerda} actually generalizes to $$n$$th order equations by induction. Instead of doing the full induction proof, I will do the extension from first order to second order (the full proof has an essentially identical process).

Suppose $$p(x)$$ is a second degree polynomial. Then $$p(x)=(x-a)q(x)$$ where $$q(x)$$ is a degree one polynomial (this is guaranteed by the fundamental theorem of algebra, meaning $$a$$ can be complex). Hence,

$$p(D)y=0\implies (D-a)q(D)y=0\implies q(D)y\in\ker(D-a)$$

\eqref{kerda} then tells us that $$q(D)y=c_2e^{at}$$. We know we can find a particular solution to $$q(D)y=e^{at}$$ (which we will call $$y_2$$) by using an [integrating factor](../integratingfactor/){:target="_blank"}, since it's first order$$^{[1]}$$.

<details>
  <summary style="color:white;">[1]</summary>
    <p>ok to generalize this to nth order i need you Picard–Lindelöf please forgive me</p>
</details>

That is, $$y_2$$ is a preimage of $$e^{at}$$ under $$q(D)$$, so the general solution to $$q(D)y=e^{at}$$ is $$y=c_1y_1+y_2$$, where $$y_1$$ is a basis for $$\ker(q(D))$$ by the preimage theorem. But, if $$y_2$$ is a preimage of $$e^{at}$$, then $$c_2y_2$$ is a preimage of $$c_2e^{at}$$. Hence, the general solution to $$q(D)y=c_2e^{at}$$ is

$$y=c_1y_1+c_2y_2$$

We claim that $$y$$ is a solution to $$p(D)y=0$$. If we take the image of $$y$$ under $$q(D)$$, we get $$c_2e^{at}$$ as we already showed. But if we then take the image under $$D-a$$, we will get zero by \eqref{kerda}. Hence, $$y$$ is in the kernel of $$(D-a)\circ q(D)=(D-a)q(D)=p(D)$$.

Now, $$y_2$$ cannot be linearly dependent (a scalar multiple of) $$y_1$$, because then it would be in the kernel of $$q(D)$$ and thus could not be a preimage of $$e^{at}\neq0$$ under $$q(D)$$. Hence, $$y_1,y_2$$ form a set of two linearly independent vectors in $$\ker(p(D))$$, making its dimension at least two. We now need to show that there cannot be another linearly independent solution.

Suppose that $$y_3$$ is also a solution to $$p(D)y=0$$ which is linearly independent with $$\{y_1,y_2\}$$. $$y_3$$ can't be in the kernel of $$q(D)$$, because then it would be linearly dependent with $$y_1$$. So $$q(D)y_3\neq0\implies q(D)y_3\in\ker(D-a)$$. That is, $$q(D)y_3=c_3e^{at}$$. But, like before, we know that $$c_3y_2$$ will be a preimage of $$c_3e^{at}$$ under $$q(D)$$, so by the preimage theorem $$y_3=c_3y_2+c_4y_h$$ where $$y_h\in\ker(q(D))$$. But, that means $$c_4y_h=c_5y_1$$, implying $$y_3=c_3y_2+c_5y_1$$, contradicting that $$y_3$$ is linearly independent from $$y_1$$ and $$y_2$$. Therefore, the dimension of $$\ker(p(D))$$ is exactly two!

This answers our second question, **"Why does a second order equation have exactly two linearly independent homogeneous solutions?"**

Because a second order equation is the composition of two degree one operators which each add a dimension to the kernel.

As I mentioned before, this logic does generalize almost exactly to the $$n$$th order case! I encourage you to fill in the details.

# Repeated Roots

i.e. why in the sweet heavenly cheese husk do we multiply by $$t$$ of all things to get our other solutions?

I brushed over this topic with a meme about reduction of order last time, but I actually have a good explanation this time.

Let's start with the simplest case. What's the solution to the differential equation

$$D^ky=0\implies y^{(k)}=0$$

This is one of the easiest differential equations, because we can just integrate $$n$$ times to get

$$y=c_1+c_2t+\ldots+c_kt^{k-1}$$

Okay, easy enough. Now you may be thinking, "okay, when you put it like that, yeah repeated roots means repeated differentiation so that's where the $$t$$'s come from *in this case*. But what about $$(D-a)^k$$?"

## Exponential Shift

Consider the derivative of $$e^{at}f(t)$$.

$$D\left(e^{at}f(t)\right)=e^{at}(f'(t)+af(t))=e^{at}(D+a)f(t)$$

If you've taken enough derivatives, you may have caught on to this little shortcut. Since exponentials just get scaled by derivatives, we can just sum up the derivatives of the function multiplying it and scale by the constant appropriately. But let me tell you, this generalizes incredibly. We call this property the **exponential shift**:

\begin{equation}
De^{at}=e^{at}(D+a),\quad e^{at}D=(D-a)e^{at}
\end{equation}

I encourage you to prove that linearity actually guarantees that

\begin{equation}
p(D)e^{at}=e^{at}p(D+a),\quad e^{at}p(D)=p(D-a)e^{at}
\end{equation}

And this is going to make our lives *so* much easier. Let's go back to

$$(D-a)y=0$$

If we multiply by $$e^{-at}$$, then we can change that pesky $$D-a$$ into just $$D$$. That is,

$$e^{-at}(D-a)y=(D-(-a)-a)e^{-at}y=D(e^{-at}y)=0$$

And if $$e^{-at}y$$ is in the kernel of $$D$$, then it's just a constant. So $$e^{-at}y=C\implies y=Ce^{at}$$. If you look at what we did closely, you'll notice we basically just did an integrating factor without doing an integrating factor.

This is the takeaway: **we can leverage the exponential shift to look at the kernel of just $$D$$**.

## Exponential Shift Into Overdrive

Alright, so let's answer the question. What happens when we have a repeated root in $$p(x)$$? Say that $$(x-a)^k$$ divides $$p(x)$$. That is, $$p(x)=q(x)(x-a)^k$$. Then if we multiply $$e^{-at}$$ to $$p(D)y=0$$, we get

$$e^{-at}q(D)(D-a)^ky=q(D+a)D^k(e^{-at}y)$$

If we let $$u=e^{-at}y$$, then we get $$q(D+a)D^ku=0$$. Thus, any solution to $$D^ku=0$$ will also be a solution to $$q(D+a)D^ku=0$$. And we know the solution to that is just $$c_1+c_2t+\ldots+c_kt^{k-1}$$. Therefore,

$$u=e^{-at}y=c_1+c_2t+\ldots+c_kt^{k-1}$$

$$y=e^{at}\left(c_1+c_2t+\ldots+c_kt^{k-1}\right)$$

is a solution to $$p(D)y=0$$.

And we have now answered our third question, **"Why do we multiply by $$t$$ when we have a repeated root of the characteristic polynomial?"**

Because exponentials shift derivatives, and the kernel of repeated differentiation is a polynomial.

This also gives us another way to think about the second question as well. What we have shown essentially implies that every $$n$$th order differential equation of the form $$p(D)y=g(t)$$ can be solved using $$n$$ integrating factors. The first of which can be $$e^{-\lambda t}$$, where $$\lambda$$ is a root of $$p(x)$$. After doing $$n$$ integrations, we will be left with $$n$$ arbitrary constants. This explanation is a bit more handwavy, though, as it does not answer why the functions on each arbitrary constant will necessarily be linearly independent.

As a final remark: for constant coefficients, reduction of order *is* just the exponential shift, but more roundabout. This is because you basically insert an exponential into the equation with $$y=ve^{at}$$, which will cause things to shift. For example, if you've done reduction of order on $$y''-2ky'+k^2y=0$$, $$y=e^{kt}v$$, then you do end up with $$v''=0$$. Which is exactly what we would expect:

$$(D-k)^2e^{kt}v=e^{kt}D^2v=0\implies v''=0$$

Except we didn't have to do the product rule a bunch of times, plug in, and simplify.

## Exponential Response Formula

Alright, I'm going to prove and motivate the exponential response formula (ERF) in one line. Please try not to laugh too hard at how absurdly simple it is. By \eqref{divide} (yeah, remember *that* one?), if $$p(a)\neq0$$, then

$$p(D)e^{at}=p(a)e^{at}\implies p(D)\left(\frac{Be^{at}}{p(a)}\right)=Be^{at}$$

is a particular solution. Okay, that's all folks. Seeya next time!

---

No, but really, it is that simple. We then get $$\frac{Be^{at}}{p(a)}$$ as a preimage of $$Be^{at}$$ because it's an eigenvector, and we can just divide by the eigenvalue when it's nonzero.

We can use some of our techniques here to get the generalized exponential response formula as well. However, it requires a result I don't feel like proving:

**$$p^{(k)}(a)=0$$ for $$0\leq k<m$$ and $$p^{(m)}(a)\neq0$$ if and only if $$a$$ is a root of $$p(x)$$ with multiplicity exactly $$m$$. And $$p(x)=q(x)(x-a)^m$$ where $$q(a)=\frac{p^{(m)}(a)}{m!}\neq0$$**

Then for $$p(D)y=q(D)(D-a)^my=Be^{at}$$, we can use our good ol' exponential shift with $$e^{-at}$$

$$q(D+a)D^m(e^{-at}y)=B$$

Letting $$u=D^m(e^{at}y)$$, we get $$q(D+a)u=B$$, where we know that plugging in $$x=0$$ into $$q(x+a)$$ will give us something nonzero. Hence, we can use our ERF to say a particular solution is $$u=\frac{B}{q(0+a)}=\frac{Bm!}{p^{(m)}(a)}$$. That is,

$$D^m(e^{-at}y)=\frac{Bm!}{p^{(m)}(a)}$$

Now, since we're just looking for a single particular solution, we can just integrate $$m$$ times and take all the constants to be $$0$$. And since the $$m$$th integral of $$1$$ is $$\frac{t^m}{m!}$$, we basically just multiply by $$t^m$$ and divide by $$m!$$. Thus,

\begin{equation}
y=\frac{Bt^me^{at}}{p^{(m)}(a)}
\end{equation}

## Complex Stuff

You may have noticed that I didn't really specify what all the constants where in any of what I did. That's because this general theory works for *all* polynomials, even complex ones. It's only the very specific real polynomial case where you *can* always convert complex roots to sines and cosines. In most textbooks, they present this stuff in operator notation, but I'll just speedrun through it for completion's sake.

If $$p(x)$$ is a real polynomial (it has real coefficients, not complex ones), then $$p(D)$$ is an operator that maps real functions to real functions. That is, if $$f(x)$$ is a real valued function, then $$p(D)f(x)$$ is also always real valued.

Thus, if $$F(x)=u(x)+iv(x)$$, then by linearity of linear transformations

$$p(D)F(x)=p(D)u(x)+ip(D)v(x)$$

So the real part of $$p(D)F(x)$$ is $$p(D)$$ applied to the real part of $$F(x)$$, and similarly with the imaginary part.

Hence, if $$p(D)F(x)=0$$, then both the real and imaginary parts must be zero, so $$p(D)u(x)=p(D)v(x)=0$$. That is, the real and imaginary parts of any complex element of the kernel are also individually in the kernel.

It follows from [Euler's Formula](../eulersformula/){:target="_blank"} that if $$\alpha=a+bi$$ is a root of $$p(x)$$, then

$$e^{(a+bi)t}=e^{at}\left(\cos(bt)+i\sin(bt)\right)$$

will be a solution, so we can take the real and imaginary parts blah blah blah

$$y=e^{at}\left(c_1\cos(bt)+c_2\sin(bt)\right)$$

will be a solution.

So, similar with repeated roots, the case of

$$y=(c_1+\ldots+c_kt^{k-1})e^{\alpha t}$$

just means two individual sets of solutions

$$
\begin{align*}
y_1=(c_1+\ldots+c_kt^{k-1})e^{at}\cos(bt)\\
y_2=(d_1+\ldots+d_kt^{k-1})e^{at}\sin(bt)\\
\end{align*}
$$

It may seem like we're doubling the number of solutions, but nah. This is because if $$p(x)$$ is real valued, then any complex root will also have a corresponding complex conjugate root. And, since Euler's formula basically just makes the conjugate flip the sign of the imaginary part, the two solutions taken from the conjugate solution will be linearly dependent on the two solutions obtained from the original complex root. That is, normally we have

$$y=(c_1+\ldots+c_kt^{k-1})e^{\alpha t}+(d_1+\ldots+d_kt^{k-1})e^{\overline\alpha t}$$

so we're still left with $$2k$$ solutions in the end.

---

## Final Thoughts

I love this perspective. The ideas of "exponentials would be an expected guess", "to get the other solutions, multiply one solution by an arbitrary function $$v(t)$$", or "just reduce the $$n$$th order equation down to a system of first order equations" seemed intuitive, but only in retrospect. As someone who questions a lot, and wants to know *why* something is true, the answers felt very contrived.

But once we change from a differential equation to a linear operator, suddenly everything is a lot simpler (at least to me). The progression from first order to $$n$$th order is smooth and things just work out exactly the way you would expect them to. 

But this is coming from someone who thinks a lot about these subjects, so perhaps it isn't much easier for you. Especially if you don't know any linear algebra (and if you got here without knowing linear algebra, uh... why? thank you, but why?) I hope this is helpful, though.

This is a heavily condensed version of a chapter from a Linear Algebra + Differential Equations textbook I'm working on. I hope you liked it, and maybe you'll want to check out the textbook when it's done (ETA: probably never). Alright, thanks for reading.

[hyperlink](https://youtu.be/Tptx8boeGhE?si=1G60x2ZMJgUPC8Gr){:target="_blank"}
