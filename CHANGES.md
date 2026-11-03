# Changes in the revised version (3 November 2026)

One revision round implementing FIX_LIST.md. Section, theorem and equation numbers refer to the
revised `paper.md`. The source draft and its two supplements were merged into one manuscript
(main text, Appendix A, Appendix B).

## A. Correctness and assurance

| Item | Disposition |
|---|---|
| A1 verifier | **Done.** `verify_exact.py` rewritten: every check goes through `check()`, which raises (no `assert`); status derived from the checks run; output path from argv and refuses to overwrite an existing file. New tests: Theorem 1 construction on complex (Gaussian-rational) non-commuting data under fixed complex congruences, with support property (3.2), rank identity (3.3), exact Riccati identity for each approximant, strictly decreasing errors and an O(delta) check; necessity (interior points have block rank N; the X=-1 and X=I/2 examples); Corollaries 2--3 on complex data incl. the lower endpoint; Theorem 4 formula (7.4) under a complex unitary with odd padding; Section 6 assemblies N=2..14; finite instances of the Theorem 9 construction; the block example of Remark 6.2. 1,030 checks, PASS, also under `python -O`. `--self-test-mutation` corrupts (5.2) and shows the failure is caught (also under -O). Scope stated honestly in the docstring, JSON and Section 11. |
| A2 GLT citations | **Done.** Section 6.1 lists the facts with ETNA 53 theorem numbers and pages (unilevel Thms 4.17, 4.18, 4.19, 4.24; multilevel Thms 4.16, 4.17, 4.18, 4.23; GLT 3 items), two short verbatim quotations, and GS17/GS18. Proof of Theorem 5 now states: no boundedness needed for functional calculus; $S_n^{-1}=S_n^\dagger$; $S_n^{-1/2}=(S_n^{-1})^{1/2}$; $H_n(I-H_n)$ Hermitian because the factors commute. Corollary 6 extends $\phi$ continuously by constants outside [0,1]. |
| A3 small rigour | **Done.** Example N=1, A=B=1, X=-1 (Remark (i) after Theorem 1, also checked); Appendix A now states C_N ⪰ 0, Y_N - X_N = o(1), and the portmanteau step with closed sets; Theorem 4 restated for all sizes N with explicit odd padding; Corollary 6 continuity of $\phi$ proved in one line ($f$ concave, $f(u)/u$ nonincreasing); Remark 3.1 on the O(delta) rate with constants; one fidelity statement (Corollary 3, $\sum_{i=\min(q,r)+1}^r$), Appendix A cross-references it; notation $e_\delta^2$ replaced by explicit $\delta^4$. |
| A4 attacked statements | **Done within the source record.** Section 6.3 paraphrases arXiv Theorem 4 (p. 11) and Conjecture 1 (p. 21) and quotes verbatim the failing identification ("and this limit coincides with ... in a.c.s. topology", published p. 10; arXiv p. 12). The source record (astra/sources_output.md) transcribed only short passages and **not** the published Theorem 3 hypotheses; the paper says so and states that the hypothesis check uses the arXiv wording. Warning added that arXiv "Theorem 3" is the earlier restricted (true) result. The failing step is pinned: $(A_NB_N^2A_N)^{1/4}\to P_N$ while $A_N\#B_N\to\frac45P_N$. |

## B. Positioning and literature

