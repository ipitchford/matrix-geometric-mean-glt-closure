#!/usr/bin/env python3
"""Exact finite checks for "Boundary limits of the matrix geometric mean and the
failure of unrestricted GLT closure" (revised version, 3 November 2026).

Usage
    python3 -I -B verify_exact.py OUTPUT.json        # run all checks, write OUTPUT.json
    python3 -I -B verify_exact.py --self-test-mutation # show that a broken formula is caught

Only the Python standard library is used. All arithmetic is exact: rationals
(fractions.Fraction) and Gaussian rationals (pairs of Fractions). Every check
goes through check(), which raises CheckFailure; there are no assert
statements, so running under ``python3 -O`` changes nothing. The status in the
output file is derived from the checks that actually ran.

Scope. These are exact checks of closed-form identities and of finite
assemblies of the constructions in the paper: positivity, exact Riccati
identities (which by uniqueness identify the geometric mean), ranks, exact
traces and decreasing approximation errors along explicit parameter
sequences. Statements quantified over all matrices, all dimensions or all
sequences are proved in the paper, not computed here.

The output path must not already exist (the shipped verification_results.json
is never overwritten).
"""
from fractions import Fraction as F
import json
import platform
import sys
import time
from pathlib import Path


# ---------------------------------------------------------------- checks ---

class CheckFailure(Exception):
    pass


GROUPS = {}
CURRENT = ["setup"]
MUTATION = {"active": False}


def group(name):
    CURRENT[0] = name
    GROUPS.setdefault(name, 0)


def check(condition, label):
    """Record one exact check; raise CheckFailure if it does not hold."""
    if condition is not True:
        if condition is False or not condition:
            raise CheckFailure(f"[{CURRENT[0]}] {label}")
    GROUPS[CURRENT[0]] = GROUPS.get(CURRENT[0], 0) + 1


# ------------------------------------------------------ Gaussian rationals ---

