"""Independent exact Bernstein certificate for the short parameter choice."""
from fractions import Fraction as R

sqrt_lo, sqrt_hi = R('1.41421356'), R('1.41421357')
assert sqrt_lo**2 < 2 < sqrt_hi**2
roots = [sqrt_lo-1, sqrt_hi-1]
cut, level = R('0.411323'), R('0.491938')
width, weight = R('0.108423'), R('3.820348')
linear, intercept = R('0.252884'), R('0.003462')
left_well, length = level-width, 1-level
assert 0 < left_well < cut < level < 1
assert 0 < width < R(1, 2) and length > width and 0 < roots[0] < roots[1] < 1 and weight > 0
assert width*weight > roots[1]

def certify(poly, start, end, ceiling):
    """Quadratic Bernstein coefficients bound a polynomial on each segment."""
    a, b, d = poly
    pending, count = [(start, end)], 0
    while pending:
        lo, hi = pending.pop()
        count += 1
        assert count < 10000
        p0 = a*lo*lo+b*lo+d
        p2 = a*hi*hi+b*hi+d
        p1 = p0+(hi-lo)*(2*a*lo+b)/2
        if max(p0, p1, p2) >= ceiling:
            mid = (lo+hi)/2
            pending.extend(((lo, mid), (mid, hi)))
    return count

pieces = ((0, left_well, (R(0), R(0), R(0)), False, -R(1, 10**5)),
          (left_well, cut, (-R(1, 2), left_well, -left_well**2/2), False,
           -R(1, 10**9)),
          (left_well, cut, (R(0), R(1, 4), -level/4), False, -R(1, 10**9)),
          (cut, level, (-R(1, 2), left_well, -left_well**2/2), True,
           -R(1, 10**8)),
          (cut, level, (R(0), R(1, 4), -level/4), True, -R(1, 10**8)),
          (level, R(1), (R(0), 1-width, -(1-width)*level), True, -R(1, 10**8)))
for lo, hi, (a, b, d), capped, ceiling in pieces:
    if capped:
        b, d = b+length, d-length*cut
    for c in roots:
        residual = (a-weight*(c+2)/2, b+weight-linear,
                    d+(linear-weight/2)*c-intercept)
        certify(residual, lo, hi, ceiling)

assert 1+linear-length/cut > R(1, 100)
for c in roots:
    assert weight*c-(1-width*length-intercept+linear*c) > R(1, 2)
    assert weight*(1-c)/2+linear*c-intercept-1-width*(2-level) > R(1, 20)
    assert length*(1-cut)+width*length+intercept-linear*(c+1) > R(3, 10**8)
    assert linear-(c+2)*(width*length+intercept) > R('0.11153757')
    assert max(1, weight-width*length-intercept+linear*c,
               2*(2-cut)*length*(c+2)-width*length-intercept-linear*(c+4),
               linear*(c+1)-width*length-intercept) < R('3.8665485')
assert R('0.11153757')-R('0.0288468')*R('3.8665485') == R('0.0000000187302')
print('Bernstein certificate passed')