| Item | Disposition |
|---|---|
| B1 Jones overlap | **Done.** Sections 1.5 and 4, table in 1.4, Appendix B: Lemma 4.12.3 + compactness gives the auxiliary-contraction description; Theorem 1's contribution is the explicit elimination; Thm 4.12.4(b)/Cor 4.12.5 give the lower endpoint and q ≥ r case; new = necessity and full set (2.5). Jones's Lemma 4.12.1(b) credited for the envelope. **Partly done:** the direct ZZ* argument is given for (B.1) ⇒ (2.4); for the converse no two-line CS-decomposition elimination was found, so the paper obtains it by combining Theorem 1 sufficiency with Proposition B.1 and says so. A unitary-factor form of (2.4) is added (Remark (iii)). |
| B2 Ando / Pusz--Woronowicz | **Done.** Lemma 2.1(a) with proof and citations to Ando 1979, Pusz--Woronowicz 1975, Kubo--Ando 1980, Bhatia 2007; Theorem 1 read as the rank-constrained part of Ando's feasible set; every limit ⪯ A#B; Lemma 2.1(b) ran(A#B)=ranA ∩ ranB with proof. Poulson slides demoted to a secondary source. |
| B3 GS17 Conj 10.1, Khan thesis | **Done conditionally.** The book was not accessible to the source record; the paper says so, quotes the published article's "thus proving [21], Conjecture 10.1." (p. 8), cites Khan Thm 5.2 (p. 66, conclusion quoted) and Conj. 5.2.1 (p. 77, quoted), and states that Conjecture 10.1 is refuted only if it asserts the unrestricted statement. The restricted Ahmad et al. Theorem 3 (quoted hypothesis) is not contradicted. |
| B4 provenance | **Done.** "Checked by two agents" removed from the body; provenance in Declarations; Pith review kept as dated prior commentary in Section 11. |
| B5 non-locality, block example | **Done.** Remark 6.1 (zero-distributed but non-local perturbation), Remark 6.2 (fully structured r=2 counterexample $I_n\otimes A_e$, $I_n\otimes B_{e,t}$, refuting block Conjecture 1 and arXiv Theorem 6 natively; exact-checked), open problem 1 in Section 10. |
| B6 bibliography | **Done.** All 25 references rebuilt from Crossref/arXiv records fetched today (`refs/crossref_records.jsonl`), except Jones (self-hosted preprint, dated "October 2026" per title page, labelled not peer reviewed) and the Poulson slides (secondary, grey literature). Kian's withdrawn preprint not cited. Bonnabel--Sepulchre added (record verified). Numbered in order of first citation. |

## C. Readability

| Item | Disposition |
|---|---|
| C1 introduction | **Done.** Section 1: plain-English geometric mean (midpoint, covariance averaging, structured matrices, quantum fidelity), GLT symbols intuitively, the claim and why it fails, results table, relation to earlier work, reader's guide. |
| C2 safety box | **Done.** "When is the symbol formula safe?" after Corollary 10. |
| C3 quantum remark | **Done.** Remark 4.1 with the exact fidelity formula from (5.2); Uhlmann fidelity → 1. |
| C4 figure | **Done.** Figure 1 (c(t) and the even/odd trace limits), produced by `make_figures.py`; Appendix A figure regenerated. |
| C5 conclusion | **Done.** Section 10 with Riemannian-midpoint sentence (Bonnabel--Sepulchre, no equivalence claimed), shorted-operator link in Remark (iv) after Theorem 1, open problems. |

## E. Extensions

| Item | Disposition |
|---|---|
| E1(a) | **Done as stated (Theorem 7), all HPD block/multilevel GLT inputs.** Monotonicity $G_n\preceq G_n^\varepsilon$, Theorem 5 for the shifted means, Weyl monotonicity, portmanteau for the closed set $[\delta,\infty)$, then $\varepsilon\to0$ by pointwise convergence of the indicators $1\{\lambda_i(\gamma_\varepsilon)\ge\delta\}$ (valid because $\gamma_\varepsilon\downarrow\gamma$ and the set is closed; no condition where κ or ξ vanish) and dominated convergence; part (b) gives tightness and stochastic domination of every subsequential limit. Crediting: the source record found that Ilyas et al.'s "maximal" refers to their Theorem 5 being maximal (p. 27 quote) and located no one-sided spectral comparison, so Theorem 7 is not credited to them; the matrix-level order bound is credited to Ando/Jones. |
| E1(b) | **Done (Corollary 8)**, block version via ran κ ∩ ran ξ = {0}. |
| E1(c) | **Done (Theorem 9)** for d ≥ 1, scalar, bounded Riemann-integrable symbols of x only; proof written for d=1 with the d-level changes stated. Index counting uses weak convergence of the empirical joint law of $(\kappa(x_j),\xi(x_j))$ (Riemann integrability of $F(\kappa,\xi)$) and the portmanteau inequality for open sets (no continuity points needed), with a diagonal choice $\eta_n\to0$; uniform norm bounds explicit; also a no-distribution variant. |
| E1(d) | **Done (Corollary 10)** for exactly that class; the "if" direction holds for all symbols; the converse for (x,θ) and block symbols is stated as open. |
| E2 | Not attempted (optional); harmonic, weighted, Karcher means and a quantitative Theorem 1 listed as open problems. |