class Q:
    """Exact Gaussian rational re + i*im."""
    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = F(re)
        self.im = F(im)

    @staticmethod
    def of(x):
        return x if isinstance(x, Q) else Q(x)

    def __add__(self, o):
        o = Q.of(o)
        return Q(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = Q.of(o)
        return Q(self.re - o.re, self.im - o.im)

    def __rsub__(self, o):
        return Q.of(o) - self

    def __neg__(self):
        return Q(-self.re, -self.im)

    def __mul__(self, o):
        o = Q.of(o)
        return Q(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = Q.of(o)
        d = o.re * o.re + o.im * o.im
        if d == 0:
            raise ZeroDivisionError("division by zero Gaussian rational")
        return Q((self.re * o.re + self.im * o.im) / d, (self.im * o.re - self.re * o.im) / d)

    def __eq__(self, o):
        o = Q.of(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))

    def conj(self):
        return Q(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def __bool__(self):
        return self.re != 0 or self.im != 0

    def __str__(self):
        if self.im == 0:
            return str(self.re)
        return f"{self.re}{'+' if self.im >= 0 else '-'}{abs(self.im)}i"


I1 = Q(0, 1)


# ---------------------------------------------------------------- matrices ---

def mat(rows):
    return [[Q.of(x) for x in r] for r in rows]


def eye(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def zeros(n, m=None):
    m = n if m is None else m
    return [[Q() for _ in range(m)] for _ in range(n)]


def mul(a, b):
    if not a or not b or not b[0]:
        return zeros(len(a), len(b[0]) if b else 0)
    bt = list(zip(*b))
    return [[sum((x * y for x, y in zip(row, col)), Q()) for col in bt] for row in a]


def mul3(a, b, c):
    return mul(mul(a, b), c)


def add(a, b):
    return [[x + y for x, y in zip(r, s)] for r, s in zip(a, b)]


def sub(a, b):
    return [[x - y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scal(a, s):
    return [[x * s for x in r] for r in a]


def ct(a):
    if not a:
        return []
    return [[a[i][j].conj() for i in range(len(a))] for j in range(len(a[0]))]


def block(a, b, c, d):
    return [ra + rb for ra, rb in zip(a, b)] + [rc + rd for rc, rd in zip(c, d)]


def dsum(*ms):
    n = sum(len(m) for m in ms)
    out = zeros(n)
    k = 0
    for m in ms:
        for i in range(len(m)):
            for j in range(len(m)):
                out[k + i][k + j] = m[i][j]
        k += len(m)
    return out


def hermitian(a):
    return all(a[i][j] == a[j][i].conj() for i in range(len(a)) for j in range(len(a)))


def inv(a):
    n = len(a)
    w = [list(r) + e for r, e in zip(a, eye(n))]
    for j in range(n):
        p = next((i for i in range(j, n) if w[i][j]), None)
        if p is None:
            raise ValueError("singular matrix")
        w[j], w[p] = w[p], w[j]
        s = w[j][j]
        w[j] = [x / s for x in w[j]]
        for i in range(n):
            if i != j and w[i][j]:
                s = w[i][j]
                w[i] = [x - s * y for x, y in zip(w[i], w[j])]
    return [r[n:] for r in w]


def rank(a):
    if not a or not a[0]:
        return 0
    w = [list(r) for r in a]
    rk = 0
    for c in range(len(w[0])):
        p = next((i for i in range(rk, len(w)) if w[i][c]), None)
        if p is None:
            continue
        w[rk], w[p] = w[p], w[rk]
        s = w[rk][c]
        w[rk] = [x / s for x in w[rk]]
        for i in range(len(w)):
            if i != rk and w[i][c]:
                s = w[i][c]
                w[i] = [x - s * y for x, y in zip(w[i], w[rk])]
        rk += 1
        if rk == len(w):
            break
    return rk


def nullspace(a):
    """Exact basis of ker a (columns returned as lists)."""
    n = len(a[0])
    w = [list(r) for r in a]
    piv = []
    rk = 0
    for c in range(n):
        p = next((i for i in range(rk, len(w)) if w[i][c]), None)
        if p is None:
            continue
        w[rk], w[p] = w[p], w[rk]
        s = w[rk][c]
        w[rk] = [x / s for x in w[rk]]
        for i in range(len(w)):
            if i != rk and w[i][c]:
                s = w[i][c]
                w[i] = [x - s * y for x, y in zip(w[i], w[rk])]
        piv.append(c)
        rk += 1
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [Q() for _ in range(n)]
        v[f] = Q(1)
        for r, c in enumerate(piv):
            v[c] = -w[r][f]
        basis.append(v)
    return basis


def charpoly(a):
    """Faddeev-LeVerrier: coefficients c[0..n] of det(x I - a), c[n] = 1."""
    n = len(a)
    c = [Q() for _ in range(n + 1)]
    c[n] = Q(1)
    m = zeros(n)
    for k in range(1, n + 1):
        m = add(mul(a, m), scal(eye(n), c[n - k + 1]))
        am = mul(a, m)
        c[n - k] = -sum((am[i][i] for i in range(n)), Q()) / k
    return c


def psd(a):
    """Exact PSD test for a Hermitian matrix: eigenvalues are real, and they are
    all >= 0 exactly when the characteristic coefficients alternate in sign."""
    if not hermitian(a):
        return False
    n = len(a)
    c = charpoly(a)
    if any(x.im != 0 for x in c):
        return False
    return all(((-1) ** (n - i)) * c[i].re >= 0 for i in range(n + 1))


def pd(a):
    """Exact positive-definiteness test via Hermitian Gaussian elimination."""
    if not hermitian(a):
        return False
    w = [list(r) for r in a]
    n = len(w)
    for k in range(n):
        d = w[k][k]
        if d.im != 0 or d.re <= 0:
            return False
        for i in range(k + 1, n):
            s = w[i][k] / d
            for j in range(k, n):
                w[i][j] = w[i][j] - s * w[k][j]
    return True


def frob2(a):
    return sum((x.abs2() for r in a for x in r), F(0))


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Q())


def is_riccati_mean(a, b, x):
    """X = A # B for A, B > 0 iff X > 0 and X A^{-1} X = B (uniqueness, (2.1))."""
    return pd(a) and pd(b) and pd(x) and mul3(x, inv(a), x) == b


def matstr(a):
    return [[str(v) for v in r] for r in a]


# ----------------------------------------------- the 2x2 family (5.1)-(5.2) ---

def core(e, t, s):
    """A_e, B_{e,t} and the closed form (5.2); s must equal sqrt(4+t^2)."""
    check(s * s == 4 + t * t and s > 0, "s = sqrt(4+t^2)")
    a = mat([[1, 0], [0, e * e]])
    b = mat([[1, e * t], [e * t, e * e * (1 + t * t)]])
    top = 3 if MUTATION["active"] else 2  # the mutation corrupts formula (5.2)
    x = scal(mat([[top, e * t], [e * t, e * e * (2 + t * t)]]), F(1) / s)
    return a, b, x


TS = [(F(0), F(2)), (F(3, 2), F(5, 2)), (F(8, 3), F(10, 3)), (F(15, 4), F(17, 4)), (F(24, 5), F(26, 5))]


def test_core(records):
    group("core 2x2 formula (5.2)")
    for e in [F(1), F(1, 2), F(1, 3), F(1, 7), F(1, 101)]:
        for t, s in TS:
            a, b, x = core(e, t, s)
            check(is_riccati_mean(a, b, x), f"(5.2) is the mean, e={e}, t={t}")
            check(rank(block(a, x, x, b)) == 2, "block rank equals N=2")
    a, b, x = core(F(1, 3), F(3, 2), F(5, 2))
    records["core_specimen_e_1_3_t_3_2"] = matstr(x)
    # (5.4) entries at t = 3/2 with symbolic e checked at several e
    for e in [F(1, 2), F(1, 5), F(2, 9)]:
        _, _, x = core(e, F(3, 2), F(5, 2))
        check(x == mat([[F(4, 5), F(3, 5) * e], [F(3, 5) * e, F(17, 10) * e * e]]), f"(5.4) at e={e}")


# --------------------------------------- Theorem 1: reduction + construction ---

def theorem1_case(a_dim, b_dim, A0, C, L, T, deltas, noncommuting=True):
    """Normal-form data, mapped by a fixed invertible congruence T.

    In normal-form coordinates (a, b, t, k) the limit pair and target are
      A = I_a + 0_b + A0 + 0_k,  B = 0_a + I_b + B0 + 0_k,  X = 0 + 0 + C + 0,
    with B0 = C A0^{-1} C + L L^*. (The construction of Section 3.3 uses only
    A0 > 0, C >= 0 and L; in the reduction of Section 3.2 one additionally has
    A0 + B0 = I, which needs square roots and is not imposed here.)
    """
    t = len(A0)
    k = len(L[0]) if L and L[0] else (0 if t else len(T) - a_dim - b_dim)
    N = a_dim + b_dim + t + k
    check(len(T) == N, "dimensions consistent")
    B0 = (add(mul3(C, inv(A0), C), mul(L, ct(L))) if k else mul3(C, inv(A0), C)) if t else []
    Alim = dsum(eye(a_dim), zeros(b_dim), A0, zeros(k))
    Blim = dsum(zeros(a_dim), eye(b_dim), B0, zeros(k))
    Xlim = dsum(zeros(a_dim), zeros(b_dim), C, zeros(k))
    Th = ct(T)
    A, B, X = mul3(T, Alim, Th), mul3(T, Blim, Th), mul3(T, Xlim, Th)
    M = block(A, X, X, B)
    # conditions (2.4) in the original coordinates
    check(hermitian(A) and hermitian(B) and hermitian(X), "Hermitian data")
    check(psd(A) and psd(B) and psd(X), "A, B, X >= 0")
    check(psd(M), "block matrix M(A,B,X) >= 0")
    rR = rank(mul(L, ct(L))) if (t and k) else 0
    check(rank(M) == a_dim + b_dim + t + rR, "rank identity (3.3)")
    check(rank(M) <= N, "rank M <= N")
    if t and noncommuting:
        check(mul(A0, C) != mul(C, A0), "mixed blocks A0, C do not commute")
        check(mul(A, X) != mul(X, A), "original A and X do not commute")
    # support observation (3.2): ker A and ker B lie in ker X
    for kerv in nullspace(A) + nullspace(B):
        col = [[v] for v in kerv]
        check(all(not r[0] for r in mul(X, col)), "support property (3.2)")
    errs = []
    for d in deltas:
        e2 = d * d  # e_delta = delta^2, so the kernel scale is delta^4
        blocks_a, blocks_b, blocks_x = [], [], []
        if a_dim:
            blocks_a.append(eye(a_dim)); blocks_b.append(scal(eye(a_dim), e2)); blocks_x.append(scal(eye(a_dim), d))
        if b_dim:
            blocks_a.append(scal(eye(b_dim), e2)); blocks_b.append(eye(b_dim)); blocks_x.append(scal(eye(b_dim), d))
        if t:
            Cd = add(C, scal(eye(t), d))
            Qd = add(eye(k), mul3(ct(L), inv(Cd), L)) if k else []
            cA = dsum(A0, scal(eye(k), e2 * e2))
            cX = block(Cd, scal(L, e2), scal(ct(L), e2), scal(Qd, e2 * e2)) if k else Cd
            cB = mul3(cX, inv(cA), cX)
            blocks_a.append(cA); blocks_b.append(cB); blocks_x.append(cX)
        elif k:
            blocks_a.append(scal(eye(k), e2 * e2)); blocks_b.append(scal(eye(k), e2 * e2)); blocks_x.append(scal(eye(k), e2 * e2))
        Ad, Bd, Xd = (mul3(T, dsum(*bl), Th) for bl in (blocks_a, blocks_b, blocks_x))
        check(is_riccati_mean(Ad, Bd, Xd), f"approximants exact: X_d = A_d # B_d (delta={d})")
        check(rank(block(Ad, Xd, Xd, Bd)) == N, "interior block rank equals N (necessity mechanism)")
        err = max(frob2(sub(Ad, A)), frob2(sub(Bd, B)), frob2(sub(Xd, X)))
        errs.append(err)
    for i in range(1, len(errs)):
        check(errs[i] < errs[i - 1], "approximation error strictly decreasing along delta")
    ratios = [e / (d * d) for e, d in zip(errs, deltas)]
    check(all(r <= 2 * ratios[0] for r in ratios), "error is O(delta) (squared error / delta^2 stays bounded)")
    return {"a": a_dim, "b": b_dim, "t": t, "k": k, "N": N, "rank_M": rank(M),
            "deltas": [str(d) for d in deltas],
            "max_squared_frobenius_error": [float(e) for e in errs]}


def test_theorem1(records):
    group("Theorem 1 sufficiency on complex non-commuting data")
    deltas = [F(1, 2), F(1, 4), F(1, 8), F(1, 16), F(1, 32), F(1, 64), F(1, 128)]
    G1 = mat([[1, I1 * F(1, 2)], [F(1, 3), 1 - I1]])
    A0a = add(mul(G1, ct(G1)), scal(eye(2), F(1, 5)))
    G2 = mat([[F(1, 2), I1], [0, F(1, 3)]])
    Ca = mul(G2, ct(G2))
    T3 = mat([[1, I1, 0, F(1, 2)], [0, 1, F(1, 3), 0], [I1 * F(1, 4), 0, 1, 0], [0, F(1, 2), 0, 1]])
    T5 = mat([[1, 0, I1, 0, F(1, 2)], [F(1, 3), 1, 0, 0, 0], [0, 0, 1, I1, 0], [0, F(1, 2) * I1, 0, 1, 0], [F(1, 5), 0, 0, 0, 1]])
    T6 = mat([[1, 0, 0, I1, 0, 0], [0, 1, F(1, 2), 0, 0, 0], [0, 0, 1, 0, I1 * F(1, 3), 0],
              [0, 0, 0, 1, 0, F(1, 2)], [F(1, 4), 0, 0, 0, 1, 0], [0, I1, 0, 0, 0, 1]])
    cases = [
        # (a, b, A0, C, L, T)
        (0, 0, A0a, Ca, mat([[1, I1], [F(1, 2), 0]]), T3),          # t=2, k=2, rank R = 2
        (1, 1, A0a, Ca, mat([[1 + I1], [F(1, 3)]]), T5),             # t=2, k=1, a=b=1
        (1, 0, A0a, Ca, mat([[F(1, 2), 1, 0], [I1, 0, 1]]), T6),     # t=2, k=3 (rank R = 2 < k)
        (0, 1, A0a, Ca, mat([[1, 0], [I1, 0]]), mat([[1, I1, 0, 0, F(1, 2)], [0, 1, 0, 0, 0], [0, F(1, 3), 1, 0, 0], [0, 0, I1, 1, 0], [F(1, 2), 0, 0, 0, 1]])),  # t=2,k=2, rank R=1
    ]
    out = []
    for a_dim, b_dim, A0, C, L, T in cases:
        out.append(theorem1_case(a_dim, b_dim, A0, C, L, T, deltas))
    # empty blocks: k = 0 (then R = 0) and t = 0 (pure common kernel)
    out.append(theorem1_case(0, 0, A0a, Ca, [[], []], mat([[1, I1], [0, 1]]), deltas))
    out.append(theorem1_case(1, 1, [], [], [], mat([[1, 0, I1], [F(1, 2), 1, 0], [0, 0, 1]]), deltas))
    records["theorem1_cases"] = out


def test_necessity(records):
    group("necessity: interior points and the role of each condition")
    datas = [
        (mat([[2, I1], [-I1, 1]]), mat([[1, F(1, 2)], [F(1, 2), 1]])),
        (mat([[3, 1 + I1, 0], [1 - I1, 2, I1 * F(1, 2)], [0, -I1 * F(1, 2), 1]]),
         mat([[1, 0, F(1, 3)], [0, 2, I1 * F(1, 4)], [F(1, 3), -I1 * F(1, 4), 1]])),
    ]
    for A, X in datas:
        B = mul3(X, inv(A), X)  # then X = A # B exactly, by uniqueness in (2.1)
        N = len(A)
        M = block(A, X, X, B)
        check(is_riccati_mean(A, B, X), "Riccati-generated interior point")
        check(psd(M) and rank(M) == N, "interior points satisfy M >= 0 and rank M = N")
    # X >= 0 is not implied by the block conditions: N = 1, A = B = 1, X = -1
    A, B, X = mat([[1]]), mat([[1]]), mat([[-1]])
    M = block(A, X, X, B)
    check(psd(M) and rank(M) == 1 and not psd(X), "example N=1, A=B=1, X=-1")
    # the rank condition is essential: A = B = I_2, X = I_2/2 has M > 0 of rank 4 > 2
    A = eye(2); X = scal(eye(2), F(1, 2))
    M = block(A, X, X, A)
    check(psd(M) and rank(M) == 4, "rank condition excludes X = I/2 at A = B = I_2")
    records["necessity_examples"] = "interior points have block rank N; X=-1 and X=I/2 excluded"


def test_corollary2(records):
    group("Corollary 2 and Corollary 3: equal inputs")
    deltas = [F(1, 2), F(1, 4), F(1, 8), F(1, 16), F(1, 32), F(1, 64)]
    u = [Q(F(3, 5)), Q(0, F(4, 5))]
    uu = [[x * y.conj() for y in u] for x in u]
    out = []
    for lam, ell in [(F(2, 5), F(4, 5)), (F(1), F(1))]:
        D = scal(uu, lam)
        C = sub(eye(2), D)
        L = [[ell * u[0]], [ell * u[1]]]
        check(add(mul(C, C), mul(L, ct(L))) == eye(2), "B0 = C^2 + L L^* = I (equal inputs)")
        rec = theorem1_case(0, 0, eye(2), C, L, eye(3), deltas, noncommuting=False)
        P = dsum(eye(2), zeros(1))
        X = dsum(C, zeros(1))
        check(psd(X) and psd(sub(P, X)) and rank(sub(P, X)) <= 1, "0 <= X <= P and rank(P - X) <= dim ker P = 1")
        # density matrix rho = P/2 (r = 2, q = 1): admissible trace interval [1/2, 1]
        tr = trace(X).re / 2
        check(F(1, 2) <= tr <= 1, "normalised trace lies in [sum_{i>min(q,r)} lambda_i, 1] = [1/2, 1]")
        rec["trace_limit_for_rho_P_over_2"] = str(tr)
        out.append(rec)
    check(out[1]["trace_limit_for_rho_P_over_2"] == "1/2", "lower endpoint 1/2 attained")
    # a rank-2 defect is not attainable when dim ker P = 1
    P = dsum(eye(2), zeros(1)); X = scal(P, F(4, 5))
    check(rank(block(P, X, X, P)) == 4 and 4 > 3, "rank(P - X) = 2 > q is excluded")
    records["corollary2_cases"] = out


def test_theorem4(records):
    group("Theorem 4 operator formula (7.4), complex unitary conjugation")
    U2 = mat([[F(3, 5), I1 * F(4, 5)], [I1 * F(4, 5), F(3, 5)]])
    U = mul(dsum(U2, eye(1)), dsum(eye(1), mat([[F(5, 13), F(12, 13) * I1], [F(12, 13) * I1, F(5, 13)]])))
    check(mul(U, ct(U)) == eye(3), "U unitary")
    ds = [F(4, 5), F(3, 5), F(5, 13)]
    ts = [F(3, 2), F(8, 3), F(24, 5)]
    ss = [F(3, 5), F(4, 5), F(12, 13)]  # sqrt(1 - d^2)
    fn = lambda vals: mul3(U, [[Q(vals[i]) if i == j else Q() for j in range(3)] for i in range(3)], ct(U))
    D, Tn, Sq = fn(ds), fn(ts), fn(ss)
    check(add(mul(Sq, Sq), mul(D, D)) == eye(3), "(I - D^2)^{1/2} exact")
    check(mul(scal(Tn, F(1, 2)), scal(Tn, F(1, 2))) == sub(inv(mul(D, D)), eye(3)), "T = 2 (D^{-2} - I)^{1/2}")
    for e in [F(1, 10), F(1, 100)]:
        n = 3
        A = dsum(eye(n), scal(eye(n), e * e))
        B = block(eye(n), scal(Tn, e), scal(Tn, e), scal(add(eye(n), mul(Tn, Tn)), e * e))
        X = block(D, scal(Sq, e), scal(Sq, e), scal(sub(scal(inv(D), 2), D), e * e))
        check(is_riccati_mean(A, B, X), f"(7.4) is the exact mean (e={e})")
        # all-size padding: one extra coordinate with A = B = X-entry e^2
        Ap, Bp, Xp = dsum(A, mat([[e * e]])), dsum(B, mat([[e * e]])), dsum(X, mat([[e * e]]))
        check(is_riccati_mean(Ap, Bp, Xp), "odd-size padding keeps the exact mean")
    records["theorem4_D_eigenvalues"] = [str(d) for d in ds]


def test_glt_scalar(records):
    group("Section 6.2 full-size scalar GLT assemblies")
    out = []
    for N in range(2, 15):
        m = N // 2
        e = F(1, N)
        t, s = (F(0), F(2)) if N % 2 == 0 else (F(3, 2), F(5, 2))
        ca, cb, cx = core(e, t, s)
        A, B, X = zeros(N), zeros(N), zeros(N)
        for j in range(m):
            idx = [j, m + j]
            for ii in range(2):
                for jj in range(2):
                    A[idx[ii]][idx[jj]] = ca[ii][jj]; B[idx[ii]][idx[jj]] = cb[ii][jj]; X[idx[ii]][idx[jj]] = cx[ii][jj]
        for j in range(2 * m, N):
            A[j][j] = B[j][j] = X[j][j] = Q(e * e)
        check(is_riccati_mean(A, B, X), f"assembled mean exact, N={N}")
        P = dsum(eye(m), zeros(N - m))
        check(frob2(sub(A, P)) <= m * e ** 4 + 1, "A_N close to D_N(a)")
        trn = trace(X).re / N
        formula = F(m, N) * (2 + (2 + t * t) * e * e) / s + F(N - 2 * m, N) * e * e
        check(trn == formula, "normalised trace formula")
        out.append({"N": N, "normalised_trace": str(trn)})
    records["glt_scalar_traces"] = out


def test_dichotomy(records):
    group("Theorem 9 construction, finite instances")
    # kappa = 4x and xi = x on (0,1/2], both 0 on (1/2,1]; sqrt(kappa xi) = 2x there.
    # eta = 1/16: positive indices x_j in (1/8, 1/2]; null indices x_j > 1/2.
    t, s = F(3, 2), F(5, 2)
    out = []
    for n in [16, 32, 64, 128, 256]:
        e = F(1, n)
        xs = [F(j, n) for j in range(1, n + 1)]
        kap = [4 * x if x <= F(1, 2) else F(0) for x in xs]
        xi = [x if x <= F(1, 2) else F(0) for x in xs]
        J1 = [j for j in range(n) if kap[j] * xi[j] > F(1, 16)]
        J0 = [j for j in range(n) if kap[j] == 0 and xi[j] == 0]
        m = (3 * n) // 16
        check(len(J1) >= m and len(J0) >= m, "enough positive and null indices")
        pairs = list(zip(J1[:m], J0[:m]))
        paired = {p for pr in pairs for p in pr}
        tr = F(0)
        riemann = sum((2 * x for x in xs if x <= F(1, 2)), F(0))
        maxdev_a = maxdev_b = F(0)
        for p, q in pairs:
            al, be = kap[p], xi[p]
            ca, cb, cx = core(e, t, s)
            Ab, Bb = scal(ca, al), scal(cb, be)
            root = 2 * xs[p]  # sqrt(al*be) = sqrt(4x^2) = 2x, exact
            check(root * root == al * be, "sqrt(kappa xi) exact at a positive index")
            Xb = scal(cx, root)  # (alpha A) # (beta B) = sqrt(alpha beta) (A # B)
            check(is_riccati_mean(Ab, Bb, Xb), "paired 2x2 block mean exact")
            Dk = mat([[al, 0], [0, kap[q]]]); Dx = mat([[be, 0], [0, xi[q]]])
            maxdev_a = max(maxdev_a, frob2(sub(Ab, Dk)))
            maxdev_b = max(maxdev_b, frob2(sub(Bb, Dx)))
            tr += trace(Xb).re
        for j in range(n):
            if j in paired:
                continue
            a_, b_ = (kap[j], xi[j]) if kap[j] * xi[j] > 0 else (e * e, e * e)
            check((kap[j] * xi[j] > 0) or (kap[j] == 0 and xi[j] == 0), "unpaired sample is positive or a common zero")
            tr += 2 * xs[j] if kap[j] * xi[j] > 0 else e * e
            maxdev_a = max(maxdev_a, (a_ - kap[j]) ** 2)
            maxdev_b = max(maxdev_b, (b_ - xi[j]) ** 2)
        check(maxdev_a <= 4 * e ** 4 and maxdev_b <= (2 * t * e) ** 2 + 4 * (1 + t * t) ** 2 * e ** 4 + 4 * e ** 4,
              "inputs are norm-close to the diagonal samplings D_n(kappa), D_n(xi)")
        trn, rn = tr / n, riemann / n
        gap = rn - trn
        check(gap > F(1, 100) or n < 32, "mean trace stays strictly below the Riemann sum of sqrt(kappa xi)")
        check(abs(trn - F(299, 1280)) <= F(2, n), "normalised trace within 2/n of the limit 299/1280")
        out.append({"n": n, "pairs": m, "normalised_trace_of_mean": str(trn), "riemann_sum_sqrt_kappa_xi": str(rn),
                    "float_trace": float(trn), "float_riemann": float(rn)})
    records["dichotomy_instances"] = {"limit_trace": "299/1280", "symbol_prediction": "1/4", "cases": out}


def test_block_structured(records):
    group("Remark 6.2: structured block (r=2) counterexample")
    t, s = F(3, 2), F(5, 2)
    out = []
    for n in range(1, 7):
        e = F(1, n + 1)
        ca, cb, cx = core(e, t, s)
        A, B, X = dsum(*[ca] * n), dsum(*[cb] * n), dsum(*[cx] * n)  # I_n (x) 2x2 blocks
        check(is_riccati_mean(A, B, X), "I_n (x) (5.2) is the exact mean")
        trn = trace(X).re / (2 * n)
        check(trn == (2 + (2 + t * t) * e * e) / (2 * s), "normalised trace formula (limit 2/5, symbol prediction 1/2)")
        out.append({"n": n, "normalised_trace": str(trn)})
    records["block_structured"] = out


def run_all():
    records = {}
    test_core(records)
    test_theorem1(records)
    test_necessity(records)
    test_corollary2(records)
    test_theorem4(records)
    test_glt_scalar(records)
    test_dichotomy(records)
    test_block_structured(records)
    return records


def main(argv):
    if len(argv) == 2 and argv[1] == "--self-test-mutation":
        MUTATION["active"] = True
        try:
            run_all()
        except CheckFailure as exc:
            print(f"Mutation detected as intended: {exc}")
            print("A broken formula makes the verifier fail (also under python -O, since no assert is used).")
            return 0
        print("ERROR: the mutated formula was NOT detected.")
        return 2
    if len(argv) != 2 or argv[1].startswith("-"):
        print(__doc__)
        return 2
    out = Path(argv[1])
    if out.exists():
        print(f"Refusing to overwrite existing file {out}; give a new output path.")
        return 2
    start = time.time()
    status, failure, records = "PASS", None, {}
    try:
        records = run_all()
    except CheckFailure as exc:
        status, failure = "FAIL", str(exc)
    result = {
        "status": status,
        "failure": failure,
        "scope": ("Exact rational/Gaussian-rational checks of closed forms and finite assemblies of the "
                  "constructions; quantified statements are proved in the paper, not computed."),
        "python": platform.python_version(),
        "optimisation_flag": sys.flags.optimize,
        "checks_by_group": GROUPS,
        "total_checks": sum(GROUPS.values()),
        "records": records,
        "seconds": round(time.time() - start, 2),
    }
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("status", "failure", "total_checks", "checks_by_group", "seconds")}, indent=2))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
