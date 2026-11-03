# AI index: boundary limits of the matrix geometric mean and GLT closure (v0.1.0-candidate)

Machine-oriented map of claims, evidence and limits. Human readers should start with
[README.md](README.md) and the paper [geometric_mean_boundary_glt.pdf](geometric_mean_boundary_glt.pdf)
(source [paper.md](paper.md)). Version DOI 10.5281/zenodo.23912963; concept DOI 10.5281/zenodo.23912962.

## Notation

A#B = A^{1/2}(A^{-1/2} B A^{-1/2})^{1/2} A^{1/2} for Hermitian positive definite (HPD) A, B; for singular
pairs the regularised mean is lim_{eps->0} (A+eps I)#(B+eps I). M(A,B,X) = [[A, X], [X, B]].
GLT = generalized locally Toeplitz; {A_n} ~GLT kappa means the sequence has symbol kappa(x, theta).
"Kubo-Ando mean" = operator mean in the sense of Kubo and Ando (1980). Matsumoto fidelity = tr(rho#sigma).

## Claims and where they are proved

| ID | Claim | Location in [paper.md](paper.md) | Evidence type |
|---|---|---|---|
| C1 | X is a limit of A_j#B_j with HPD A_j -> A, B_j -> B iff X >= 0, M(A,B,X) >= 0 and rank M(A,B,X) <= N | Theorem 1, Sections 2-3 | proof; dilation form already follows from Jones (2026) Lemma 4.12.3 (Appendix B) |
| C2 | Equal inputs A: limits are exactly {0 <= X <= A, rank(A-X) <= dim ker A} | Corollary 2, Section 4 | proof; lower endpoint and q >= r case in Jones |
| C3 | Exact interval of limiting Matsumoto fidelities at a state of rank r in dimension d | Corollary 3, Remark 4.1 | proof |
| C4 | 2x2 formula: inputs within eps of diag(1,0) whose mean tends to c(t) diag(1,0), c(t) = 2/sqrt(4+t^2), any c in (0,1] | Section 5, formulas (5.1)-(5.3) | proof; exact checks |
| C5 | Bounded HPD scalar GLT input sequences with equal step-function symbols whose means have symbol 4/5 times the predicted one on half the interval, or no eigenvalue distribution | Section 6.2, (6.1)-(6.6), Figure 1 | proof; exact checks of the assemblies N = 2..14 |
| C6 | C5 refutes Theorem 4 and Conjecture 1 of arXiv:2505.03256 (quoted) and, per an AI-assisted reading of the published text, Theorem 3 and Conjecture 1 of Ilyas et al., Linear Algebra Appl. (2025); the failing proof step is located | Section 6.3 | source comparison; published-version check is AI-assisted, not a full transcription |
| C7 | Fully structured 2x2-block counterexample built from constant-symbol block Toeplitz terms | Remark 6.2 | proof; exact checks |
| C8 | Any sequence of Hermitian contractions can be realised behind two fixed input symbols | Theorem 4, Section 7, formula (7.4) | proof; exact checks |
| C9 | Closure {A_n#B_n} ~GLT kappa#xi when kappa+xi > 0 a.e., for every Kubo-Ando mean | Theorem 5, Corollary 6, Section 8 | proof (standard identity plus GLT transfer) |
| C10 | The spectral law of A_n#B_n is stochastically dominated by that of the regularised symbol kappa#xi; closure when kappa#xi = 0 a.e. | Theorem 7, Corollary 8, Section 9 | proof |
| C11 | For bounded Riemann-integrable scalar symbols of x only: closure for every HPD realisation iff the symbols have no common zero set of positive measure or essentially disjoint supports | Theorem 9, Corollary 10, Section 9 | proof; finite instances checked exactly (normalised trace 299/1280 < 1/4) |
| C12 | Sharp spectral envelope of means of inputs approaching projections of any rank density | Theorem A.1, Appendix A, [figA1_spectral_envelope.png](figA1_spectral_envelope.png) | proof |
| C13 | Dilation description of the set of limits and its relation to C1 | Proposition B.1, Appendix B | proof; credited to Jones (2026) |

Practical summary: the "When is the symbol formula safe?" box after Corollary 10.
Open problems (necessity for (x, theta) and block symbols, structured classes, other means): Section 10.

## Verification artefacts

- [verify_exact.py](verify_exact.py) -> [verification_results.json](verification_results.json): 1,030 exact
  rational and Gaussian-rational checks (Python standard library only) of formula (5.2), the Section 3.3
  construction on complex non-commuting data, the role of each condition in Theorem 1, Corollaries 2-3,
  formula (7.4), the assemblies of Section 6, finite instances of a variant of the Theorem 9 construction and
  Remark 6.2. Every check raises on failure (no assert), so `python -O` does not disable it.
  `--self-test-mutation` corrupts formula (5.2) and exits 0 only if the corruption is detected.
  Scope: identities and finite assemblies only; limits and quantifiers rest on the written proofs.
- [make_figures.py](make_figures.py) draws [fig1_mean_collapse.png](fig1_mean_collapse.png) and
  [figA1_spectral_envelope.png](figA1_spectral_envelope.png) (PDF versions also shipped) from closed forms.
- Replay commands: [README.md](README.md) "Reproduce"; CI: [.github/workflows/replay.yml](.github/workflows/replay.yml);
  pinned figure packages: [requirements.txt](requirements.txt).

## Sources, novelty and revision record

- [refs.bib](refs.bib) and [refs/crossref_records.jsonl](refs/crossref_records.jsonl): bibliography and the
  Crossref/arXiv records it was copied from (Jones 2026 and the Poulson slides have no registry record).
- [source_novelty_ledger.md](source_novelty_ledger.md), [novelty_report.md](novelty_report.md): dated, bounded
  literature check and closest-collision analysis (Ando, Pusz-Woronowicz, Jones section 4.12).
- [RESEARCH_GATES.json](RESEARCH_GATES.json): contribution map, sources read, limitation triage.
- [CHANGES.md](CHANGES.md): how each item of the internal revision round was handled.
- Integrity: [MANIFEST.sha256](MANIFEST.sha256). Licences: [LICENSE.md](LICENSE.md) (text and figures CC0-1.0, code MIT).

## Limits

Unrefereed candidate: internal AI-assisted review only; no human peer review, independent reproduction or
proof-assistant formalisation. The verifier checks finite exact identities, not the theorems' quantifiers.
Necessity in the dichotomy is proved only for bounded Riemann-integrable scalar symbols depending on x.
The published version of the target article was checked by an AI-assisted reading; the 2017 monograph
(Conjecture 10.1) was not accessible, so its status is conditional. Priority holds only within a bounded search.
