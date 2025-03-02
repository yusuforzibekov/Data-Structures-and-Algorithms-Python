"""Sample tests for programming assignment: Calculate biorhythm"""
from tasks.biorhythm import calculate_biorhythm, BiorhythmCycles


def test_calculate_biorhythm():
    # Sample tests
    assert calculate_biorhythm('1990-10-15', '2023-02-22') == BiorhythmCycles(-89, 43, 69)
    assert calculate_biorhythm('1974-01-29', '2011-12-14') == BiorhythmCycles(40, 22, 91)
