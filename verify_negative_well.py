"""Independent exact vertex certificate for the short parameter choice."""
from fractions import Fraction as F

U, ell, k = F('0.411323'), F('0.491938'), F('0.108423')
Q, lam, nu = F('3.820348'), F('0.252884'), F('0.003462')
low, high = F('1.41421356'), F('1.41421357')
assert low * low < 2 < high * high
roots = (low - 1, high - 1)
assert 0 < ell-k < U < ell < 1 and 0 < k < F(1, 2)
assert 1-ell > k and 0 < roots[0] < roots[1] < 1 and Q > 0
assert Q*k > roots[1]

def residual(u, c, branch, upper):
    if branch == 0:
        gamma = 0
    elif branch == 1:
        gamma = -(u-ell+k)**2/2
    elif branch == 2:
        gamma = -(ell-u)/4
    else:
        gamma = (1-k)*(u-ell)
    # Reduce using c^2=1-2c before evaluating the root endpoints.
    return (gamma + ((1-ell)*(u-U) if upper else 0)
            - Q*(c+2)*u*u/2+(Q-lam)*u+c*(lam-Q/2)-nu)

branches = ((0, ell-k, 0, False, -F(1, 10**5)),
            (ell-k, U, 1, False, -F(1, 10**9)),
            (ell-k, U, 2, False, -F(1, 10**9)),
            (U, ell, 1, True, -F(1, 10**8)),
            (U, ell, 2, True, -F(1, 10**8)),
            (ell, 1, 3, True, -F(1, 10**8)))
high_residuals = []
for left, right, branch, upper, ceiling in branches:
    for c in roots:
        # Recover the exact quadratic from three evaluations.
        y0, yp, ym = (residual(t, c, branch, upper) for t in (0, 1, -1))
        a, b = (yp+ym)/2-y0, (yp-ym)/2
        points = [left, right]
        if a < 0 and left < -b/(2*a) < right:
            points.append(-b/(2*a))
        maximum = max(residual(t, c, branch, upper) for t in points)
        assert maximum < ceiling
        high_residuals.append(maximum)

assert 1+lam-(1-ell)/U > F(1, 100)
offsets, slopes, coefficients, defects, low_margins = [], [], [], [], []
for c in roots:
    low_margin = Q*c-(1-k*(1-ell)-nu+lam*c)
    assert low_margin > F(1, 2)
    defect = Q*(1-c)/2+lam*c-nu-1-k*(2-ell)
    assert defect > F(1, 20)
    offset = (1-ell)*(1-U)+k*(1-ell)+nu-lam*(c+1)
    slope = lam-(c+2)*(k*(1-ell)+nu)
    values = (F(1), Q-k*(1-ell)-nu+lam*c,
              2*(2-U)*(1-ell)*(c+2)-k*(1-ell)-nu-lam*(c+4),
              lam*(c+1)-k*(1-ell)-nu)
    assert offset > F(3, 10**8)
    assert slope > F('0.11153757')
    assert max(values) < F('3.8665485')
    offsets.append(offset)
    slopes.append(slope)
    coefficients.extend(values)
    defects.append(defect)
    low_margins.append(low_margin)
margin = F('0.11153757')-F('0.0288468')*F('3.8665485')
assert margin == F('0.0000000187302') and margin > 0
print('vertex certificate passed')
print('worst high residual', float(max(high_residuals)))
print('minimum low margins', float(1+lam-(1-ell)/U), float(min(low_margins)))
print('minimum offset', float(min(offsets)), 'minimum slope', float(min(slopes)))
print('maximum coefficient', float(max(coefficients)), 'minimum defect', float(min(defects)))
print('exact final margin', margin)
