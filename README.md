# Boundary limits of the matrix geometric mean and the failure of unrestricted GLT closure

Research package, revised version, 3 November 2026. Author: Anonymous.
Text CC0-1.0; code MIT (see `LICENSE.md`).

## The result in one paragraph

The geometric mean $A\#B$ of two positive definite matrices is the matrix version of $\sqrt{ab}$,
used to average covariance matrices, structured matrices and quantum states. When the matrices
approach singular ones, the mean can jump, and this paper describes every value it can jump to: a
matrix $X$ is a possible limit exactly when $X\succeq0$, the block matrix
$\left(\begin{smallmatrix}A&X\\X&B\end{smallmatrix}\right)$ is positive semidefinite, and that block
matrix has rank at most the dimension. The same mechanism breaks a published claim about large
structured matrices (GLT sequences): two input sequences can have identical eigenvalue "symbols"
while their geometric means have the wrong symbol, or none at all. This refutes the unrestricted
theorem and Conjecture 1 of Ilyas, Khan, Loi and Serra-Capizzano (Linear Algebra Appl., 2025). The
paper also shows when the symbol formula is safe: when the two symbols never vanish together on a
set of positive measure, or never overlap. For scalar symbols depending on space only, nothing else
is safe.

## What else is in the paper

- The exact interval of possible limits of the Matsumoto (geometric) fidelity at a fixed state, and
  an example of two nearly pure qubit states, arbitrarily close, with any Matsumoto fidelity in (0,1].
- A theorem that hides any sequence of contractions behind two fixed input symbols.
- Closure of GLT sequences under every Kubo--Ando mean when the sum of the symbols is invertible.
- A one-sided theorem: the eigenvalues of the means never exceed what the regularised symbol predicts.
- A sharp spectral envelope for means near projections (Appendix A), and the relation to Jones's
  dilation description (Appendix B).
- A practical box, "When is the symbol formula safe?", and a list of open problems.

## Status and limits

This is an unrefereed candidate, developed with AI assistance and checked by separate AI reviewers;
it has not been peer reviewed by humans or formally verified. All statements have written proofs;
`verify_exact.py` checks closed forms and finite assemblies exactly but does not check limits or
quantifiers. The arXiv version of the target article is quoted directly; for the published version, short
passages were verified verbatim and a separate AI-assisted reading confirmed that its Theorem 3 and
Conjecture 1 admit the counterexamples (pages cited in Section 6.3). The 2017
monograph containing the original Conjecture 10.1 was not accessible, so its status is stated
conditionally. The dilation description of the set of limits follows from recent work of Jones; the
contribution of Theorem 1 is the explicit rank form. Literature searches were dated and bounded
(`source_novelty_ledger.md`, `novelty_report.md`).

## Files

| File | Contents |
|---|---|
| `geometric_mean_boundary_glt.pdf` | The paper (typeset). |
| `paper.md` | Source of the paper. |
| `fig1_mean_collapse.pdf/.png`, `figA1_spectral_envelope.pdf/.png` | Figures 1 and A.1. |
| `make_figures.py` | Draws the figures from the closed-form formulas. |
| `verify_exact.py` | 1,030 exact rational / Gaussian-rational checks; output path from the command line. |
| `verification_results.json` | Output of `verify_exact.py` (Python 3.11.14). |
| `refs/crossref_records.jsonl` | Crossref and arXiv records for the bibliography, fetched 3 November 2026. |
| `source_novelty_ledger.md`, `novelty_report.md` | Sources inspected, overlaps, bounded novelty assessment. |
| `CHANGES.md` | How each revision item was handled. |
| `refs.bib` | The bibliography, generated from the records in `refs/`. |
| `AI_INDEX.md` | Machine-oriented index: claims, evidence, scope and replay. |
| `RESEARCH_GATES.json` | Contribution map, sources read and limitation triage. |
| `CITATION.cff`, `.zenodo.json` | Citation and archive metadata. |
| `requirements.txt`, `.github/workflows/replay.yml` | Pinned figure dependencies and CI replay. |
| `MANIFEST.sha256` | SHA-256 of every file in the package. |

## Reproduce

With Python 3.11 or later (standard library only):

```bash
python3 -I -B verify_exact.py my_results.json        # about 2 s; refuses to overwrite an existing file
python3 -O -I -B verify_exact.py my_results_O.json   # same result: no assert statements are used
python3 -I -B verify_exact.py --self-test-mutation   # corrupts formula (5.2) and shows the failure is caught
```

Figures (Matplotlib 3.10.8, NumPy):

```bash
uv run --with matplotlib==3.10.8 --with numpy python3 -I -B make_figures.py .
```

PDF:

```bash
pandoc paper.md --from=markdown+tex_math_single_backslash+autolink_bare_uris --standalone --pdf-engine=pdflatex --output=geometric_mean_boundary_glt.pdf
```

## How to cite

Anonymous (2026). *Boundary limits of the matrix geometric mean and the failure of unrestricted GLT
closure*. Version 0.1.0-candidate. Evidence Press, unrefereed candidate. https://doi.org/10.5281/zenodo.23912963

- Version DOI: [10.5281/zenodo.23912963](https://doi.org/10.5281/zenodo.23912963); concept DOI (all versions): [10.5281/zenodo.23912962](https://doi.org/10.5281/zenodo.23912962)
- Repository: https://github.com/ipitchford/matrix-geometric-mean-glt-closure (tag `v0.1.0-candidate`)
- Release page: https://evidencepress.org/releases/matrix-geometric-mean-glt-closure/
