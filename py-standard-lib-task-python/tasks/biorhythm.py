"""Template for programming assignment: Calculate biorhythm"""
import math
from datetime import datetime
from collections import namedtuple

BiorhythmCycles = namedtuple('BiorhythmCycles', ['physical', 'emotional', 'intellectual'])

def calculate_biorhythm(birth_date: str, current_date: str) -> 'BiorhythmCycles':
    """
    Calculate biorhythm cycles on a given date based on birthdate.

    Biorhythm cycles are three values that are calculated using the
    following formulas:

    Physical = 100 * sin(2 * PI * t / 23)
    Emotional = 100 * sin(2 * PI * t / 28)
    Intellectual = 100 * sin(2 * PI * t / 33)

    where *t* is the number of days since birth. Please round them
    to the nearest integers before returning an output.

    For more information on biorhythms, please read the corresponding
    Wikipedia article:
    https://en.wikipedia.org/wiki/Biorhythm_(pseudoscience)

    Args:
        birth_date: str
            A string containing birthdate in the format YYYY-MM-DD.
        current_date: str
            A string containing a given date of calculation in the
            format YYYY-MM-DD.
    Returns:
        BiorhythmCycles, a named tuple with three integer properties:
        "physical", "emotional" and "intellectual".
    """
    birth = datetime.strptime(birth_date, '%Y-%m-%d')
    current = datetime.strptime(current_date, '%Y-%m-%d')
    days = (current - birth).days
    
    physical = round(100 * math.sin(2 * math.pi * days / 23))
    emotional = round(100 * math.sin(2 * math.pi * days / 28))
    intellectual = round(100 * math.sin(2 * math.pi * days / 33))
    
    return BiorhythmCycles(physical, emotional, intellectual)
