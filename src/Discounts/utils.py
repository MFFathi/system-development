# Author: Mohamed Elafifi
"""Module with validation logic for discounts."""
DESCRIPTION_MIN_LEN = 5  # INCLUSIVE
DESCRIPTION_MAX_LEN = 200  # INCLUSIVE


def validate_description(description: str):
    """Validate discount description."""
    ABOVE_MIN = len(description) >= DESCRIPTION_MIN_LEN
    BELOW_MAX = len(description) <= DESCRIPTION_MAX_LEN

    return ABOVE_MIN and BELOW_MAX