## Other

- No quality ratings of any kind appear in `revised/`; ledger and novelty report updated to the revised claims
  and to what was actually inspected (the original draft's statement that the published full text was
  inspected in full is replaced by the precise, more limited record).
- Pages of the PDF were rendered and inspected; fixed: broken DOI links, doubled figure labels, an
  orphaned heading, crowded remarks.

## Final fixes (after proof audit, adversarial audit and re-review)

| Source | Item | Disposition |
|---|---|---|
| proof_audit M1 / re-review NEW-1 / audit attribution note | Published-version claims | Abstract, §1.3, results table, §6.3 and §11 now say: arXiv Theorem 4 and Conjecture 1 are quoted and refuted; for the published Theorem 3 and Conjecture 1, a separate AI-assisted reading of the published full text confirmed that their hypotheses admit the examples (pp. 8--9, p. 19) and that the proof contains the attacked step (p. 10). GS17 Conjecture 10.1 remains conditional. |
| proof_audit M2, m3; audit 1 | Scope of the dichotomy | Paragraph after Corollary 10, the safety box and §10 rewritten: sufficiency for all scalar/block symbols; necessity only for bounded Riemann-integrable scalar symbols of $x$; block conditions stated as $\ker\kappa\cap\ker\xi=\{0\}$ and $\operatorname{ran}\kappa\cap\operatorname{ran}\xi=\{0\}$ (counterexample $\kappa=\xi=\operatorname{diag}(1,0)$); "anywhere in the envelope" restricted to inputs approaching projections. |
| proof_audit m1 | Remark 3.1 rate | Now $O(\delta^2)$ for $A$ ($O(\delta^4)$ if $b=0$), $O(\delta)$ for $B$, $X$; congruence factor $\|T^{-1}\|^2$ noted. |
| proof_audit m2; audit 5 | Functional calculus | Corollary 6 uses $z\mapsto\phi(\operatorname{Re}z)$ on $\mathbb C$; §1.2 says "continuous functions of Hermitian GLT sequences". |
| proof_audit m4 | Limit sequence attribution | "In the arXiv proof the limit sequence is ...". |
| proof_audit m5 | Verifier instances | §11 now describes them accurately as a variant (η₀ = 1/16, ⌊3n/16⌋ pairs from the smallest admissible indices, blockwise trace). Verifier code unchanged. |
| proof_audit m6 | Notation | Appendix B uses $k$ for the common kernel. |
| proof_audit m7 | Slack | Bound tightened to $e_n^2(K+1)$. |
| proof_audit m8 | Theorem 9 for $d>1$ | The proof now states exactly the two grid facts used (Riemann sums converge as the mesh $\max_i1/n_i\to0$; multilevel (G2), ETNA 53 Thm 4.23) and that every step holds verbatim with $n$ replaced by $N(n)$; Theorem 9 / Corollary 10 kept for $d\ge1$. |
| audit 2 | Theorem 7(b) wording | "the right side increases to". |
| audit 3 | Quantum guard | Replaced by: all states in the family are full rank; robustness needs quantitative control of the smallest eigenvalues. |
| audit 4 | Abstract | "need not be continuous at singular pairs". |
| re-review m1 | Verbatim arXiv quotations | Short quotations of arXiv Theorem 4 (p. 11) and Conjecture 1 (p. 21) added in §6.3. |
| re-review m3 | "Theorem 5 is maximal" | Now "their Theorem 5, pp. 10--11". |
| re-review m4 | Figure 1 | Label overlap fixed (labels moved, leader lines); fonts enlarged in both figures. |
| re-review m5 | Undefined terms | Kubo--Ando mean glossed in the abstract and §1.1; zero-distributed and a.c.s. defined in §1.2. |
| re-review m2, m6 | Cosmetic | Left as is (one-direction ZZ* argument already disclosed; reference dates explained in entries). |

PDF rebuilt (21 pages) and the changed pages re-inspected; an orphaned "Open problems" heading was fixed.
`verify_exact.py` rerun to a new path (PASS, 1,030 checks) and that output replaced `verification_results.json`.
