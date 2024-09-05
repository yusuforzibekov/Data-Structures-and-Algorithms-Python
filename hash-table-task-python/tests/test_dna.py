"""Sample tests for 'tasks.dna' module."""
from tasks.dna import find_repeated_dna_sequences


def test_find_repeated_dna_sequences_sample():
    """Sample tests for find_repeated_dna_sequences function."""
    assert find_repeated_dna_sequences('AAAATTTTAAAATTTT') == ['AAAATTTT']
    assert set(find_repeated_dna_sequences('ATATATATATA')) == set(
        ['ATATATAT', 'TATATATA'])