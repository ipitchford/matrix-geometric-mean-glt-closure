# Novelty-gate report: geometric-mean boundary limits and GLT closure (revised version)

**Original search date:** 2 November 2026. **Revised:** 3 November 2026 for the revised paper.
**Corpus boundary:** live indexed web search, the primary full texts listed in
`source_novelty_ledger.md`, and Crossref/arXiv records in `refs/crossref_records.jsonl`.
**Contribution units:** theorems, constructive proofs and exact verification artefacts.

This report records the novelty-gate outcome. It does not certify historical priority.

## 1. Frozen claims

1. **Theorem 1.** For every $N$, $A,B\succeq0$ and Hermitian $X$: $X$ is a limit of $A_j\#B_j$ with
   $A_j,B_j\succ0$, $A_j\to A$, $B_j\to B$ iff $X\succeq0$,
   $\left(\begin{smallmatrix}A&X\\X&B\end{smallmatrix}\right)\succeq0$ and its rank is at most $N$.
2. **GLT counterexamples.** Bounded HPD scalar GLT input sequences with equal symbols whose means have
   symbol $\tfrac45$ times the predicted one, or no distribution; a fully structured $2\times2$ block version.
3. **Theorem 4.** Arbitrary contraction data realised behind two fixed input symbols.
4. **Theorem 7.** For all HPD GLT inputs, the spectral law of the means is stochastically dominated by
   that of the regularised symbol $\kappa\#\xi$.
5. **Theorem 9 / Corollary 10.** For bounded Riemann-integrable scalar symbols of $x$ only, closure for
   every realisation iff $|\{\kappa+\xi=0\}|=0$ or $|\{\kappa\xi>0\}|=0$.
6. **Appendix A.** Sharp spectral envelope of means near projections of any rank density.

### Exclusions

No claim of a new boundary discontinuity, continuity locus, mean, maximal characterisation, dilation
mechanism or sum normalisation. No Karcher-mean result. The finite-dimensional and growing-dimensional
statements are separate.

## 2. Normalisation table

| Original notation | Canonical notation | Transformation checked |
|---|---|---|
| $G(A,B)$ in the GLT target | $A\#B$ | Same positive Riccati solution |
| Candidate symbol $\widetilde G(\kappa,\xi)$ | Regularised mean $\kappa\#\xi$ | Common positive shift, decreasing limit |
| Pairwise repeated $2\times2$ blocks | Grouped range/null coordinates | Simultaneous permutation |
| Sum-normalised pair | $H$, $I-H$ | Congruence by $(A+B)^{-1/2}$ on its support |
| Trace of the mean of states | Matsumoto fidelity | Same scalar quantity |

## 3. Fingerprints

The $2\times2$ mean at $e=1/2$, $t=3/2$ is
$X=\left(\begin{smallmatrix}4/5&3/10\\3/10&17/40\end{smallmatrix}\right)$, characteristic polynomial
$\lambda^2-\tfrac{49}{40}\lambda+\tfrac14$. The dichotomy instance in `verify_exact.py`
($\kappa=4x$, $\xi=x$ on $(0,1/2]$, zero elsewhere) has limiting normalised trace $299/1280$ against the
predicted $1/4$. No candidate integer sequence or generating function is load-bearing, so no OEIS search
applies.

## 4. Search log and collisions

The query families and inspected sources are in `source_novelty_ledger.md`, Sections 2 and 4.

| Date | Corpus | Outcome |
|---|---|---|
| 2026-11-02 | Indexed literature, arXiv | Target located; no correction or erratum found |
| 2026-11-02 | Matrix-analysis texts, slides | Collision for the elementary discontinuity |
| 2026-11-02 | Jones §4.12 | Close prior work: envelope, dilation attainability, continuity dichotomy |
| 2026-11-02 | Formula searches (graph closure, cluster set, rank defect, Riccati) | Exact rank criterion not located |
| 2026-11-03 | Crossref/arXiv records for every cited work | Bibliographic data verified |
| 2026-11-03 | Published LAA text (locations), Khan thesis, ETNA papers | Failing step verified verbatim in the published proof; no one-sided spectral comparison located |
| 2026-11-03 | Published LAA text, AI-assisted reading | Hypotheses of Theorem 3 (pp. 8--9) and Conjecture 1 (p. 19) admit the counterexamples |

No new literature search for Theorems 7 and 9 beyond these sources was run in the revision; their
novelty status rests on the same bounded record.

## 5. Outcome by unit

| Unit | Outcome | Allowed wording | Forbidden wording |
|---|---|---|---|
| Boundary discontinuity | Collision | Classical mechanism | First example |
| Theorem 1 | Bounded uncertainty | Explicit elimination of the dilation variable; not found elsewhere | First description of the set of limits |
| Corollaries 2--3 | Partial collision (Jones) | Necessity and full set new as far as found | New fidelity discontinuity |
| GLT counterexamples, Theorem 4 | Bounded uncertainty | Refutes the stated theorem and conjecture | Absolute priority |
| Theorem 7 | Bounded uncertainty | Sequence-level form of a classical order bound | New order bound |
| Theorem 9 / Corollary 10 | Bounded uncertainty | Sharp for the stated class | Sharp for all symbols |
| GS17 Conjecture 10.1 | Not inspected | Conditional statement only | "Refutes Conjecture 10.1" |
| Exact verification | Clear within scope | Exact finite checks | Formal verification |

## 6. Decision

**Bounded uncertainty.** The results may be presented with their proofs and the explicit credits in the
paper. Rerun the gate if an equivalence with a matrix-completion theorem, a dilation classification, a
reverse-test result or a GLT closure criterion is found, or once the 2017 monograph is inspected.
