# Standalone paper

The article is `paper.tex`, with section sources and the bibliography in the
adjacent `.tex` files. From this directory, compile it with:

```sh
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

The [audit handoff](AUDIT.md) records the proof map, figure checks, and review
status. The author's requirements are in [REQUIREMENTS.md](REQUIREMENTS.md).

The appendix verifies the parameter inequalities mathematically. Two
supplementary standard-library Python programs independently check the
previously used numerical parameter choice. From this directory run:

```sh
python verify_negative_well.py
python audit_negative_well.py
```

Both print their results and exit with an error if a check fails. The first
checks quadratic maxima using their vertices and endpoints. The second uses
Bernstein coefficients and interval subdivision. These optional checks do not
replace review of the proof or establish literature priority. The commands above
generate `paper.pdf` locally as a reading copy.

Supplementary finite checks are documented in
[`experiments/README.md`](../experiments/README.md),
[`STRUCTURAL_TESTS.md`](../experiments/STRUCTURAL_TESTS.md), and
[`SCALAR_CHARGE_TEST.md`](../experiments/SCALAR_CHARGE_TEST.md).
