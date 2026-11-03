#!/usr/bin/env python3
"""Draw the two figures of the revised paper from proved closed-form formulas.

Usage: python3 -I -B make_figures.py OUTPUT_DIR
Writes fig1_mean_collapse.png/.pdf (main text) and figA1_spectral_envelope.png/.pdf
(Appendix A). Nothing here is numerical evidence: every plotted value is an exact
formula from the paper ((4.3), (5.5) and Theorem A.1) evaluated in floating point.
"""
import os
import sys
import tempfile
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "ep_matrix_matplotlib"))
import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
    sys.exit(__doc__)
OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 12,
    "axes.spines.top": False, "axes.spines.right": False,
    "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
})
PURPLE, ORANGE, GREY = "#6b385f", "#ad6639", "#555555"

# ---------------- Figure 1 -------------------------------------------------
fig, ax = plt.subplots(1, 2, figsize=(9.0, 3.9))
t = np.linspace(0, 10, 600)
ax[0].plot(t, 2 / np.sqrt(4 + t ** 2), color=PURPLE, lw=2)
ax[0].axhline(1, color=GREY, lw=0.8, ls=":")
ax[0].text(9.9, 1.02, "value predicted from the limits: 1", ha="right", va="bottom", fontsize=11, color=GREY)
for tv, lab, pos in [(0, "t = 0: c = 1", (2.6, 0.90)), (1.5, "t = 3/2: c = 4/5", (3.4, 0.76))]:
    cv = 2 / np.sqrt(4 + tv ** 2)
    ax[0].plot([tv], [cv], "o", color=ORANGE, ms=5, zorder=3)
    ax[0].annotate(lab, (tv, cv), xytext=pos, textcoords="data", fontsize=11, va="center",
                   arrowprops=dict(arrowstyle="-", color=GREY, lw=0.7, shrinkA=2, shrinkB=4))
ax[0].set(xlim=(0, 10), ylim=(0, 1.12), xlabel="coupling parameter t",
          ylabel="limit of the mean, c(t)")
ax[0].set_title("(a) Two inputs tending to diag(1,0)", fontsize=12, loc="left")

N = np.arange(8, 121)
m = N // 2
e = 1.0 / N
tt = np.where(N % 2 == 0, 0.0, 1.5)
s = np.sqrt(4 + tt ** 2)
tr = m / N * (2 + (2 + tt ** 2) * e ** 2) / s + (N - 2 * m) / N * e ** 2
for parity, col, lab in [(0, PURPLE, "even N: tends to 1/2"), (1, ORANGE, "odd N: tends to 2/5")]:
    sel = N % 2 == parity
    ax[1].plot(N[sel], tr[sel], "o", ms=2.6, color=col, label=lab)
ax[1].axhline(0.5, color=PURPLE, lw=0.7, ls=":")
ax[1].axhline(0.4, color=ORANGE, lw=0.7, ls=":")
ax[1].set(xlabel="matrix size N", ylabel="normalised trace of the mean",
          xlim=(8, 120), ylim=(0.36, 0.54))
ax[1].set_title("(b) Same input symbol, no output limit", fontsize=12, loc="left")
ax[1].legend(loc="center right", frameon=False, fontsize=11)
fig.tight_layout()
for ext in ("png", "pdf"):
    fig.savefig(OUT / f"fig1_mean_collapse.{ext}", dpi=220, bbox_inches="tight")
plt.close(fig)

# ---------------- Figure A.1 -----------------------------------------------
fig, ax = plt.subplots(figsize=(6.0, 4.4))
p = np.linspace(0, 1, 501)
ax.stackplot(p, 1 - p, np.minimum(p, 1 - p), np.maximum(2 * p - 1, 0),
             colors=["#9b7a9c", "#d5ae45", "#65a995"], linewidth=0,
             labels=["forced mass at 0", "free mass (any law on [0,1])", "forced mass at 1"])
ax.set(xlim=(0, 1), ylim=(0, 1), xlabel="limiting rank fraction p of the projection",
       ylabel="fraction of eigenvalues of the mean")
ax.axvline(0.5, color="#4b3a42", lw=0.8, ls=":")
ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), frameon=False, ncol=2, fontsize=11)
fig.tight_layout()
for ext in ("png", "pdf"):
    fig.savefig(OUT / f"figA1_spectral_envelope.{ext}", dpi=220, bbox_inches="tight")
plt.close(fig)
print("wrote", sorted(x.name for x in OUT.glob("fig*")))
