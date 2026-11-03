---
title: "Boundary limits of the matrix geometric mean and the failure of unrestricted GLT closure"
author: "Anonymous"
date: "3 November 2026 (revised version)"
lang: en-GB
fontsize: 11pt
papersize: a4
geometry: margin=25mm
colorlinks: true
linkcolor: violet
urlcolor: violet
toc: false
numbersections: false
header-includes:
  - \usepackage{amsmath,amssymb,booktabs}
  - \usepackage{microtype}
  - \usepackage{float}
  - \floatplacement{figure}{htbp}
  - \setlength{\emergencystretch}{3em}
  - \usepackage{caption}
  - \usepackage{needspace}
  - \captionsetup[figure]{labelformat=empty}
---

# Abstract

The geometric mean $A\#B$ of two positive definite matrices is the
midpoint of the natural geodesic between them and the unique positive
solution of the Riccati equation $XA^{-1}X=B$. It is continuous on positive definite pairs but need not be continuous at singular pairs. We describe every
limit that can occur: a matrix $X$ is a limit of $A_j\#B_j$ with
positive definite $A_j\to A$, $B_j\to B$ exactly when $X\succeq0$, the
block matrix $\left(\begin{smallmatrix}A&X\\X&B\end{smallmatrix}\right)$
is positive semidefinite, and its rank is at most the ambient dimension.
In Ando's description of $A\#B$ as the largest $X$ with that block
matrix positive semidefinite, the limits are therefore exactly the
positive semidefinite feasible points whose block matrix has rank at
most $N$. A dilation description
of the same set, with an auxiliary contraction, already follows from
recent work of Jones; our contribution is the explicit elimination of
that variable and its consequences. At equal inputs we obtain the full
set of limits and the exact interval of limiting Matsumoto fidelities.

For generalized locally Toeplitz (GLT) matrix-sequences we construct
uniformly bounded positive definite input sequences with identical
scalar symbols whose geometric means have the wrong symbol, or no
eigenvalue distribution at all. These examples satisfy the hypotheses of Theorem 4 and Conjecture 1 of
the arXiv version of Ilyas, Khan, Loi and Serra-Capizzano and, according
to an AI-assisted reading of the published text, of Theorem 3 and
Conjecture 1 of their article in Linear Algebra Appl. (2025); these
statements are therefore false as stated. We
locate the failing step of the published proof. On the positive side,
closure holds when the sum of the two symbols is positive definite
almost everywhere, for every Kubo--Ando mean (the axiomatic class of
operator means that contains the arithmetic, geometric and harmonic
means). A new one-sided theorem
shows that the regularised symbol is always an upper envelope: the
eigenvalues of the means can lose mass relative to it but never gain
it. For bounded Riemann-integrable scalar symbols depending on the space
variable only, this yields a sharp dichotomy: the symbol formula holds
for every positive definite realisation if and only if the two symbols
have no common zero set of positive measure or have essentially disjoint
supports.

# 1. Introduction

## 1.1. The geometric mean and why its boundary matters

