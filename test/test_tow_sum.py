import pytest

from problems.two_sum import two_sum


@pytest.mark.parametrize(
    "set_input_1, set_input_2, set_output",
    (
            (  # test case 1
                    [2, 7, 11, 15],
                    9,
                    [0, 1],
            ),
            (  # test case 2
                    [2, 7, 11, 15],
                    9,
                    [0, 1],
            ),
    )
)
def test_two_sum(set_input_1, set_input_2, set_output):
    result = two_sum(set_input_1, set_input_2)
    assert result == set_output