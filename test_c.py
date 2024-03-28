import pytest

from C import solution


@pytest.mark.parametrize('n,k,graph,expectation',
                         [
                            (5, 1, {1: [2, 3], 3: [4, 5]}, 2),
                            (2, 1, {1: [2]}, 1),
                            (6, 1, {1: [2], 2: [3], 3: [4], 4: [5], 5: [6]}, 3),
                            (3, 1, {1: [2, 3]}, 1),
                            (8, 2, {1: [2, 3], 2: [4, 5], 3: [6, 7, 8]}, 1),
                            (6, 2, {1: [2, 4], 2: [3], 4: [5], 5: [6]}, 2),
                            (4, 1, {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}, 2)]
                         )
def test_solution(n, k, graph, expectation):
    assert solution(n, k, graph) == expectation
