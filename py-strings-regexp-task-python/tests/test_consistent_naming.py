"""Sample tests for 'tasks.consistent_naming' module."""
from tasks.consistent_naming import make_naming_consistent


def test_make_naming_consistent():
    # Sample test 1
    code = expected_code = 'initNumber = 1'
    assert make_naming_consistent(code) == expected_code

    # Sample test 2
    code = '\n'.join([
        'for a_i, b_i in zip(aList, bList):',
        '    print(a_i, b_i)'
    ])
    expected_code = '\n'.join([
        'for a_i, b_i in zip(a_list, b_list):',
        '    print(a_i, b_i)'
    ])
    assert make_naming_consistent(code) == expected_code

    # Sample test 3
    code = '\n'.join([
        '_abc_ = 0',
        'variableABC10 = 1',
        'if _abc_ < variableABC10:',
        '    print(_abc_)'
    ])
    expected_code = '\n'.join([
        '_abc_ = 0',
        'variable_abc_10 = 1',
        'if _abc_ < variable_abc_10:',
        '    print(_abc_)'
    ])
    assert make_naming_consistent(code) == expected_code

    # Sample test 4
    code = '\n'.join([
        '_ab__c_ = 0',
        'variableABC10 = 1',
        'if _ab__c_ < variableABC10',
        '    print(variableABC10)'
    ])
    expected_code = '\n'.join([
        'abC = 0',
        'variableABC10 = 1',
        'if abC < variableABC10',
        '    print(variableABC10)'
    ])
    assert make_naming_consistent(code) == expected_code