For positive numbers $a,b$ the geometric mean $\sqrt{ab}$ is the
"multiplicative midpoint" of $a$ and $b$. Its matrix analogue for
Hermitian positive definite (HPD) matrices $A,B$ is
$$
A\#B=A^{1/2}\bigl(A^{-1/2}BA^{-1/2}\bigr)^{1/2}A^{1/2},
$$
introduced by Pusz and Woronowicz [1] and placed in the general
theory of operator means by Kubo and Ando [2] (a Kubo--Ando
mean is any operation on positive matrices satisfying a short list of
natural axioms: monotonicity, the transformer inequality and continuity
from above; the arithmetic, harmonic and geometric means are examples); see also Ando
[3], Lawson and Lim [4] and Bhatia [5]. It keeps
the properties one wants from a mean (symmetry, monotonicity, invariance
under congruence $A\mapsto TAT^*$) even though $A$ and $B$ need not
commute. It is the midpoint of the geodesic joining $A$ and $B$ in the
affine-invariant Riemannian geometry of positive definite matrices
[5], [6]. It is used to average covariance matrices, for
example in brain--computer interfaces [7]; to average
structured matrices such as Toeplitz matrices [8]; and in quantum
information, where $\operatorname{tr}(\rho\#\sigma)$ is the Matsumoto
(or geometric) fidelity of two states [9], [10],
[11].

Real data are often rank deficient: covariance matrices with fewer
samples than variables, nearly pure quantum states, discretised
operators whose coefficients vanish on a region. The mean of singular
matrices is defined by a limit, normally
$\lim_{\varepsilon\downarrow0}(A+\varepsilon I)\#(B+\varepsilon I)$, but
other approximating sequences can give other limits. That discontinuity
is classical. The first question of this paper is: *which* limits can
occur? Theorem 1 answers it completely.

## 1.2. GLT sequences and symbols, intuitively

Discretising a differential or integral operator on finer and finer
grids produces a sequence of matrices $A_n$ of growing size. For a large
class of such sequences, the *generalized locally Toeplitz* (GLT) class
[12], [13], [14], [15], the eigenvalues are
asymptotically described by a function $\kappa(x,\theta)$, the
*symbol*, of a space variable $x$ and a frequency variable $\theta$:
for large $n$ the histogram of the eigenvalues of $A_n$ looks like the
histogram of the values of $\kappa$. For example, the standard
finite-difference matrix of $-u''$ has symbol $2-2\cos\theta$, and a
variable coefficient $a(x)$ multiplies it; the diagonal matrix of
samples $\operatorname{diag}(a(j/n))_{j=1}^n$ has symbol $a(x)$. GLT
sequences form an algebra: sums, products, inverses (when the symbol is invertible almost everywhere) and continuous
functions of Hermitian GLT sequences are GLT, and the symbol follows the same operations. Two features matter
below. First, the symbol cannot see perturbations whose norm tends to
zero, or whose rank is a vanishing fraction of the size. Second, a
Hermitian GLT sequence always has a limiting eigenvalue distribution.
Two technical terms recur. A sequence is *zero-distributed* if, for
every $\delta>0$, the fraction of its singular values above $\delta$
tends to zero; these are exactly the GLT sequences with symbol $0$. An
*approximating class of sequences* (a.c.s.) is the notion of convergence
used in GLT theory: a family of sequences approximates a given one if
the differences split into a part of small norm and a part of small
relative rank.

The natural question is whether the symbol of $A_n\#B_n$ is the
geometric mean of the symbols. If it is, the spectral analysis of an
averaged discretisation comes for free.

## 1.3. What was claimed, and what goes wrong

Ahmad, Khan and Serra-Capizzano [16] proved the symbol formula
$\{A_n\#B_n\}\sim_{\rm GLT}(\kappa\xi)^{1/2}$ for scalar symbols when at
least one symbol is nonzero almost everywhere, following Garoni and
Serra-Capizzano [12]. Ilyas, Khan, Loi and Serra-Capizzano [17]
then stated it with no such hypothesis (we quote the arXiv wording in
Section 6.3; an AI-assisted reading of the published version found the
same hypotheses), and conjectured the
corresponding statement for matrix-valued symbols with the regularised
mean as the candidate symbol. The same result appears in Khan's thesis
[18].

The unrestricted statement is false. The reason is visible already in
dimension two (Section 5): two positive definite matrices can both be
within $\varepsilon$ of $\operatorname{diag}(1,0)$ while their mean is
close to $\operatorname{diag}(c,0)$ for any prescribed $c\in[0,1]$. A
coupling of size $O(1/N)$ between the range and the kernel decides the
answer. A GLT symbol cannot see such a coupling. Repeating the
two-dimensional example along the diagonal gives HPD sequences with
the same step-function symbol whose means have symbol $\tfrac45$ times
the predicted one, or no symbol at all (Figure 1, after the table below).

\needspace{14\baselineskip}

## 1.4. Results

| Result | Statement in brief | Status relative to earlier work |
|---|---|---|
| Theorem 1 | Limits of $A_j\#B_j$ at a singular pair $(A,B)$ are exactly the $X\succeq0$ with $\left(\begin{smallmatrix}A&X\\X&B\end{smallmatrix}\right)\succeq0$ of rank $\le N$ | Dilation form follows from Jones [19]; explicit elimination new as far as we found |
| Corollaries 2--3 | Equal inputs: limits $0\preceq X\preceq A$ with $\operatorname{rank}(A-X)\le\dim\ker A$; exact interval of Matsumoto-fidelity limits | Lower endpoint and the case $q\ge r$ are in Jones; necessity and the full set are new |
| Section 6 | Bounded HPD scalar GLT inputs with equal symbols whose means have the wrong symbol or no distribution | Refutes [17]: arXiv Thm 4, Conj. 1 (quoted); published Thm 3, Conj. 1 (AI-assisted reading, Section 6.3) |
| Theorem 4 | Any sequence of contractions can be hidden behind two fixed input symbols | New as far as we found |
| Theorem 5, Corollary 6 | Closure if $\kappa+\xi\succ0$ a.e., for every Kubo--Ando mean | Standard identity, GLT transfer |
| Theorem 7, Corollary 8 | Means never gain spectral mass over $\kappa\#\xi$; closure if $\kappa\#\xi=0$ a.e. | New (sequence-level form of a classical order bound) |
| Theorem 9, Corollary 10 | For bounded Riemann-integrable $x$-only scalar symbols: closure for all realisations $\iff$ no common zero set of positive measure, or essentially disjoint supports | New |
| Appendix A | Sharp spectral envelope of means near projections of any rank density | New as far as we found |

![**Figure 1.** (a) Both inputs $A_e,B_{e,t}$ of (5.1) tend to the projection $\operatorname{diag}(1,0)$ as $e\to0$, but their geometric mean tends to $c(t)\operatorname{diag}(1,0)$ with $c(t)=2/\sqrt{4+t^2}$: every value in $(0,1]$ occurs. (b) Assembling these blocks gives two matrix-sequences with the same GLT symbol at every size. Choosing $t=0$ at even sizes and $t=3/2$ at odd sizes makes the normalised trace of the mean approach $1/2$ along even sizes and $2/5$ along odd sizes, so the means have no limiting eigenvalue distribution. Values are the exact formula (6.6).](fig1_mean_collapse.pdf){width=100%}

## 1.5. Relation to earlier work

Two pieces of earlier work are close and we state the overlap up front.
First, Ando [3] and Pusz--Woronowicz [1] characterised $A\#B$ as
the *largest* Hermitian $X$ with
$\left(\begin{smallmatrix}A&X\\X&B\end{smallmatrix}\right)\succeq0$
(Lemma 2.1). Theorem 1 says that the set of boundary limits is exactly
the part of this classical feasible set where, in addition, $X\succeq0$
and the block matrix has rank at most $N$. In particular every limit lies
below $A\#B$.

Second, Jones [19] studies continuity of Kubo--Ando means and
channel divergences. His Lemma 4.12.1(b) gives the envelope "every limit
point lies below $A\#B$". His Lemma 4.12.3 constructs boundary limits by
dilating a positive contraction into the common kernel; together with an
elementary compactness argument this already gives a complete
description of the set of limits *with an auxiliary contraction*
(Appendix B). His Theorem 4.12.4(b) and Corollary 4.12.5 give the lower
endpoint of our fidelity interval and the case in which it is $[0,1]$.
The contribution of Theorem 1 is the explicit elimination of the
auxiliary contraction into block positivity plus one rank inequality,
and the use of that form for the necessity half of the corollaries.
The two-dimensional discontinuity itself is classical (an example is
attributed to Bhatia [5] in lecture slides by Poulson
[20]). The GLT consequences (Sections 6--9) and Appendix A are
not in these sources.

## 1.6. Reader's guide

Section 2 fixes notation and states Theorem 1; Section 3 proves it.
Section 4 treats equal inputs and quantum fidelity. Section 5 gives the
two-dimensional formula that drives every counterexample. Section 6
contains the GLT counterexamples and locates the error in the published
proof. Section 7 shows how much information can be hidden. Section 8
gives the positive closure theorem, and Section 9 the one-sided envelope
and the dichotomy, followed by a practical summary ("When is the symbol
formula safe?"). Section 10 lists open problems and Section 11 the scope
of verification. Appendix A treats growing dimensions at projections;
Appendix B records the dilation view and its relation to Theorem 1.

# 2. Setting and the graph-closure theorem

All matrices are complex and finite dimensional; the real symmetric case
uses the same constructions with real data. We write $A\succeq0$
($A\succ0$) for positive semidefinite (definite), $\preceq$ for the
Loewner order, and use the operator norm $\|\cdot\|$. The geometric
mean of $A,B\succ0$ is the unique positive definite solution $X$ of
$$
XA^{-1}X=B. \tag{2.1}
$$
Indeed, conjugation by $A^{-1/2}$ reduces (2.1) to the equation that
defines the positive square root of $A^{-1/2}BA^{-1/2}$. Consequently,
for every invertible $T$ and all $a,b>0$,
$$
(TAT^*)\#(TBT^*)=T(A\#B)T^*,\qquad (aA)\#(bB)=\sqrt{ab}\,(A\#B).\tag{2.2}
$$
The mean is monotone: $A\preceq A'$ and $B\preceq B'$ imply
$A\#B\preceq A'\#B'$ [2]. For $A,B\succeq0$ we use the
standard extension
$$
A\#B=\lim_{\varepsilon\downarrow0}(A+\varepsilon I)\#(B+\varepsilon I),
\tag{2.3}
$$
a decreasing limit by monotonicity. We also use
$A\#B\preceq(A+B)/2$: for $A,B\succ0$ put $T=A^{-1/2}BA^{-1/2}$; then
$(T^{1/2}-I)^2\succeq0$ gives $T^{1/2}\preceq(I+T)/2$, and congruence by
$A^{1/2}$ gives the claim; the singular case follows from (2.3).

For $A,B,X$ Hermitian put
$$
M(A,B,X)=\begin{pmatrix}A&X\\X&B\end{pmatrix}.
$$

**Lemma 2.1 (classical facts).** Let $A,B\succeq0$.

(a) *(Ando, Pusz--Woronowicz)* $A\#B$ is the largest Hermitian $X$
with $M(A,B,X)\succeq0$ [3], [1], [5].

(b) $\operatorname{ran}(A\#B)=\operatorname{ran}A\cap\operatorname{ran}B$.

*Proof.* (a) For $A\succ0$, $M(A,B,X)\succeq0$ is equivalent to
$B\succeq XA^{-1}X$, that is $Y^2\preceq K$ with
$Y=A^{-1/2}XA^{-1/2}$ and $K=A^{-1/2}BA^{-1/2}$. Since the square root
is operator monotone, $Y\preceq|Y|=(Y^2)^{1/2}\preceq K^{1/2}$, which
after congruence is $X\preceq A\#B$; equality is feasible by (2.1). For
singular $A,B$, feasibility of $X$ at $(A,B)$ implies feasibility at
$(A+\varepsilon I,B+\varepsilon I)$, hence
$X\preceq(A+\varepsilon I)\#(B+\varepsilon I)$; let $\varepsilon\to0$.
Feasibility of $A\#B$ itself follows by taking limits.
(b) If $u\in\ker A$, the vector $(u,0)$ has zero quadratic form for the
positive semidefinite matrix $M(A,B,A\#B)$, hence lies in its kernel,
so $(A\#B)u=0$; similarly for $\ker B$. Thus
$\operatorname{ran}(A\#B)\subseteq\operatorname{ran}A\cap\operatorname{ran}B$.
Conversely, if $0\ne v\in\operatorname{ran}A\cap\operatorname{ran}B$,
there is $c>0$ with $A\succeq c\,vv^*$ and $B\succeq c\,vv^*$, so by
monotonicity and (2.2)--(2.3)
$A\#B\succeq(c\,vv^*)\#(c\,vv^*)=c\,vv^*$, and $v\in\operatorname{ran}(A\#B)$.
$\square$

**Theorem 1 (complete graph closure).** Let $A,B,X$ be Hermitian
$N\times N$ matrices with $A,B\succeq0$. The following are equivalent.

1. There are $A_j,B_j\succ0$ with $A_j\to A$, $B_j\to B$ and
   $A_j\#B_j\to X$.
2. $X\succeq0$, and
   $$
   M(A,B,X)\succeq0,\qquad \operatorname{rank}M(A,B,X)\le N.\tag{2.4}
   $$

**Remarks.**

(i) *Each condition is needed.* For $N=1$, $A=B=1$ and
$X=-1$, the block matrix is positive semidefinite of rank $1$ but $X$ is
not attainable. For $A=B=I_2$ and $X=\tfrac12I_2$ the block matrix is
positive definite (rank $4>2$); since $\#$ is continuous at positive
definite pairs, the only limit is $I_2$.

(ii) *Relation to Lemma 2.1(a).* By Theorem 1 every limit is a
feasible point for Ando's problem, so every limit satisfies
$X\preceq A\#B$ (this envelope is also Jones's Lemma 4.12.1(b)
[19]). The regularised mean is the top of the set of limits.

(iii) *Unitary-factor form.* Condition 2 holds if and only if
$X\succeq0$ and $X=A^{1/2}WB^{1/2}$ for some unitary $W$. Indeed, if
(2.4) holds, write $M(A,B,X)=ZZ^*$ with
$Z=\left(\begin{smallmatrix}F\\G\end{smallmatrix}\right)$,
$F,G\in\mathbb C^{N\times N}$; then $FF^*=A$, $GG^*=B$, $FG^*=X$, and
the polar decompositions $F=A^{1/2}U$, $G=B^{1/2}V$ give
$X=A^{1/2}UV^*B^{1/2}$. Conversely, $Z=\left(\begin{smallmatrix}A^{1/2}\\B^{1/2}W^*\end{smallmatrix}\right)$
gives $ZZ^*=M(A,B,X)$, of rank at most $N$. For $A,B\succ0$, any such
Hermitian $X$ satisfies $XA^{-1}X=B^{1/2}W^*WB^{1/2}=B$, so the set is
$\{A\#B\}$, the classical unitary characterisation.

(iv) *Schur-complement reading.* In the normal form of Section 3 the rank
condition says that the residual $R=B_0-CA_0^{-1}C$, a generalised
Schur complement in the sense of shorted-operator theory [21],
has rank at most the dimension of the common kernel.

**Corollary 2 (equal boundary inputs).** Let $A\succeq0$ have rank $r$
in dimension $N$, and put $q=N-r$. The set of limits of $A_j\#B_j$ over
all $A_j,B_j\succ0$ tending to $A$ is exactly
$$
\{X:\ 0\preceq X\preceq A,\ \operatorname{rank}(A-X)\le q\}.\tag{2.5}
$$
In particular, if $q\ge r$, every $X$ with $0\preceq X\preceq A$ occurs.

# 3. Proof of Theorem 1

## 3.1. Necessity

Let $X_j=A_j\#B_j$. By (2.1) the Schur complement of $A_j$ in
$M_j=M(A_j,B_j,X_j)$ is $B_j-X_jA_j^{-1}X_j=0$, so $M_j\succeq0$ and
$\operatorname{rank}M_j=N$. Positive semidefiniteness passes to the
limit, and so does $\operatorname{rank}\le N$, because all
$(N+1)$-minors of $M_j$ vanish. Finally $X\succeq0$ as a limit of
positive definite matrices.

## 3.2. A simultaneous congruence reduction

Assume condition 2. Put $S=A+B$, $s=\operatorname{rank}S$, $k=N-s$.
Choose an invertible $T_0$ with $T_0ST_0^*=I_s\oplus0_k$. Since
$0\preceq T_0AT_0^*,T_0BT_0^*\preceq T_0ST_0^*$, both transformed
matrices vanish on the last $k$ coordinates; on the first $s$
coordinates they sum to $I_s$, so they commute and can be diagonalised
by one unitary. (No commutation of the original $A$ and $B$ is used.)
Grouping eigenvalues equal to $1$, equal to $0$ and strictly between,
we obtain a fixed invertible $T$ with
$$
TAT^*=I_a\oplus0_b\oplus A_0\oplus0_k,\quad
TBT^*=0_a\oplus I_b\oplus B_0\oplus0_k,\quad A_0,B_0\succ0,\ A_0+B_0=I_t,
\tag{3.1}
$$
where $a+b+t+k=N$. By (2.2), both conditions of Theorem 1 are invariant
under $(A,B,X)\mapsto(TAT^*,TBT^*,TXT^*)$; block rank is preserved by
the block-diagonal congruence $T\oplus T$. So we may assume (3.1).

*Support.* If $u\in\ker A$, then $(u,0)$ has zero quadratic form for
$M(A,B,X)\succeq0$, hence lies in its kernel, so $Xu=0$; similarly for
$\ker B$. In (3.1) this forces
$$
X=0_a\oplus0_b\oplus C\oplus0_k,\qquad C\succeq0.\tag{3.2}
$$
On the mixed coordinates put $R=B_0-CA_0^{-1}C$. The Schur complement
criterion gives $R\succeq0$, and block elimination gives
$$
\operatorname{rank}M(A,B,X)=a+b+t+\operatorname{rank}R.\tag{3.3}
$$
Hence the rank hypothesis is exactly $\operatorname{rank}R\le k$, and
we may choose $L\in\mathbb C^{t\times k}$ with $R=LL^*$ (padding with
zero columns). For real data, $T$ and $L$ can be chosen real.

## 3.3. The approximating pairs

For $\delta\in(0,1]$ put
$$
C_\delta=C+\delta I_t,\qquad Q_\delta=I_k+L^*C_\delta^{-1}L,\tag{3.4}
$$
and on the $t+k$ mixed and kernel coordinates
$$
\mathcal A_\delta=\begin{pmatrix}A_0&0\\0&\delta^4I_k\end{pmatrix},\qquad
\mathcal X_\delta=\begin{pmatrix}C_\delta&\delta^2L\\\delta^2L^*&\delta^4Q_\delta\end{pmatrix},\qquad
\mathcal B_\delta=\mathcal X_\delta\mathcal A_\delta^{-1}\mathcal X_\delta.\tag{3.5}
$$
The Schur complement of $C_\delta$ in $\mathcal X_\delta$ is
$\delta^4(Q_\delta-L^*C_\delta^{-1}L)=\delta^4I_k\succ0$, so
$\mathcal X_\delta\succ0$ and $\mathcal B_\delta\succ0$, and (2.1) gives
$\mathcal A_\delta\#\mathcal B_\delta=\mathcal X_\delta$ exactly.
Multiplying out,
$$
\mathcal B_\delta=\begin{pmatrix}
C_\delta A_0^{-1}C_\delta+LL^*&\delta^2(C_\delta A_0^{-1}L+LQ_\delta)\\
\delta^2(L^*A_0^{-1}C_\delta+Q_\delta L^*)&\delta^4(L^*A_0^{-1}L+Q_\delta^2)
\end{pmatrix}.\tag{3.6}
$$
Since $C_\delta\succeq\delta I_t$, $\|Q_\delta\|\le1+\|L\|^2/\delta$.
Hence $\delta^2\|LQ_\delta\|\le\delta^2\|L\|+\delta\|L\|^3$ and
$\delta^4\|Q_\delta\|^2\le\delta^4+2\delta^3\|L\|^2+\delta^2\|L\|^4$. The
upper-left block of (3.6) differs from $CA_0^{-1}C+LL^*=B_0$ by
$\delta(CA_0^{-1}+A_0^{-1}C)+\delta^2A_0^{-1}$. Therefore
$$
\mathcal A_\delta\to A_0\oplus0_k,\qquad\mathcal B_\delta\to B_0\oplus0_k,\qquad
\mathcal X_\delta\to C\oplus0_k .\tag{3.7}
$$
On each coordinate of the $a$-block use the scalar pair $(1,\delta^2)$,
and on each coordinate of the $b$-block the pair $(\delta^2,1)$; both have
mean $\delta\to0$. The direct sum of these pairs with
$(\mathcal A_\delta,\mathcal B_\delta)$, transformed back by $T^{-1}$,
gives the required approximants. Empty blocks are harmless: if $k=0$
then $R=0$ and $L$ is void; if $t=0$ the kernel coordinates carry
$\mathcal A_\delta=\mathcal B_\delta=\mathcal X_\delta=\delta^4I_k$.
$\square$

**Remark 3.1 (rate).** The estimates above show that, in the normal form, the
errors are $O(\delta^2)$ for $A$ ($O(\delta^4)$ when $b=0$; the
$b$-block contributes $\delta^2$) and $O(\delta)$ for $B$ and $X$, with
constants of order $1+\|C\|\,\|A_0^{-1}\|+\|L\|^3$ (where
$\|L\|^2=\|R\|\le1$). Undoing the congruence multiplies the constants
by at most $\|T^{-1}\|^2$. The constants can be large when $A_0$ has small
eigenvalues; the exact checks in Section 11 confirm the $O(\delta)$
behaviour on complex non-commuting data.

# 4. Equal inputs and Matsumoto fidelity

**Proof of Corollary 2.** With
$U=\tfrac1{\sqrt2}\left(\begin{smallmatrix}I&I\\I&-I\end{smallmatrix}\right)$,
$$
U^*M(A,A,X)U=\begin{pmatrix}A+X&0\\0&A-X\end{pmatrix}.
$$
For $X\succeq0$, block positivity is therefore $0\preceq X\preceq A$.
Then $\ker(A+X)=\ker A$, so
$\operatorname{rank}M(A,A,X)=r+\operatorname{rank}(A-X)$, and Theorem 1
gives (2.5). $\square$

**Corollary 3 (limits of the Matsumoto fidelity).** Let $\rho$ be a
density matrix of rank $r$ in dimension $d$ with nonzero eigenvalues
$\lambda_1\ge\dots\ge\lambda_r>0$, and $q=d-r$. Over all positive
definite density matrices $\rho_j,\sigma_j\to\rho$, the possible limits
of $\operatorname{tr}(\rho_j\#\sigma_j)$ form exactly the interval
$$
\Bigl[\ \sum_{i=\min(q,r)+1}^{r}\lambda_i,\ 1\ \Bigr],\tag{4.1}
$$
where an empty sum is $0$. Thus the interval is $\{1\}$ for full rank,
and $[0,1]$ when $q\ge r$.

*Proof.* By Corollary 2 the matrix limits are $X=\rho-D$ with
$0\preceq D\preceq\rho$ and $\operatorname{rank}D\le q$. If $E$ is the
projection onto $\operatorname{ran}D$, then
$\operatorname{tr}D\le\operatorname{tr}(E\rho)\le\sum_{i=1}^{\min(q,r)}\lambda_i$
by Ky Fan's maximum principle, since $\operatorname{rank}E\le q$ and
$\rho$ has $r$ nonzero eigenvalues. The bound is attained by the
spectral part $D_*$ of $\rho$ for its $\min(q,r)$ largest eigenvalues,
and $tD_*$ ($0\le t\le1$) gives every intermediate trace. Theorem 1
supplies positive definite approximants; normalising each by its trace
does not change the limit, by (2.2), since both traces tend to $1$.
Conversely, a convergent sequence of fidelities has a subsequence along
which the means converge, because
$0\preceq\rho_j\#\sigma_j\preceq(\rho_j+\sigma_j)/2$ is bounded, and
Corollary 2 applies to it. $\square$

The lower endpoint, and the value $0$ when $q\ge r$, can be obtained
from Jones's dilation results (Theorem 4.12.4(b) with a suitable
invariant subspace, and Corollary 4.12.5 [19]), which also prove
that the fidelity is continuous at $(\rho,\rho)$ only when $\rho$ has
full rank. What Corollaries 2--3 add is necessity: no limit outside
(2.5), and no fidelity below (4.1). Cree and Sikora [11] study this
fidelity and its semidefinite formulations.

**Remark 4.1 (two nearly identical qubit states).** Take the matrices
$A_e$ and $B_{e,t}$ of (5.1) and normalise them:
$\rho_e=A_e/(1+e^2)$ and $\sigma_e=B_{e,t}/(1+(1+t^2)e^2)$. Here
$\rho_e$ is the pure state $|0\rangle$ with noise of weight $e^2$ in
the other direction, and $B_{e,t}=vv^*+\operatorname{diag}(0,e^2)$ with
$v=(1,te)$ is a pure state rotated by an angle of order $te$ plus the
same noise. Both states tend to $|0\rangle\langle0|$ as $e\to0$, so their
trace distance tends to $0$ and their Uhlmann fidelity
$\bigl(\operatorname{tr}|\rho_e^{1/2}\sigma_e^{1/2}|\bigr)^2$
[22] tends to $1$ (it is continuous and equals $1$ at the
limit). By (5.2), however,
$$
\operatorname{tr}(\rho_e\#\sigma_e)=\frac{2+(2+t^2)e^2}{\sqrt{4+t^2}\,\sqrt{(1+e^2)(1+(1+t^2)e^2)}}
\longrightarrow\frac{2}{\sqrt{4+t^2}} .
$$
So two states that are arbitrarily close can have any Matsumoto fidelity
in $(0,1]$. The trigger is not exotic: a coherent rotation of size
$\theta=te$ combined with a noise floor of order $\theta^2$. Every state in this family has full rank, so positive definiteness alone
is no safeguard. Matsumoto fidelity should therefore not be used as a
robust closeness measure near pure states without quantitative control
of the smallest eigenvalues, for example a uniform positive lower bound
on the spectrum.

# 5. A two-dimensional formula

For $e>0$ and $t\ge0$ let
$$
A_e=\begin{pmatrix}1&0\\0&e^2\end{pmatrix},\qquad
B_{e,t}=\begin{pmatrix}1&te\\te&(1+t^2)e^2\end{pmatrix}.\tag{5.1}
$$
Both are positive definite with determinant $e^2$. A direct
multiplication gives $(A_e+B_{e,t})A_e^{-1}(A_e+B_{e,t})=(4+t^2)B_{e,t}$,
so $X=(A_e+B_{e,t})/\sqrt{4+t^2}$ is positive definite and satisfies
$XA_e^{-1}X=B_{e,t}$. By (2.1),
$$
A_e\#B_{e,t}=\frac1{\sqrt{4+t^2}}\begin{pmatrix}2&te\\te&(2+t^2)e^2\end{pmatrix}.\tag{5.2}
$$
For fixed $t$, both inputs tend to $P=\operatorname{diag}(1,0)$, while
$$
A_e\#B_{e,t}\to c(t)P,\qquad c(t)=\frac2{\sqrt{4+t^2}} .\tag{5.3}
$$
The value $0$ is also attainable, letting $t\to\infty$ with $te\to0$.
At $t=3/2$ every coefficient is rational:
$$
B_{e,3/2}=\begin{pmatrix}1&3e/2\\3e/2&13e^2/4\end{pmatrix},\qquad
A_e\#B_{e,3/2}=\begin{pmatrix}4/5&3e/5\\3e/5&17e^2/10\end{pmatrix}.\tag{5.4}
$$
Formula (5.2) is a transparent instance of the classical mechanism; no
novelty is claimed for it.

# 6. Scalar GLT counterexamples

## 6.1. The GLT facts used

We use the following results for (block, multilevel) GLT sequences, with
the numbering of Barbarino, Garoni and Serra-Capizzano [14], [15];
the scalar unilevel versions are in Garoni and Serra-Capizzano
[12], [13]. Approximating classes of sequences (a.c.s.) go back
to [23]; see also [24].

* (G1) A Hermitian GLT sequence has its symbol as eigenvalue
  distribution (axiom GLT 1).
* (G2) Diagonal sampling of an almost-everywhere continuous bounded
  function $a$ (equivalently, a Riemann-integrable one) has symbol $a$:
  [14], Theorem 4.24, p. 78 (unilevel) and [15], Theorem 4.23,
  p. 169 (multilevel); also axiom GLT 3, second item.
* (G3) A sequence is zero-distributed if and only if it is GLT with
  symbol $0$ (axiom GLT 3, third item: [14], p. 86; [15], p. 180).
  In particular adding a sequence whose norm tends to zero does not
  change a symbol.
* (G4) Sums and products: [14], Theorem 4.17, p. 73; [15],
  Theorem 4.16, p. 164.
* (G5) Pseudoinverse: [14], Theorem 4.18, p. 73, which reads
  "If $\{A_n\}_n\sim_{\rm GLT}\kappa$ and $\kappa$ is invertible a.e.,
  then $\{A_n^\dagger\}_n\sim_{\rm GLT}\kappa^{-1}$"; multilevel:
  [15], Theorem 4.17, p. 165.
* (G6) Continuous functional calculus: [14], Theorem 4.19, p. 74;
  [15], Theorem 4.18, p. 165, which reads "If
  $\{A_n\}_n\sim_{\rm GLT}\kappa$ and each $A_n$ is Hermitian, then
  $\{f(A_n)\}_n\sim_{\rm GLT}f(\kappa)$ for any continuous function
  $f:\mathbb C\to\mathbb C$." No uniform norm bound on $A_n$ is required.

## 6.2. The construction

Let $a=\mathbf 1_{(0,1/2]}$ on $[0,1]$ and, for each size $N$,
$m=\lfloor N/2\rfloor$, so that the diagonal sampling is
$P_N=D_N(a)=\operatorname{diag}(a(j/N))_{j=1}^N=\operatorname{diag}(I_m,0_{N-m})$.
Take $e_N=1/N$, $d_N=N-2m\in\{0,1\}$, a bounded sequence $t_N\ge0$, and
$$
A_N=\begin{pmatrix}I_m&0\\0&e_N^2I_m\end{pmatrix}\oplus e_N^2I_{d_N},\qquad
B_N=\begin{pmatrix}I_m&t_Ne_NI_m\\t_Ne_NI_m&(1+t_N^2)e_N^2I_m\end{pmatrix}\oplus e_N^2I_{d_N}.\tag{6.1}
$$
Both are positive definite (their Schur complements are $e_N^2I_m$),
uniformly bounded, and
$$
\|A_N-P_N\|=e_N^2,\qquad\|B_N-P_N\|\le t_Ne_N+(1+t_N^2)e_N^2\to0.\tag{6.2}
$$
By (G2) and (G3), $\{A_N\}\sim_{\rm GLT}a$ and $\{B_N\}\sim_{\rm GLT}a$.
After a permutation the matrices are direct sums of copies of (5.1), so
(5.2) gives
$$
A_N\#B_N=\frac1{\sqrt{4+t_N^2}}\begin{pmatrix}2I_m&t_Ne_NI_m\\t_Ne_NI_m&(2+t_N^2)e_N^2I_m\end{pmatrix}\oplus e_N^2I_{d_N},\tag{6.3}
$$
and in particular
$$
\|A_N\#B_N-c(t_N)P_N\|\le\frac{t_Ne_N+(2+t_N^2)e_N^2}{\sqrt{4+t_N^2}}+e_N^2\to0.\tag{6.4}
$$

**A wrong output symbol.** With $t_N=3/2$, (6.4), (G2) and (G3) give
$$
\{A_N\}\sim_{\rm GLT}a,\qquad\{B_N\}\sim_{\rm GLT}a,\qquad\{A_N\#B_N\}\sim_{\rm GLT}\tfrac45a,\tag{6.5}
$$
whereas $(a\cdot a)^{1/2}=a$, and the regularised mean of the symbols
(the candidate in Conjecture 1 of [17]) is also $a$.

**No output distribution.** With $t_N=0$ for even $N$ and $t_N=3/2$ for
odd $N$, the normalised trace is exactly
$$
\frac1N\operatorname{tr}(A_N\#B_N)=\frac mN\cdot\frac{2+(2+t_N^2)e_N^2}{\sqrt{4+t_N^2}}+\frac{d_N}{N}e_N^2,\tag{6.6}
$$
which tends to $1/2$ along even $N$ and to $2/5$ along odd $N$. The
empirical eigenvalue distributions tend to $\tfrac12\delta_0+\tfrac12\delta_1$
and $\tfrac12\delta_0+\tfrac12\delta_{4/5}$ respectively. Since the
means are uniformly bounded, a continuous compactly supported test
function equal to $x$ on a common spectral interval distinguishes the
two limits, so $\{A_N\#B_N\}$ has no eigenvalue distribution and, by
(G1), is not GLT at all. The sequence is defined at every size $N$.

## 6.3. The statements refuted, and where the proof fails

*arXiv version.* We read arXiv:2505.03256v1 of [17] in full. Its
Theorem 4 (printed p. 11) reads, in part: "Let $r = 1$ and $d \ge 1$. Assume
$\{A_n\}_n\sim_{\rm GLT}\kappa$ and $\{B_n\}_n\sim_{\rm GLT}\xi$, where
$A_n,B_n\in\mathcal P_{\nu(n)}$ for every multi-index $n$. Then
$\{G(A_n,B_n)\}_n\sim_{\rm GLT}(\kappa\xi)^{1/2}$", where
$\mathcal P_{\nu(n)}$ denotes the HPD matrices of that size and $G$ the
geometric mean; a spectral-distribution relation is also asserted. No
boundedness, structure or regularisation hypothesis is made. The
sequences (6.1) satisfy these hypotheses with $d=1$ and $\kappa=\xi=a$,
so (6.5) contradicts Theorem 4. Conjecture 1 (printed p. 21) begins:
"Let $\{A_n\}_n$ and $\{B_n\}_n$ be Hermitian positive definite GLT
matrix-sequences with $\{A_n\}_n\sim_{\rm GLT}\kappa$,
$\{B_n\}_n\sim_{\rm GLT}\xi$. Then the geometric mean matrix-sequence
is again GLT", with the candidate symbol of Definition 3, equation (4.5)
(p. 21), the regularised mean of the symbols. For $\kappa=\xi=a$ the
candidate is $a$, so (6.5) and the alternating example contradict it.
*Warning on numbering:* the arXiv version's "Theorem 3" is a
restatement of the earlier, correct result of Ahmad et al. [16]
(which assumes that one symbol is nonzero almost everywhere); it is not
affected.

*Published version* (Linear Algebra Appl., 2025,
doi:10.1016/j.laa.2025.08.004). The scalar theorem is Theorem 3
(statement from p. 8, proof from p. 9); Conjecture 1 is on p. 19, with
the extended mean in Definition 3, equation (4.5), p. 18. Our own source
record transcribed only short passages verbatim. A separate AI-assisted
reading of the published institutional full text confirmed that the
hypotheses of published Theorem 3 (pp. 8--9) and of Conjecture 1 (p. 19)
admit the examples above, and that the published proof contains the
identification attacked below (p. 10). We record this as an AI-assisted
reading, not a transcription; readers can check the cited pages. In
both versions, after showing that the shifted means
$\{G(A_n+\varepsilon I,B_n)\}$ form an a.c.s. for a limit sequence, the
proof asserts (published p. 10; arXiv p. 12, where the text has "in the
a.c.s. topology")

> "and this limit coincides with $\{G(A_n,B_n)\}_n$ in a.c.s. topology".

The examples show that this identification is false. Concretely, in the
arXiv proof the limit sequence is $\{(A_nB_n^2A_n)^{1/4}\}$, and any
argument identifying it with $\{G(A_n,B_n)\}$ up to a zero-distributed
sequence must fail here: in (6.1) with $t_N=3/2$ we have
$(A_NB_N^2A_N)^{1/4}\to P_N$ in norm (the blocks converge uniformly and
$x\mapsto x^{1/4}$ is continuous on bounded positive matrices), while
$A_N\#B_N\to\tfrac45P_N$; the difference $\tfrac15P_N$ has rank $m\sim N/2$
and is not zero-distributed. The same problem affects the heuristic
given for Conjecture 1, which shifts both inputs and passes to the limit
$\varepsilon\to0$ after $n\to\infty$.

**Related statements.** Immediately before its Theorem 3 the published
article states that the result proves a Conjecture 10.1, in the words
"thus proving [21], Conjecture 10.1." (p. 8; the "[21]" is that article's own reference number); Khan's thesis [18]
attributes this conjecture to the Garoni--Serra-Capizzano monograph
[12] immediately before its Theorem 5.2 (printed p. 66). We could not
access the relevant pages of the monograph and do not quote or claim to
refute its Conjecture 10.1 as worded there. If, as these later sources
indicate, it asserts the scalar symbol formula without a non-vanishing
hypothesis, then the examples above refute it. The thesis presents its
Theorem 5.2 (printed p. 66), whose conclusion reads
"$\{G(A_n,B_n)\}_n\sim_{\rm GLT}(\kappa\xi)^{1/2}$", as the same
unrestricted scalar result, and its Conjecture 5.2.1 (printed p. 77,
candidate mean in Definition 3, equation (5.13), p. 76) states "Then
the geometric mean matrix-sequence is again GLT and" the candidate
formula; both are affected in the same way. The restricted theorem of
Ahmad et al. ([16], Theorem 3, p. 10, attributed there to
Theorem 10.2 of [12]), with the hypothesis "Assume that at least one
between $\kappa$ and $\xi$ is nonzero almost everywhere.", is not
contradicted: in (6.1) both symbols vanish on $(1/2,1]$.

## 6.4. How structured are the counterexamples?

**Remark 6.1 (the perturbation is small but non-local).** The
perturbation of $P_N$ in (6.1) has norm $O(1/N)$, so it is invisible to
the symbol; but the off-diagonal block couples the sample point $x$ with
$x+1/2$. It is therefore not of the form $g(n)T_n(f)$ with a fixed
symbol $f$ and $g(n)\to0$, which is the kind of small-norm term that
arises in discretisations. The refutation is of the theorems as stated,
which allow any HPD GLT sequences.

**Remark 6.2 (a fully structured block counterexample).** With $2\times2$
symbols ($r=2$) no permutation is needed. Let
$$
\mathcal A_n=I_n\otimes A_{e_n},\qquad\mathcal B_n=I_n\otimes B_{e_n,t},\qquad e_n\to0,\ t=3/2 .
$$
For a constant matrix $F$ the block Toeplitz matrix $T_n(F)$ is
$I_n\otimes F$, so $\mathcal A_n=T_n(F_0)+e_n^2T_n(F_2)$ and
$\mathcal B_n=T_n(F_0)+e_nt\,T_n(F_1)+e_n^2(1+t^2)T_n(F_2)$ with
$F_0=\operatorname{diag}(1,0)$,
$F_1=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)$,
$F_2=\operatorname{diag}(0,1)$. Both sequences are HPD with the constant
symbol $F_0$, and the perturbations have exactly the traditional form
$g(n)T_n(f)$. By (5.2), $\mathcal A_n\#\mathcal B_n=I_n\otimes(A_{e_n}\#B_{e_n,t})$
has symbol $\tfrac45F_0$, whereas the candidate symbol of Conjecture 1
(and $(\kappa\xi)^{1/2}$ for these commuting symbols) is $F_0$. This
refutes the block form of Conjecture 1 natively, and also the block
theorem for commuting symbols in the arXiv version (Theorem 6, p. 13),
which we checked only in that version.

Whether closure holds for scalar sequences generated by fixed-symbol
Toeplitz matrices, diagonal samplings and terms $g(n)T_n(f)$ is open
(Section 10).

# 7. Arbitrary contraction data behind fixed symbols

**Theorem 4 (universal contraction realisation).** For every $N\ge2$
let $m=\lfloor N/2\rfloor$ and let $C^{(N)}$ be any Hermitian $m\times m$
matrix with $0\preceq C^{(N)}\preceq I_m$. There are positive definite
$A_N,B_N$ with
$$
\|A_N-P_N\|+\|B_N-P_N\|\to0,\qquad
\Bigl\|A_N\#B_N-\bigl(C^{(N)}\oplus0_{N-m}\bigr)\Bigr\|\to0,\tag{7.1}
$$
where $P_N=D_N(a)$ as in Section 6. In particular both input sequences
are GLT with symbol $a$, while the output can encode any contraction
sequence, including one with no spectral limit.

*Proof.* First let $N=2n$. Choose $0<\delta_n\le1$ with $\delta_n\to0$,
and put
$$
D_n=\frac{C^{(N)}+\delta_nI_n}{1+\delta_n},\qquad e_n=\delta_n^2,\qquad
T_n=2\bigl(D_n^{-2}-I_n\bigr)^{1/2}.\tag{7.2}
$$
Then $0\prec D_n\preceq I_n$, $\|D_n-C^{(N)}\|\le\delta_n$ and
$\|T_n\|\le2(1+\delta_n)/\delta_n$. Set
$$
A_N=\begin{pmatrix}I_n&0\\0&e_n^2I_n\end{pmatrix},\qquad
B_N=\begin{pmatrix}I_n&e_nT_n\\e_nT_n&e_n^2(I_n+T_n^2)\end{pmatrix}.\tag{7.3}
$$
The Schur complement of the upper-left block of $B_N$ is $e_n^2I_n$, so
$B_N\succ0$, and
$\|B_N-P_N\|\le e_n\|T_n\|+e_n^2(1+\|T_n\|^2)\le4\delta_n+16\delta_n^2+\delta_n^4\to0$.
All blocks are functions of $D_n$; diagonalising $D_n$ reduces the
mean to (5.2) with $t=$ the eigenvalues of $T_n$. Since
$\sqrt{4I+T_n^2}=2D_n^{-1}$ and $\tfrac12D_nT_n=(I-D_n^2)^{1/2}$,
$$
A_N\#B_N=\begin{pmatrix}D_n&e_n(I_n-D_n^2)^{1/2}\\e_n(I_n-D_n^2)^{1/2}&e_n^2(2D_n^{-1}-D_n)\end{pmatrix}.\tag{7.4}
$$
The off-diagonal blocks have norm at most $e_n$, and the lower-right
block at most $e_n^2(2(1+\delta_n)/\delta_n+1)\le5\delta_n^3$. With
$\|D_n-C^{(N)}\|\le\delta_n$ this gives (7.1). For $N=2n+1$ append one
coordinate on which $A_N$, $B_N$ and their mean all equal $e_n^2$; then
$P_N=\operatorname{diag}(I_n,0_{n+1})=D_N(a)$ still, and (7.1) follows
from the even case. $\square$

If $C^{(N)}$ has a limiting spectral law $\nu$, the means have law
$\tfrac12\nu+\tfrac12\delta_0$. Appendix A shows that this is the most
freedom possible at a projection of rank density $1/2$.

# 8. Closure when the sum symbol is positive definite

**Theorem 5.** Let $\{A_n\}$, $\{B_n\}$ be HPD (scalar or $r\times r$
block, unilevel or multilevel) GLT sequences of the same sizes with
symbols $\kappa$, $\xi$ (Hermitian positive semidefinite a.e.). If
$$
\Sigma:=\kappa+\xi\succ0\quad\text{almost everywhere},\tag{8.1}
$$
then
$$
\{A_n\#B_n\}\sim_{\rm GLT}\Sigma^{1/2}\bigl[H(I-H)\bigr]^{1/2}\Sigma^{1/2},\qquad H=\Sigma^{-1/2}\kappa\Sigma^{-1/2},\tag{8.2}
$$
and the right-hand side equals $\kappa\#\xi$ (defined by (2.3)) almost
everywhere; in the scalar case it is $\sqrt{\kappa\xi}$.

*Proof.* Put $S_n=A_n+B_n\succ0$ and $H_n=S_n^{-1/2}A_nS_n^{-1/2}$, so
that $0\prec H_n\prec I$. By (2.2) with $T=S_n^{1/2}$,
$$
A_n\#B_n=S_n^{1/2}\bigl(H_n\#(I-H_n)\bigr)S_n^{1/2}=S_n^{1/2}\bigl[H_n(I-H_n)\bigr]^{1/2}S_n^{1/2},\tag{8.3}
$$
because $H_n$ and $I-H_n$ commute. By (G4), $\{S_n\}\sim_{\rm GLT}\Sigma$.
Since $\Sigma$ is invertible a.e. and $S_n$ is invertible, (G5) gives
$\{S_n^{-1}\}=\{S_n^\dagger\}\sim_{\rm GLT}\Sigma^{-1}$. Applying (G6)
with $f(x)=\sqrt{\max(\operatorname{Re}x,0)}$ to the Hermitian sequences
$S_n$ and $S_n^{-1}$ gives $\{S_n^{1/2}\}\sim_{\rm GLT}\Sigma^{1/2}$ and
$\{S_n^{-1/2}\}=\{(S_n^{-1})^{1/2}\}\sim_{\rm GLT}\Sigma^{-1/2}$; no norm
bound is needed, although $S_n^{-1}$ may be unbounded. By (G4),
$\{H_n\}\sim_{\rm GLT}H$ and $\{H_n(I-H_n)\}\sim_{\rm GLT}H(I-H)$; the
matrices $H_n(I-H_n)$ are Hermitian because the factors commute. One more
application of (G6) and (G4) gives (8.2).

For the identification, fix a point where $\Sigma\succ0$ and apply (8.3)
to $\kappa+\varepsilon I$, $\xi+\varepsilon I$: their sum
$\Sigma+2\varepsilon I$ tends to $\Sigma\succ0$, so every factor
converges (the inverse square root at the invertible limit, and the
square root on the closed positive cone), and the limit is the right
side of (8.2). By (2.3) the left side tends to $\kappa\#\xi$. $\square$

The sum normalisation (8.3) is standard (it is the coordinate used by
Jones [19], §4.12); the content of Theorem 5 is its GLT transfer.
Hypothesis (8.1) is weaker than invertibility of one entire symbol:
complementary indicator symbols satisfy it although neither is
invertible a.e.

**Corollary 6 (every Kubo--Ando mean).** Under the hypotheses of
Theorem 5, let $\sigma$ be a Kubo--Ando mean with representing function
$f$ (positive and operator monotone on $(0,\infty)$), so that
$A\sigma B=A^{1/2}f(A^{-1/2}BA^{-1/2})A^{1/2}$ for $A,B\succ0$. Define
$$
\phi(t)=t\,f\Bigl(\frac{1-t}{t}\Bigr)\ (0<t<1),\qquad
\phi(0)=\lim_{u\to\infty}\frac{f(u)}u,\qquad\phi(1)=f(0+),\tag{8.4}
$$
and extend $\phi$ to $\mathbb R$ by the constant $\phi(0)$ on
$(-\infty,0]$ and $\phi(1)$ on $[1,\infty)$, and to $\mathbb C$ by
$z\mapsto\phi(\operatorname{Re}z)$. Then
$\{A_n\sigma B_n\}\sim_{\rm GLT}\Sigma^{1/2}\phi(H)\Sigma^{1/2}=\kappa\sigma\xi$.

*Proof.* A positive operator monotone function is concave and
nondecreasing, so $f(0+)$ exists and $f(u)/u$ is nonincreasing and
nonnegative, so its limit at $\infty$ exists; with $u=(1-t)/t$,
$\phi(t)=f(u)/(1+u)$, so $\phi$ is continuous on $[0,1]$, and its
extension is continuous on $\mathbb C$, as (G6) requires. (The normalisation $f(1)=1$ is
not needed.) Congruence invariance gives
$A_n\sigma B_n=S_n^{1/2}\phi(H_n)S_n^{1/2}$, and the proof of Theorem 5
applies with (G6) for $\phi$; the spectra of $H_n$ lie in $(0,1)$, so
the extension does not change $\phi(H_n)$. The identification with the
regularised mean is as before. $\square$

# 9. One-sided domination and a sharp dichotomy

The common shift in (2.3) produces an *upper* bound by monotonicity.
At the level of matrix-sequences this gives a one-sided theorem that
holds with no hypothesis on the symbols.

Notation: for a $d$-level, $r\times r$ block sequence of size $d_n$, the
symbols are defined on $D=[0,1]^d\times[-\pi,\pi]^d$. For a measurable
Hermitian-positive-semidefinite-valued $g$ on $D$ let $\nu_g$ be the
probability measure on $[0,\infty)$ given by
$\nu_g(E)=\frac1{(2\pi)^dr}\int_D\#\{i:\lambda_i(g(x,\theta))\in E\}\,dx\,d\theta$,
and write $\mu_n$ for the empirical eigenvalue measure of an $n$-th
matrix.

**Theorem 7 (the regularised symbol is a universal upper envelope).**
Let $\{A_n\}\sim_{\rm GLT}\kappa$ and $\{B_n\}\sim_{\rm GLT}\xi$ be HPD
(scalar or block, uni- or multilevel) and $G_n=A_n\#B_n$. Let
$\gamma=\kappa\#\xi$ pointwise, as in (2.3). Then:

(a) for every $\delta>0$,
$$
\limsup_{n\to\infty}\frac1{d_n}\#\{j:\lambda_j(G_n)\ge\delta\}\le\nu_\gamma([\delta,\infty));\tag{9.1}
$$
(b) the measures $\mu_n$ of $G_n$ are tight, and every subsequential weak
limit $\nu$ is stochastically dominated by $\nu_\gamma$:
$\nu((\delta,\infty))\le\nu_\gamma((\delta,\infty))$ for every
$\delta\in\mathbb R$.

In words: the eigenvalues of the means can lose mass relative to the
regularised symbol, but never gain it.

*Proof.* (a) Fix $\varepsilon>0$. The sequence $\{\varepsilon I\}$ is
GLT with symbol $\varepsilon I_r$, so by (G4)
$\{A_n+\varepsilon I\}\sim_{\rm GLT}\kappa+\varepsilon I$ and similarly
for $B_n$. The sum symbol is $\succeq2\varepsilon I\succ0$, so Theorem 5
gives $\{G_n^\varepsilon\}\sim_{\rm GLT}\gamma_\varepsilon$, where
$G_n^\varepsilon=(A_n+\varepsilon I)\#(B_n+\varepsilon I)$ and
$\gamma_\varepsilon=(\kappa+\varepsilon I)\#(\xi+\varepsilon I)$. By
(G1) the empirical measures $\mu^\varepsilon_n$ of $G_n^\varepsilon$
converge vaguely to the probability measure $\nu_{\gamma_\varepsilon}$
($\gamma_\varepsilon$ is finite a.e.); vague convergence of probability
measures to a probability measure is weak convergence. Monotonicity of
$\#$ gives $G_n\preceq G_n^\varepsilon$, so by Weyl's monotonicity
principle the $j$-th largest eigenvalues satisfy
$\lambda_j^\downarrow(G_n)\le\lambda_j^\downarrow(G_n^\varepsilon)$ and
hence
$\#\{j:\lambda_j(G_n)\ge\delta\}\le\#\{j:\lambda_j(G_n^\varepsilon)\ge\delta\}$.
By the portmanteau theorem for the closed set $[\delta,\infty)$,
$$
\limsup_n\frac1{d_n}\#\{j:\lambda_j(G_n)\ge\delta\}\le\limsup_n\mu^\varepsilon_n([\delta,\infty))\le\nu_{\gamma_\varepsilon}([\delta,\infty)).
$$
Now let $\varepsilon\downarrow0$. At every point, $\gamma_\varepsilon$
decreases to $\gamma$ in the Loewner order, so the ordered eigenvalues
satisfy $\lambda_i(\gamma_\varepsilon)\ge\lambda_i(\gamma)$ and, by
continuity of ordered eigenvalues, $\lambda_i(\gamma_\varepsilon)\to\lambda_i(\gamma)$.
Hence $\mathbf 1\{\lambda_i(\gamma_\varepsilon)\ge\delta\}\to\mathbf 1\{\lambda_i(\gamma)\ge\delta\}$
pointwise: if $\lambda_i(\gamma)\ge\delta$ both indicators equal $1$ for
every $\varepsilon$, and if $\lambda_i(\gamma)<\delta$ the first is
eventually $0$. No assumption on where $\kappa$ or $\xi$ vanishes is
needed. Dominated convergence gives
$\nu_{\gamma_\varepsilon}([\delta,\infty))\to\nu_\gamma([\delta,\infty))$,
which proves (9.1).

(b) Since $G_n\succ0$ and (9.1) with $\delta=M$ tends to $0$ as
$M\to\infty$ ($\gamma$ is finite a.e.), the $\mu_n$ are tight. Let
$\nu$ be a subsequential weak limit and $\delta'>0$. The portmanteau
theorem for the open set $(\delta',\infty)$ and (9.1) give
$\nu((\delta',\infty))\le\liminf\mu_n((\delta',\infty))\le\nu_\gamma([\delta',\infty))$.
For $\delta\ge0$ and $\delta'\downarrow\delta$, the left side increases to
$\nu((\delta,\infty))$ and the right side increases to
$\nu_\gamma((\delta,\infty))$, since the sets $[\delta',\infty)$
increase to $(\delta,\infty)$. For $\delta<0$ both sides equal $1$.
$\square$

The fixed-dimensional analogue (every limit point lies below $A\#B$) is
Lemma 2.1(a) and Jones's Lemma 4.12.1(b) [19], whose proof uses the
same shift. The published article of Ilyas et al. calls one of its
own results maximal, in the sense of its conclusion (p. 27): "This shows
that Theorem 5 is maximal" (their Theorem 5, pp. 10--11, whose statement
we did not transcribe); our source record located no one-sided
spectral comparison between $G(A_n,B_n)$ and $(\kappa\xi)^{1/2}$ there,
so we present Theorem 7 as new, within the bounds of that check.

**Corollary 8 (disjoint supports give closure).** If $\kappa\#\xi=0$
almost everywhere, then $\{A_n\#B_n\}$ is zero-distributed, hence
$\{A_n\#B_n\}\sim_{\rm GLT}0=\kappa\#\xi$. By Lemma 2.1(b) the hypothesis
means $\operatorname{ran}\kappa\cap\operatorname{ran}\xi=\{0\}$ a.e.;
for scalar symbols it means $\kappa\xi=0$ a.e.

*Proof.* Here $\nu_\gamma=\delta_0$, so (9.1) gives
$d_n^{-1}\#\{j:\lambda_j(G_n)\ge\delta\}\to0$ for every $\delta>0$. As
$G_n\succ0$, its singular values are its eigenvalues, so $\{G_n\}$ is
zero-distributed, and (G3) applies. $\square$

Together, Theorem 5 and Corollary 8 cover two situations; the next
theorem shows that, for scalar symbols of the space variable, nothing
else is safe.

**Theorem 9 (failure whenever a common zero set meets a common
support).** Let $d\ge1$ and let $\kappa,\xi:[0,1]^d\to[0,\infty)$ be
bounded and Riemann integrable, regarded as GLT symbols independent of
$\theta$. Let $|\cdot|$ denote Lebesgue measure. If
$$
|\{\kappa+\xi=0\}|>0\qquad\text{and}\qquad|\{\kappa\xi>0\}|>0,\tag{9.2}
$$
then there are HPD sequences $\{A_n\}\sim_{\rm GLT}\kappa$ and
$\{B_n\}\sim_{\rm GLT}\xi$ with $\sup_n(\|A_n\|+\|B_n\|)<\infty$ such that

(i) $\limsup_n d_n^{-1}\operatorname{tr}(A_n\#B_n)<\int_{[0,1]^d}\sqrt{\kappa\xi}\,dx$,
so $\{A_n\#B_n\}$ is not GLT with symbol $\sqrt{\kappa\xi}$; and

(ii) after a modification along every other index, $\{A_n\#B_n\}$ has no
eigenvalue distribution at all.

*Proof.* We write the proof for $d=1$, sizes $n$ and sample points
$x_j=j/n$. For $d>1$ the sequence is indexed by multi-indices
$n=(n_1,\dots,n_d)$ with $\min_in_i\to\infty$, the sample points are
$x_j=j/n$ (componentwise) for $j$ in the grid $\{1,\dots,n_1\}\times\dots\times\{1,\dots,n_d\}$,
and the size is $N(n)=n_1\cdots n_d$. The proof uses only two facts
about the grid, and both hold for $d>1$: Riemann sums of a
Riemann-integrable function on $[0,1]^d$ over this grid converge to its
integral, because the mesh $\max_i1/n_i$ tends to zero; and diagonal
sampling of a Riemann-integrable function has that function as symbol
(the multilevel form of (G2), [15], Theorem 4.23). With $n$ replaced
by $N(n)$ and index sets taken in the grid, every step below holds
verbatim. Let $K\ge\sup(\kappa+\xi)$, $K\ge1$,
and write $\kappa_j=\kappa(x_j)$, $\xi_j=\xi(x_j)$, $s_j=\sqrt{\kappa_j\xi_j}$.

*Step 1: counting sample indices.* For continuous bounded
$F:\mathbb R^2\to\mathbb R$ the function $F(\kappa,\xi)$ is bounded and
continuous wherever both $\kappa$ and $\xi$ are, hence Riemann
integrable, so $n^{-1}\sum_jF(\kappa_j,\xi_j)\to\int_0^1F(\kappa,\xi)$.
Thus the empirical law of the pairs $(\kappa_j,\xi_j)$ converges weakly
to the law $\pi$ of $(\kappa(x),\xi(x))$ under Lebesgue measure, and the
portmanteau theorem gives $\liminf_n\pi_n(U)\ge\pi(U)$ for open
$U\subset\mathbb R^2$. (No continuity-point condition is needed for open
sets.) Put $z=|\{\kappa+\xi=0\}|>0$ and choose $\eta_0>0$ with
$w=|\{\kappa\xi>\eta_0\}|>0$, which is possible by (9.2) and continuity
of measure. Applying the portmanteau inequality to
$U_\eta=\{u<\eta,\ v<\eta\}$ (for each fixed $\eta>0$,
$\pi(U_\eta)\ge z$) and to $V=\{uv>\eta_0\}$ ($\pi(V)=w$), and
choosing $\eta_n\downarrow0$ slowly by a diagonal argument, we get for
all large $n$:
$$
\#J^0_n\ge\tfrac z2n,\quad J^0_n=\{j:\kappa_j<\eta_n,\ \xi_j<\eta_n\};\qquad
\#J^1_n\ge\tfrac w2n,\quad J^1_n=\{j:\kappa_j\xi_j>\eta_0\}.
$$
For large $n$ also $\eta_n^2<\eta_0$, so $J^0_n\cap J^1_n=\emptyset$.
Let $c_0=\min(z,w)/3$ and $m_n=\lfloor c_0n\rfloor$, and choose distinct
$p_1,\dots,p_{m_n}\in J^1_n$ and $q_1,\dots,q_{m_n}\in J^0_n$. (For the
finitely many small $n$ where this is impossible, take $m_n=0$.)

*Step 2: the sequences.* Let $e_n=1/n$ and fix $t\ge0$. Define $A_n$
and $B_n$ as follows. On each pair of coordinates $(p_i,q_i)$ put the
$2\times2$ blocks $\kappa_{p_i}A_{e_n}$ and $\xi_{p_i}B_{e_n,t}$ from
(5.1). On every unpaired coordinate $j$ put the diagonal entries
$\tilde\kappa_j=\max(\kappa_j,e_n^2)$ and $\tilde\xi_j=\max(\xi_j,e_n^2)$.
All other entries are zero. Since $\kappa_{p_i},\xi_{p_i}>0$, both
matrices are HPD. Compared with $D_n(\kappa)$ and $D_n(\xi)$, the
changes form, after a permutation, a direct sum of $1\times1$ and
$2\times2$ blocks, so
$$
\|A_n-D_n(\kappa)\|\le Ke_n^2+\eta_n,\qquad\|B_n-D_n(\xi)\|\le Kte_n+K(1+t^2)e_n^2+\eta_n+e_n^2,
$$
both tending to $0$. By (G2) and (G3), $\{A_n\}\sim_{\rm GLT}\kappa$ and
$\{B_n\}\sim_{\rm GLT}\xi$, and the norms are uniformly bounded.

*Step 3: the trace.* By (2.2) and (5.2) the mean is the direct sum of
the scalars $\sqrt{\tilde\kappa_j\tilde\xi_j}$ and of the blocks
$s_{p_i}(A_{e_n}\#B_{e_n,t})$, whose trace is
$s_{p_i}c(t)\bigl(1+(1+t^2/2)e_n^2\bigr)$. Using
$\sqrt a-\sqrt b\le\sqrt{a-b}$ for $a\ge b\ge0$ and
$\tilde\kappa_j\tilde\xi_j-\kappa_j\xi_j\le e_n^2(\kappa_j+\xi_j)+e_n^4\le e_n^2(K+1)$, we get
$$
\frac{\operatorname{tr}(A_n\#B_n)}n-\frac1n\sum_{j=1}^ns_j
\le e_n\sqrt{K+1}+\frac1n\sum_{i=1}^{m_n}s_{p_i}\Bigl[c(t)\bigl(1+(1+\tfrac{t^2}2)e_n^2\bigr)-1\Bigr],\tag{9.3}
$$
where the terms $s_{q_i}\ge0$ of the Riemann sum were dropped. Take
$t=3/2$, so $c(t)=4/5$. For large $n$ the bracket is at most $-1/10$,
and $s_{p_i}>\sqrt{\eta_0}$, so
$$
\limsup_n\frac{\operatorname{tr}(A_n\#B_n)}n\le\int_0^1\sqrt{\kappa\xi}\,dx-\frac{c_0\sqrt{\eta_0}}{10}<\int_0^1\sqrt{\kappa\xi}\,dx,
$$
because $\sqrt{\kappa\xi}$ is Riemann integrable. If
$\{A_n\#B_n\}\sim_{\rm GLT}\sqrt{\kappa\xi}$, then by (G1), the uniform
bound $\|A_n\#B_n\|\le(\|A_n\|+\|B_n\|)/2$, and a continuous compactly
supported test function equal to $x$ on the spectra, the normalised
traces would converge to $\int_0^1\sqrt{\kappa\xi}$. This proves (i).

(ii) Use $t=0$ for even $n$ and $t=3/2$ for odd $n$. For $t=0$,
$B_{e,0}=A_e$ and the block mean is $s_{p_i}A_{e_n}$, so the
left side of (9.3) lies between $-\frac1n\sum_is_{q_i}\ge-\eta_n$ and
$e_n\sqrt{K+1}+Ke_n^2$; the normalised traces tend to
$\int\sqrt{\kappa\xi}$ along even $n$, but stay below it by a fixed
amount along odd $n$. Since the means are uniformly bounded, they have
no eigenvalue distribution. $\square$

**Corollary 10 (dichotomy).** Let $\kappa,\xi\ge0$ be bounded,
Riemann-integrable functions on $[0,1]^d$, regarded as scalar GLT
symbols independent of $\theta$. Then the following are equivalent:

1. for every pair of HPD sequences $\{A_n\}\sim_{\rm GLT}\kappa$,
   $\{B_n\}\sim_{\rm GLT}\xi$, one has $\{A_n\#B_n\}\sim_{\rm GLT}\sqrt{\kappa\xi}$;
2. $|\{\kappa+\xi=0\}|=0$ or $|\{\kappa\xi>0\}|=0$.

*Proof.* If $|\{\kappa+\xi=0\}|=0$, Theorem 5 applies; if
$|\{\kappa\xi>0\}|=0$, Corollary 8 applies. Otherwise Theorem 9 gives a
counterexample. $\square$

For arbitrary scalar or block GLT symbols, depending on $(x,\theta)$,
the formula holds if $\kappa+\xi\succ0$ almost everywhere (Theorem 5) or
$\kappa\#\xi=0$ almost everywhere (Corollary 8). For bounded
Riemann-integrable scalar symbols depending only on $x$, these
conditions are also necessary for the formula to hold for every HPD
realisation (Corollary 10). For scalar symbols the two conditions mean
"no common zero set of positive measure" and "essentially disjoint
supports". For block symbols they mean $\ker\kappa\cap\ker\xi=\{0\}$ and
$\operatorname{ran}\kappa\cap\operatorname{ran}\xi=\{0\}$ almost
everywhere; neither is implied by the absence of a common zero set (for
example $\kappa=\xi=\operatorname{diag}(1,0)$ everywhere, as in Remark
6.2). Necessity for symbols depending on $\theta$, and for block
symbols, is open.

> **When is the symbol formula safe?**
>
> * *Safe:* $\kappa+\xi\succ0$ almost everywhere (Theorem 5). For scalar
>   symbols this says the two symbols have no common zero set of positive
>   measure; isolated zeros, such as $\theta=0$ for a Laplacian, are
>   harmless. For block symbols it says $\ker\kappa\cap\ker\xi=\{0\}$
>   a.e. The same holds for every Kubo--Ando mean (Corollary 6).
> * *Safe:* $\kappa\#\xi=0$ almost everywhere (Corollary 8): for scalar
>   symbols, essentially disjoint supports; for block symbols, trivial
>   intersection of the ranges a.e. The means are then zero-distributed.
> * *Always true:* the eigenvalues of the means never exceed what the
>   regularised symbol $\kappa\#\xi$ predicts, in the sense of
>   stochastic domination (Theorem 7).
> * *Unsafe (proved for bounded Riemann-integrable scalar symbols of $x$;
>   open in general):* a common zero region of positive measure together
>   with a common support of positive measure (Theorem 9). Typical
>   sources are degenerate diffusion with coefficients vanishing on a
>   subdomain, masked or windowed operators, and covariance models that
>   share a null space. Couplings of size $O(1/N)$ between range and
>   kernel, comparable to discretisation error, then decide the output.
>   For inputs approaching projections, Theorem 4 and Appendix A show
>   that the output spectrum can be anywhere in the envelope (A.1).
> * In the unsafe case no numerical test on the symbols can certify the
>   formula: the counterexample inputs are indistinguishable from "good"
>   ones at the symbol level.

# 10. Conclusion and open problems

The boundary behaviour of the matrix geometric mean is governed by one
rank inequality (Theorem 1). Limits of means sit below the regularised
mean and can be anything in the rank-constrained part of Ando's feasible
set. In geometric terms: the midpoint of the affine-invariant geodesic
between two positive definite matrices is not determined by the
endpoints once these reach the boundary of the cone, which is one reason
why fixed-rank geometries must be built separately [25] (we claim
no equivalence with those constructions). For GLT sequences with
arbitrary scalar or block symbols, the symbol formula holds if
$\kappa+\xi\succ0$ almost everywhere or $\kappa\#\xi=0$ almost
everywhere, and in every case the regularised symbol is an upper
envelope (Theorem 7). For bounded Riemann-integrable scalar symbols
depending only on $x$, these conditions are also necessary for the
formula to hold for every HPD realisation. Theorem 4 and Appendix A
describe the attainable output freedom for inputs approaching
projections.

\needspace{8\baselineskip}

Open problems:

1. *Structured classes.* Does closure hold for scalar sequences in the
   algebra generated by fixed-symbol Toeplitz matrices $T_n(f)$,
   diagonal samplings $D_n(a)$ and small terms $g(n)T_n(f)$? Our scalar
   counterexamples need a non-local coupling (Remark 6.1); heuristically,
   fixed-symbol operators couple $\{a=1\}$ and $\{a=0\}$ only through
   $o(n)$ effective rank.
2. *Extra data.* Which asymptotic data beyond the two symbols, for
   example a joint symbol of the coupling between range and common
   kernel at scale $1/N$, determine the output symbol? Appendix A and
   Theorem 4 suggest a contraction-valued field.
3. *The general dichotomy.* Extend Corollary 10 to symbols depending on
   $(x,\theta)$ and to block symbols.
4. *Exact output sets.* Characterise all limiting spectral laws of
   $A_n\#B_n$ for given input symbols, extending Appendix A from
   projections to general symbols.
5. *Other means.* Rank-type descriptions of the boundary limits of the
   harmonic mean, the weighted means $\#_t$, other Kubo--Ando means and
   Karcher means of more than two matrices; a quantitative version of
   Theorem 1 controlling the distance to the set of limits.

# 11. Verification, scope and novelty boundary

**Proofs.** Every result above has a complete written proof. The
quantified statements (all matrices, all dimensions, all sequences)
rest on those proofs.

**Exact checks.** The script `verify_exact.py` (Python standard library
only; output written to a path given on the command line) performs
1,030 exact checks in rational and Gaussian-rational arithmetic:
formula (5.2) for many $(e,t)$; the construction of Section 3.3 on
complex, non-commuting data (including empty blocks), mapped through
fixed complex congruences, with the support property (3.2), the rank
identity (3.3), exactness of every approximating mean via (2.1), and
strictly decreasing errors consistent with $O(\delta)$; the role of
each condition in Theorem 1; Corollaries 2--3 on complex data,
including the lower endpoint; formula (7.4) under complex unitary
conjugation, with odd-size padding; the assemblies (6.1)--(6.6) for
$N=2,\dots,14$; finite instances of a variant of the construction of
Theorem 9 (for $\kappa=4x$, $\xi=x$ on $(0,1/2]$, both zero on
$(1/2,1]$, with $\eta_0=1/16$ and $\lfloor3n/16\rfloor$ pairs taken from
the smallest admissible indices instead of the proof's
$\lfloor c_0n\rfloor$, $n=16,\dots,256$; the paired blocks are checked
exactly and the trace is summed block by block; the normalised traces
approach $299/1280<1/4=\int\sqrt{\kappa\xi}$); and the
block example of Remark 6.2. Each check raises an error on failure (no
`assert` statements, so `python -O` does not disable them), and the
option `--self-test-mutation` corrupts formula (5.2) to show that the
failure is detected. These checks test identities and finite
assemblies; they do not test limits or quantifiers.

**Sources.** The arXiv version of [17], the thesis [18], the
article [16] and the two ETNA papers [14], [15] were
accessible. For the published version of [17] the relevant locations
and the short passages quoted above were verified; in addition, a
separate AI-assisted reading of the published full text confirmed that
the hypotheses of its Theorem 3 (pp. 8--9) and Conjecture 1 (p. 19)
admit our examples and that its proof contains the attacked
identification (p. 10). The published statements were not transcribed
in full (Section 6.3). The 2017 monograph
[12] was not accessible, so the status of its Conjecture 10.1 is
stated conditionally. Jones [19] is a self-hosted, book-length
preprint dated October 2026; only §4.12 (printed pp. 105--110) was read
in detail.

**Novelty.** A dated, bounded literature search (recorded in
`source_novelty_ledger.md` and `novelty_report.md`) found no earlier
statement of the rank criterion (2.4), of the GLT counterexamples, of
Theorems 4, 7 and 9, or of Appendix A. This does not establish
priority. The discontinuity mechanism, the maximal characterisation, the
envelope $X\preceq A\#B$, the dilation description of the set of
limits and the sum normalisation are earlier work and are credited
above. A public AI-generated review on Pith, dated 15 August 2026
(<https://pith.science/paper/2505.03256>), had already questioned the
a.c.s. step in the arXiv version without giving a counterexample; we
claim no priority for noticing a possible gap. We have not corresponded
with the authors of [17].

# Declarations

**Provenance and status.** This manuscript and its code were developed
with AI assistance (ChatGPT for the original draft; Claude-based agents
for the revision). Separate AI agents checked the proofs and the
literature. The work has not undergone independent human peer review or
formal proof-assistant verification. It is released as an unrefereed
candidate.

**Licence.** Text CC0-1.0; code MIT.

**Archive and DOI.** Version 0.1.0-candidate of this package (manuscript, code and records) is archived at Zenodo, DOI [10.5281/zenodo.23912963](https://doi.org/10.5281/zenodo.23912963) (all versions: DOI [10.5281/zenodo.23912962](https://doi.org/10.5281/zenodo.23912962)), and on GitHub at <https://github.com/ipitchford/matrix-geometric-mean-glt-closure>.

# Appendix A. A sharp spectral envelope at a projection

This appendix concerns growing dimensions. Let $P_N$ be orthogonal
projections on $\mathbb C^N$ of rank $r_N$, with $r_N/N\to p\in[0,1]$,
and $q_N=N-r_N$.

**Theorem A.1.** Let $A_N,B_N\succ0$ with
$\|A_N-P_N\|+\|B_N-P_N\|\to0$, and let $\mu_N$ be the empirical
eigenvalue measure of $X_N=A_N\#B_N$. Every weak subsequential limit of
$\mu_N$ has the form
$$
\mu=(1-p)\delta_0+(2p-1)_+\delta_1+\min(p,1-p)\,\nu,\tag{A.1}
$$
with $\nu$ a probability measure on $[0,1]$ (irrelevant when its
coefficient is $0$). Conversely, every measure of this form is the limit
of $\mu_N$ for suitable such $A_N,B_N$, for the given projections.

So a null space occupying a fraction $1-p$ of the dimension can alter at
most that fraction of the spectrum, and this is attained (Figure A.1).
At $p=1/2$ the whole nonzero half of the spectrum is undetermined; this is
Theorem 4.

![**Figure A.1.** The envelope (A.1): for each limiting rank fraction $p$, the share of eigenvalues of the mean forced to $0$, forced to $1$, and free to have any distribution on $[0,1]$.](figA1_spectral_envelope.pdf){width=70%}

*Proof of necessity.* Write $P_N=\operatorname{diag}(I_{r_N},0_{q_N})$
by a unitary change of basis. Since
$0\prec X_N\preceq(A_N+B_N)/2=P_N+o(1)$, the spectra are bounded; the
compression of $X_N$ to $\ker P_N$ is $o(1)$, and so is the
off-diagonal block, because $\|X_{12}\|^2\le\|X_{11}\|\,\|X_{22}\|$ for
a positive semidefinite block matrix. If both blocks are nonempty write
$A_N=\left(\begin{smallmatrix}a_N&b_N\\b_N^*&d_N\end{smallmatrix}\right)$
and
$T_N=\left(\begin{smallmatrix}a_N^{-1/2}&-a_N^{-1}b_N\\0&I\end{smallmatrix}\right)$.
Then $\|T_N-I\|\to0$ and
$T_N^*A_NT_N=\operatorname{diag}(I,S_N)$ with
$S_N=d_N-b_N^*a_N^{-1}b_N\succ0$. Put $Y_N=T_N^*X_NT_N$,
$Z_N=T_N^*B_NT_N$, and $C_N=(Y_N)_{11}$. Two implicit steps:
(i) $C_N\succeq0$, as a compression of the positive matrix $Y_N$;
(ii) $Y_N-X_N=o(1)$ because $T_N\to I$ and $X_N$ is bounded, so
$(Y_N)_{12}$ and $(Y_N)_{22}$ are $o(1)$ and
$X_N=\operatorname{diag}(C_N,0)+o(1)$. By (2.2),
$Y_N=\operatorname{diag}(I,S_N)\#Z_N$, and the $(1,1)$ block of (2.1)
gives
$$
(Z_N)_{11}-C_N^2=(Y_N)_{12}S_N^{-1}(Y_N)_{12}^*=:R_N\succeq0,\qquad\operatorname{rank}R_N\le q_N.
$$
Also $(Z_N)_{11}=I+E_N$ with $\|E_N\|\to0$, since $Z_N\to P_N$. Thus
$C_N^2=I-R_N+E_N$. The matrix $I-R_N$ has at least $(r_N-q_N)_+$
eigenvalues equal to $1$ and all eigenvalues at most $1$; by Weyl's
inequality, at least $(r_N-q_N)_+$ eigenvalues of $C_N^2$, hence (by
(i)) of $C_N$, are within $o(1)$ of $1$, and all lie in $[0,1+o(1)]$.
By (ii) and Weyl's inequality, $X_N$ has at least $q_N$ eigenvalues
within $o(1)$ of $0$ and, disjointly, at least $(r_N-q_N)_+$ within
$o(1)$ of $1$, and all its eigenvalues lie in $[-o(1),1+o(1)]$. If a
block is empty the same conclusions are immediate.

*Portmanteau step.* Let $\mu$ be a subsequential weak limit and
$\eta>0$. For the closed sets $[-\eta,\eta]$, $[1-\eta,1+\eta]$ and
$[-\eta,1+\eta]$, $\mu(F)\ge\limsup\mu_N(F)$ gives
$\mu([-\eta,\eta])\ge1-p$, $\mu([1-\eta,1+\eta])\ge(2p-1)_+$ and
$\mu([-\eta,1+\eta])=1$. Letting $\eta\downarrow0$,
$\mu(\{0\})\ge1-p$, $\mu(\{1\})\ge(2p-1)_+$ and $\mu$ is supported in
$[0,1]$. Since $(1-p)+(2p-1)_++\min(p,1-p)=1$, the measure
$\mu-(1-p)\delta_0-(2p-1)_+\delta_1\ge0$ has mass $\min(p,1-p)$ and is
supported in $[0,1]$, which is (A.1).

*Proof of attainability.* Let $d_N=\min(r_N,q_N)$, choose numbers
$c_{N,1},\dots,c_{N,d_N}\in[0,1]$ whose empirical measures tend to $\nu$
(when $d_N/N\to0$ nothing is needed), and pair $d_N$ range directions of
$P_N$ with $d_N$ null directions. Let $\eta_N\downarrow0$, $\eta_N\le1$,
and for each pair replace $c$ by $\hat c=(c+\eta_N)/(1+\eta_N)$, put
$t=2\sqrt{\hat c^{-2}-1}$ (so $\sqrt{4+t^2}=2/\hat c$ and
$t\le2(1+\eta_N)/\eta_N$), $\varepsilon_N=\eta_N^2$, and use the pair
$(A_{\varepsilon_N},B_{\varepsilon_N,t})$ of (5.1). Uniformly in
$c\in[0,1]$,
$\|B-\operatorname{diag}(1,0)\|\le\varepsilon_Nt+\varepsilon_N^2(1+t^2)\le21\eta_N$,
$\|A-\operatorname{diag}(1,0)\|=\eta_N^4$, and by (5.2)
$\|A\#B-\operatorname{diag}(c,0)\|\le|\hat c-c|+\varepsilon_Nt\hat c/2+\varepsilon_N^2(2+t^2)\hat c/2\le8\eta_N$.
On the remaining range directions take $A=B=1$, on the remaining null
directions $A=B=\varepsilon_N^2$. Direct sums preserve these uniform
bounds, and undoing the unitary change of basis completes the proof.
$\square$

For the special case of identical density matrices in fixed dimension
see Corollary 3.

# Appendix B. The dilation view and its relation to Theorem 1

This appendix records a general description without claiming priority
for it. Its attainability construction is Jones's Lemma 4.12.3
[19] (printed pp. 106--107), stated there for every Kubo--Ando
connection; the converse is an elementary compactness argument.

Fix $N$ and a Kubo--Ando mean $\sigma$ with function $\phi$ as in
(8.4). Given $A,B\succeq0$, apply a fixed invertible congruence so that
$$
S=A+B=P=I_s\oplus0_k,\qquad A=H\oplus0_k,\qquad B=(I_s-H)\oplus0_k,\qquad0\preceq H\preceq I_s.
$$
where $k=N-s$ is the dimension of the common kernel. Let $\mathcal C_\sigma(A,B)$ be the set of limits of $A_j\sigma B_j$ with
$A_j,B_j\succ0$, $(A_j,B_j)\to(A,B)$.

**Proposition B.1.** In these coordinates
$$
\mathcal C_\sigma(A,B)=\{P\phi(T)P:\ 0\preceq T\preceq I_N,\ PTP=H\oplus0_k\}.\tag{B.1}
$$

*Proof.* Necessity: with $S_j=A_j+B_j$ and
$T_j=S_j^{-1/2}A_jS_j^{-1/2}$, we have $0\prec T_j\prec I$, so a
subsequence converges to some $T$ with $0\preceq T\preceq I$; since
$S_j^{1/2}\to P$, $A=PTP$, and
$A_j\sigma B_j=S_j^{1/2}\phi(T_j)S_j^{1/2}\to P\phi(T)P$.
Attainability: for $0<\varepsilon<1/2$ put
$T_\varepsilon=(1-2\varepsilon)T+\varepsilon I$,
$S_\varepsilon=P+\varepsilon^2(I-P)$,
$A_\varepsilon=S_\varepsilon^{1/2}T_\varepsilon S_\varepsilon^{1/2}$ and
$B_\varepsilon=S_\varepsilon^{1/2}(I-T_\varepsilon)S_\varepsilon^{1/2}$.
Both are positive definite and tend to $A$, $B$, and
$A_\varepsilon\sigma B_\varepsilon=S_\varepsilon^{1/2}\phi(T_\varepsilon)S_\varepsilon^{1/2}\to P\phi(T)P$.
$\square$

**Relation to Theorem 1.** For $\sigma=\#$, $\phi(t)=\sqrt{t(1-t)}$.
One inclusion between (B.1) and condition 2 of Theorem 1 is immediate
through the factorisation $M=ZZ^*$: given $T$, put $F=PT^{1/2}$ and
$G=P(I-T)^{1/2}$. Then $FF^*=PTP=A$, $GG^*=P-PTP=B$, and
$FG^*=PT^{1/2}(I-T)^{1/2}P=P\phi(T)P=:X\succeq0$, so
$$
M(A,B,X)=\begin{pmatrix}F\\G\end{pmatrix}\begin{pmatrix}F\\G\end{pmatrix}^{\!*}\succeq0,\qquad\operatorname{rank}M(A,B,X)\le N.
$$
For the reverse inclusion we do not have a two-line elimination;
it follows by combining the two complete characterisations: condition
2 implies, by the construction of Section 3, that $X$ is a limit, and
Proposition B.1 then supplies $T$. Thus Theorem 1 is the closed form of
the dilation description for the geometric mean: it replaces the
existence of the auxiliary contraction $T$ by block positivity and one
rank inequality. Fixed dimension is essential to the compactness
argument; limits in growing dimension need separate estimates, as in
Appendix A.

# References

1. W. Pusz and S. L. Woronowicz. Functional calculus for sesquilinear forms and the purification map. *Reports on Mathematical Physics* 8(2) (1975) 159--170. DOI [10.1016/0034-4877(75)90061-0](https://doi.org/10.1016/0034-4877(75)90061-0).
2. F. Kubo and T. Ando. Means of positive linear operators. *Mathematische Annalen* 246(3) (1980) 205--224. DOI [10.1007/BF01371042](https://doi.org/10.1007/BF01371042).
3. T. Ando. Concavity of certain maps on positive definite matrices and applications to Hadamard products. *Linear Algebra and its Applications* 26 (1979) 203--241. DOI [10.1016/0024-3795(79)90179-4](https://doi.org/10.1016/0024-3795(79)90179-4).
4. J. D. Lawson and Y. Lim. The geometric mean, matrices, metrics, and more. *The American Mathematical Monthly* 108(9) (2001) 797--812. DOI [10.1080/00029890.2001.11919815](https://doi.org/10.1080/00029890.2001.11919815).
5. R. Bhatia. *Positive Definite Matrices*. Princeton University Press, 2007; e-book edition DOI [10.1515/9781400827787](https://doi.org/10.1515/9781400827787).
6. M. Moakher. A differential geometric approach to the geometric mean of symmetric positive-definite matrices. *SIAM Journal on Matrix Analysis and Applications* 26(3) (2005) 735--747. DOI [10.1137/S0895479803436937](https://doi.org/10.1137/S0895479803436937).
7. A. Barachant, S. Bonnet, M. Congedo and C. Jutten. Multiclass brain--computer interface classification by Riemannian geometry. *IEEE Transactions on Biomedical Engineering* 59(4) (2012) 920--928. DOI [10.1109/TBME.2011.2172210](https://doi.org/10.1109/TBME.2011.2172210).
8. D. A. Bini, B. Iannazzo, B. Jeuris and R. Vandebril. Geometric means of structured matrices. *BIT Numerical Mathematics* 54(1) (2014) 55--83 (online 2013). DOI [10.1007/s10543-013-0450-4](https://doi.org/10.1007/s10543-013-0450-4).
9. K. Matsumoto. Reverse test and quantum analogue of classical fidelity and generalized fidelity. arXiv [1006.0302](https://arxiv.org/abs/1006.0302) (2010).
10. K. Matsumoto. A new quantum version of f-divergence. In *Reality and Measurement in Algebraic Quantum Theory*, Springer Proceedings in Mathematics & Statistics, 2018, pp. 229--273. DOI [10.1007/978-981-13-2487-1_10](https://doi.org/10.1007/978-981-13-2487-1_10).
11. S. Cree and J. Sikora. A fidelity measure for quantum states based on the matrix geometric mean. arXiv [2006.06918v2](https://arxiv.org/abs/2006.06918) (2020; v2 2021).
12. C. Garoni and S. Serra-Capizzano. *Generalized Locally Toeplitz Sequences: Theory and Applications*, Vol. I. Springer, 2017. DOI [10.1007/978-3-319-53679-8](https://doi.org/10.1007/978-3-319-53679-8).
13. C. Garoni and S. Serra-Capizzano. *Generalized Locally Toeplitz Sequences: Theory and Applications*, Vol. II. Springer, 2018. DOI [10.1007/978-3-030-02233-4](https://doi.org/10.1007/978-3-030-02233-4).
14. G. Barbarino, C. Garoni and S. Serra-Capizzano. Block generalized locally Toeplitz sequences: theory and applications in the unidimensional case. *Electronic Transactions on Numerical Analysis* 53 (2020) 28--112. DOI [10.1553/etna_vol53s28](https://doi.org/10.1553/etna_vol53s28).
15. G. Barbarino, C. Garoni and S. Serra-Capizzano. Block generalized locally Toeplitz sequences: theory and applications in the multidimensional case. *Electronic Transactions on Numerical Analysis* 53 (2020) 113--216. DOI [10.1553/etna_vol53s113](https://doi.org/10.1553/etna_vol53s113).
16. D. Ahmad, M. F. Khan and S. Serra-Capizzano. Matrix-sequences of geometric means in the case of hidden (asymptotic) structures. *Mathematics* 13(3) (2025) 393. DOI [10.3390/math13030393](https://doi.org/10.3390/math13030393).
17. A. Ilyas, M. F. Khan, V. Loi and S. Serra-Capizzano. A maximal distribution result and numerical tests for geometric means of HPD GLT matrix-sequences with degenerate commuting/non-commuting GLT symbols. *Linear Algebra and its Applications* (2025, article in press; open access CC BY 4.0). DOI [10.1016/j.laa.2025.08.004](https://doi.org/10.1016/j.laa.2025.08.004). Preprint: Geometric means of HPD GLT matrix-sequences: a maximal result beyond invertibility assumptions on the GLT symbols, arXiv [2505.03256v1](https://arxiv.org/abs/2505.03256) (2025; first author listed there as "Asiim Ilyas").
18. M. F. Khan. *GLT matrix-sequences and few emblematic applications*. Doctoral thesis, arXiv [2511.06312](https://arxiv.org/abs/2511.06312) (2025).
19. M. Jones. *Continuity, Testing Regions and Fragility of Quantum Channel Divergences*. Self-hosted book-length preprint, version 1, October 2026 (title page), §4.12, printed pp. 105--110. <https://hexagonmath.org/pdf/2610.00611v1>. Not peer reviewed; not indexed in Crossref or arXiv.
20. J. Poulson. Equilibrating low-rank approximations. Lecture slides, MolSSI/ELSI workshop, 2018, slide 9 (secondary source for the classical example attributed to Bhatia). <https://wordpress.elsi-interchange.org/wp-content/uploads/2018/08/Poulson_Jack-MolSSI_ELSI_2018-Richmond.pdf>.
21. W. N. Anderson, Jr. and G. E. Trapp. Shorted operators. II. *SIAM Journal on Applied Mathematics* 28(1) (1975) 60--71. DOI [10.1137/0128007](https://doi.org/10.1137/0128007).
22. A. Uhlmann. The "transition probability" in the state space of a $*$-algebra. *Reports on Mathematical Physics* 9(2) (1976) 273--279. DOI [10.1016/0034-4877(76)90060-4](https://doi.org/10.1016/0034-4877(76)90060-4).
23. S. Serra-Capizzano. Distribution results on the algebra generated by Toeplitz sequences: a finite-dimensional approach. *Linear Algebra and its Applications* 328(1--3) (2001) 121--130. DOI [10.1016/S0024-3795(00)00311-6](https://doi.org/10.1016/S0024-3795(00)00311-6).
24. C. Garoni. Topological foundations of an asymptotic approximation theory for sequences of matrices with increasing size. *Linear Algebra and its Applications* 513 (2017) 324--341. DOI [10.1016/j.laa.2016.10.021](https://doi.org/10.1016/j.laa.2016.10.021).
25. S. Bonnabel and R. Sepulchre. Riemannian metric and geometric mean for positive semidefinite matrices of fixed rank. *SIAM Journal on Matrix Analysis and Applications* 31(3) (2009) 1055--1070. DOI [10.1137/080731347](https://doi.org/10.1137/080731347).
