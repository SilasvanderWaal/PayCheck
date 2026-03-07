from typing import List
from app.models.break_rule import BreakRule


def calculate_break_duration(shift_hours: float, break_rules: List[BreakRule]) -> int:
    """
    Sum break minutes from all matching rules.
    A rule matches if the shift is longer than min_shift_hours.
    Returns total break minutes as an integer.
    """
    total_minutes = 0
    for rule in break_rules:
        if shift_hours > float(rule.min_shift_hours):
            total_minutes += rule.break_minutes
    return total_minutes