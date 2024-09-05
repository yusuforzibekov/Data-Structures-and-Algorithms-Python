"""Sample tests for 'tasks.rpn' module."""
from tasks.rpn import evaluate_rpn_tokens


def test_evaluate_rpn_tokens_sample():
    """Sample tests for evaluate_rpn_tokens function."""
    assert evaluate_rpn_tokens(['3', '2', '+', '10', '*']) == 50

    assert evaluate_rpn_tokens(['10', '4', '-', '2', '*', '5', '/']) == 2
