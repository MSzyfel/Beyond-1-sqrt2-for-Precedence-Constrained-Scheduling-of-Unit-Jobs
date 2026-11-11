# Manuscript audit handoff

The standalone article is [paper.tex](paper.tex), with a compiled reading copy
in [paper.pdf](paper.pdf). It is based on the earlier
[working draft](../research/scheduling_metaoptimized_draft.tex). The article
states a deterministic polynomial-time approximation ratio of
`1 + sqrt(2) - 0.0288468`, approximately `2.3853667624`, for unit-time
precedence-constrained jobs on an input-dependent number of identical machines.
The author's continuing requirements are in [REQUIREMENTS.md](REQUIREMENTS.md).

## Proof map

1. [preliminaries.tex](preliminaries.tex) gives the time-indexed LP, virtual
   capacity padding, and interpolated completion quantiles.
2. [early.tex](early.tex) develops the priority-prefix bounds, scalar excess,
   priority-band progress, virtual-pool transfer, and the partial pool.
3. [late.tex](late.tex) combines the geometric excess bound and scalar charges
   through a signed-moment identity to obtain the per-job estimate.
4. [certificate.tex](certificate.tex) gives deterministic selection, the final
   guarantee, and the appendix's exact parameter inequalities.

The current article uses a different, simpler parameter certificate from the
earlier working note. Its appendix also gives a parametric sufficient family
and optimization problem, using upper quantile endpoint `1` and a common
coefficient for both scalar cases. No equivalence with the working note's
broader family is asserted. In particular, the working note's more general
certificate with a variable upper endpoint and a separate low-crossing charge
is not reproduced in full. The appendix verifies the chosen parameters using
direct inequalities and completed squares. The following optional independent
checks of the same numerical choice were retained from the previous audit:

```sh
python verify_negative_well.py
python audit_negative_well.py
```

The first checks rational quadratic vertices and endpoints. The second uses
Bernstein coefficients and subdivision. Both passed during this audit. They
check the finite numerical conditions, not the continuous proof as a whole.
Rational optimization parameters or rational computational certification are
not required by the author's current instructions. Compilation
instructions are in [README.md](README.md).

## Figures and supplementary checks

- Figure 1 has four machines, ten depicted predecessors, and seven independent
  band jobs. [figure_one_exact.py](../experiments/figure_one_exact.py) checks a
  feasible LP realization, the `(5.9, 7]` band, padding, schedule, and heights.
- Figure 2 uses a left-continuous profile with a jump at `0.55`. Its failure set
  is `(0.85, 1]`. [figure_two_exact.py](../experiments/figure_two_exact.py)
  checks a feasible four-job LP realization and the exact region areas. The
  intersections with the outlined region have areas `27/800` and `9/800`,
  which add to the stated overlap bound `9/200`.
  An inspected right-continuous variant was valid for the general geometric
  lemma but did not have the left continuity of the quantile profiles. The
  available files do not establish which earlier figure the author meant.
- The [experiment guide](../experiments/README.md) documents exact small-LP
  rounding checks. The [structural](../experiments/STRUCTURAL_TESTS.md) and
  [scalar](../experiments/SCALAR_CHARGE_TEST.md) guides describe additional
  finite stress tests. Their samples and limitations are stated there.
- [ELL_HALF_CERTIFICATE.md](../experiments/ELL_HALF_CERTIFICATE.md) records an
  exploratory exact exclusion of `ell = 1/2` within specified conditions of the
  present certificate, including a nonnegative depth coefficient. It is not
  used in the article and does not rule out the negative-coefficient case or
  a different proof or certificate.
- [negative_depth_certificate.py](../experiments/negative_depth_certificate.py)
  checks a feasible parameter choice with a negative depth coefficient and a
  positive improvement. This illustrates the second case in the general
  certificate, though it does not attain the sharper stated improvement.
- [boundary_equality_certificate.py](../experiments/boundary_equality_certificate.py)
  checks a feasible choice with `Q*kappa = c`, the weak-inequality boundary
  allowed by the general certificate.

## Attribution and remaining review

The related-work section was expanded after a primary-source audit to cover
fractional priorities, release dates and precedence delays, preemption,
related machines, structured precedence orders, and inapproximability.
Each result is stated with its relevant model assumptions. A targeted search
of recent literature did not identify a stronger approximation for the exact
input-dependent-machine model, but it cannot establish priority conclusively.

The numbered Li 2017 results cited in the article use the linked full version,
not the differently numbered FOCS proceedings. The precise Bansal–Khot
hypothesis is cited through Svensson's accessible formulation. The earlier
Munier–Queyranne–Schulz result is stated for the general precedence-delay
setting supported by that source.

These are internal mathematical, numerical, and literature checks. Finite
tests do not prove the theorem. Independent external review of the full proof
and a comprehensive literature-priority check remain necessary before treating
the claimed improvement as established.
