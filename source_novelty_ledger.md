# Source, object-identity and novelty ledger (revised version)

**Original search and assessment:** 2 November 2026. **Revised:** 3 November 2026, to match the
revised paper `paper.md` (new Theorems 7 and 9, Corollaries 8 and 10, Remark 6.2; corrected
statements about which sources were inspected).

This ledger records a bounded literature check. It does not certify priority. Results proved in
the paper are kept separate from the assessment that their exact formulations were not found.

## 1. Exact mathematical objects

The mean is the Kubo--Ando / Pusz--Woronowicz geometric mean
$A\#B=A^{1/2}(A^{-1/2}BA^{-1/2})^{1/2}A^{1/2}$ for $A,B\succ0$, extended to singular pairs by the
common decreasing shift. The research question concerns limits along **all** positive definite
paths. The graph-closure statement (Theorem 1) is: $X$ is such a limit at $(A,B)$ iff $X\succeq0$,
$\left(\begin{smallmatrix}A&X\\X&B\end{smallmatrix}\right)\succeq0$ and its rank is at most $N$.

The GLT target concerns Hermitian positive definite matrix-sequences with separate scalar or block
GLT symbols. The counterexamples use scalar symbols, norm-small perturbations of diagonal sampling,
bounded norms and positive definiteness at every size; a block ($r=2$) version uses only constant-symbol
block Toeplitz matrices and terms $g(n)T_n(f)$.

## 2. Primary sources and what was actually inspected

| Source | Inspected | Relationship |
|---|---|---|
| Ilyas, Khan, Loi, Serra-Capizzano, arXiv:2505.03256v1 | Full text: Theorem 3 (restatement of Ahmad et al.), Theorem 4 p. 11, proof p. 12, Theorem 6 p. 13, Definition 3 and Conjecture 1 p. 21 | Direct target: Theorem 4, Theorem 6 (block, commuting) and Conjecture 1 refuted as stated |
| Same article, published version, Linear Algebra Appl. (2025), doi:10.1016/j.laa.2025.08.004 | Locations verified via the institutional full text: Theorem 3 pp. 8--9; identification step p. 10 (quoted verbatim); Definition 3 / (4.5) p. 18; Conjecture 1 p. 19; "maximal" remark p. 27; reference to "Conjecture 10.1" p. 8. Full statements were **not** transcribed. A separate AI-assisted reading of the published full text (3 November 2026) confirmed that the hypotheses of Theorem 3 (pp. 8--9) and Conjecture 1 (p. 19) admit the counterexamples and that the proof contains the attacked identification (p. 10) | Refuted as stated (on the basis of that AI-assisted reading); the arXiv wording is quoted in the paper |
| Ahmad, Khan, Serra-Capizzano, Mathematics 13(3) 393 (2025) | Theorem 3, p. 10 (restating Garoni--Serra-Capizzano Theorem 10.2, with a non-vanishing hypothesis) | Earlier positive theorem; not contradicted |
| Khan, doctoral thesis, arXiv:2511.06312 | Theorem 5.2 p. 66 (conclusion quoted); Conjecture 5.2.1 p. 77; Definition 3 / (5.13) p. 76 | Repeats the unrestricted statement and the conjecture; affected in the same way |
| Garoni, Serra-Capizzano, GLT Vol. I (Springer 2017) | **Not accessible** (landing page only) | Status of its Conjecture 10.1 stated conditionally in the paper |
| Barbarino, Garoni, Serra-Capizzano, ETNA 53 (2020) 28--112 and 113--216 | Theorem numbers for inversion, functional calculus, sums/products, diagonal sampling, zero-distributed sequences | Cited with exact numbers in Section 6.1 |
| Jones, *Continuity, Testing Regions and Fragility of Quantum Channel Divergences*, self-hosted preprint, October 2026 | Section 4.12, printed pp. 105--110: Lemma 4.12.1, Remark 4.12.2, Lemma 4.12.3, Theorem 4.12.4, Corollaries 4.12.5--4.12.6 | Closest prior work; see Section 3 |
| Ando (1979), Pusz--Woronowicz (1975), Kubo--Ando (1980), Bhatia (2007) | Standard results used: maximal characterisation, monotonicity, representing functions | Credited; classical |
| Poulson, lecture slides (2018) | Slide 9 | Secondary illustration of the classical discontinuity |

All references in the paper come from Crossref or arXiv records fetched on 3 November 2026
(`refs/crossref_records.jsonl`), except Jones (self-hosted, not indexed) and the Poulson slides.

### Earlier public criticism

