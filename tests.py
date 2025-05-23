import numpy as np

import pytest

from fishersrc.cfisher import pvalue, pvalue_npy

# Computed by ``fisher.test`` in R 3.2.2 and printed with
# ``sprintf(".16f")``.
@pytest.mark.parametrize("table,expected", [
    ([[100, 2], [1000, 5]],
     (0.1300759363430016, 0.9797904453147230, 0.1300759363430016)),
    ([[2, 100], [5, 1000]],
     (0.9797904453147230, 0.1300759363430016, 0.1300759363430016)),
    ([[2, 7], [8, 2]],
     (0.0185217259520665, 0.9990149169715733, 0.0230141375652212)),
    ([[5, 1], [10, 10]],
     (0.9782608695652173, 0.1652173913043478, 0.1973244147157191)),
    ([[5, 15], [20, 20]],
     (0.0562577507439996, 0.9849086665340765, 0.0958044001247763)),
    ([[5, 16], [20, 25]],
     (0.0891382278309642, 0.9723490195633506, 0.1725864953812995)),
    ([[10, 5], [10, 1]],
     (0.1652173913043479, 0.9782608695652174, 0.1973244147157192)),
    ([[10, 5], [10, 0]],
     (0.0565217391304348, 1.0000000000000000, 0.0612648221343874)),
    ([[5, 0], [1, 4]],
     (1.0000000000000000, 0.0238095238095238, 0.0476190476190476)),
    ([[0, 5], [1, 4]],
     (0.5000000000000000, 1.0000000000000000, 1.0000000000000000)),
    ([[5, 1], [0, 4]],
     (1.0000000000000000, 0.0238095238095238, 0.0476190476190476)),
    ([[0, 1], [3, 2]],
     (0.4999999999999999, 1.0000000000000000, 1.0000000000000000))
])
def test_against_r(table, expected):
    epsilon = 1e-10
    p = pvalue(table[0][0], table[0][1], table[1][0], table[1][1])
    assert abs(p.left_tail - expected[0]) < epsilon
    assert abs(p.right_tail - expected[1]) < epsilon
    assert abs(p.two_tail - expected[2]) < epsilon