Pith carries an explicitly AI-generated review of arXiv:2505.03256 dated 15 August 2026
(<https://pith.science/paper/2505.03256>). It flags the a.c.s. approximation step but gives no
counterexample. It is recorded as prior commentary; no priority is claimed for noticing a gap.

## 3. Closest-collision analysis

**Classical discontinuity.** The $2\times2$ mechanism (collapsing congruence of fixed inputs) is
classical; no novelty is claimed for formula (5.2).

**Ando / Pusz--Woronowicz.** $A\#B$ is the largest Hermitian $X$ with block matrix
$\succeq0$. Theorem 1 identifies the set of limits as the positive semidefinite feasible points whose
block matrix has rank at most $N$; every limit lies below $A\#B$.

**Jones, Section 4.12.** Lemma 4.12.1(b): every limit point lies below $A\sigma B$. Lemma 4.12.3:
attainability by dilation into the common kernel, for every connection; with compactness this
gives a complete description of the set of limits with an auxiliary contraction (Appendix B of the
paper). Theorem 4.12.4(b) and Corollary 4.12.5: lower endpoint of the fidelity interval and the
case $q\ge r$. Remark 4.12.2: one-sided perturbations cannot produce jumps. The surviving
distinction of Theorem 1 is the explicit elimination of the auxiliary contraction; of Corollaries
2--3, the necessity half and the full matrix set. Theorem 7 is the sequence-level (GLT) analogue of
the order bound in Lemma 4.12.1(b).

**"Maximal" in Ilyas et al.** The published conclusion (p. 27) calls its Theorem 5 maximal; the
source record located no one-sided spectral comparison between $G(A_n,B_n)$ and
$(\kappa\xi)^{1/2}$ there. Theorem 7 is therefore not credited to that article.

## 4. Formula-first search log (2 November 2026, unchanged)

Searches used the two available web search engines, with the more comprehensive engine used for verification and exact-priority queries. Query families included:

### Target and status

- "2505.03256" counterexample correction erratum
- "geometric mean" "GLT" "counterexample"
- "geometric means" "degenerate" "counterexample" GLT 2026
- "GLT" "Khan" "error" geometric
- "Conjecture 10.1" "geometric"
- Exact paper title and DOI with correction/erratum terms.

### Boundary object and equivalent formulations

- "geometric mean" "discontinuous" "positive semidefinite"
- "geometric mean" "boundary" "continuity" "rank"
- "geometric mean" "arbitrary" "singular" "limit"
- "geometric mean" "cluster" matrices singular
- "geometric mean" "cluster set" projection
- "geometric mean" "rank" "continuity points"
- "matrix means" "boundary limits"
- "geometric mean" "graph closure"
- "geometric mean" "closure of the graph"
- "geometric mean" "cluster set" matrices
- "geometric mean" "rank" "block matrix" "limit"
- "operator mean" "continuity points"
- "geometric mean" "set of limits"
- "geometric mean" "rank defect"

### After reduction to Riccati and block rank

- "geometric mean" "rank" "Riccati" "closure"
- "matrix geometric mean" "singular" "all limits"
- "geometric mean" "graph" "Schur complement" rank
- "geometric mean" "rank condition" semidefinite limit
- "geometric mean" "set of all" "limits" matrix
- "geometric mean" "closure" "positive semidefinite" block
- "Geometric mean block matrices" rank semidefinite
- "geometric mean" "cluster values"
- "geometric mean" "rank" "closure of"
- "geometric mean" "4/5" "3/10" "17/40"
- "Matsumoto fidelity" "limits" "rank"
- "geometric mean" "rank condition" "boundary"

These later queries returned standard Riccati characterizations, computational surveys, fixed-rank alternative means, and unrelated Schur-complement results. They did not locate the exact graph-closure criterion.

The exact-entry query yielded unrelated results rather than a matrix identity. The fidelity query located surrounding quantum-fidelity literature; it did not settle priority for the exact trace interval. The formal gate outcome is recorded in `novelty_report.md`.

This log is a record of searches run, not a claim that all relevant literature is indexed, accessible, or exhausted.

## 5. Claim-by-claim assessment (revised)

| Claim | Status in paper | Novelty after bounded search |
|---|---|---|
| Boundary discontinuity, formula (5.2) | Exact formula | Known; not claimed |
| Theorem 1 (rank criterion) | Complete proof | Explicit elimination not found; dilation form follows from Jones |
| Corollary 2 (equal inputs) | Complete proof | Necessity and full set not found; attainability partly in Jones |
| Corollary 3 (fidelity interval) | Complete proof | Lower endpoint and $q\ge r$ case in Jones; necessity not found |
| GLT counterexamples (Section 6) | Complete proof | No prior instance found |
| Structured block counterexample (Remark 6.2) | Complete proof | No prior instance found |
| Theorem 4 (universal contraction realisation) | Complete proof | No prior instance found |
| Theorem 5 / Corollary 6 | Complete proof | Standard sum normalisation; GLT transfer only |
| Theorem 7 (upper envelope) | Complete proof | Sequence-level form not found; matrix-level order bound classical / Jones |
| Corollary 8 (disjoint supports) | Complete proof | Not found |
| Theorem 9, Corollary 10 (dichotomy, $x$-only Riemann-integrable scalar symbols) | Complete proof | Not found |
| Appendix A (spectral envelope at projections) | Complete proof | Not found |
| Appendix B (dilation cluster set) | Proof included | Credited to Jones (attainability) plus compactness |

## 6. Remaining limits

Searches were run on 2 November 2026 and were bounded. The 2017 monograph was not inspected. The
published article was inspected only at the locations listed. No correspondence with the authors of
the target article has taken place. No external referee has assessed the work.
