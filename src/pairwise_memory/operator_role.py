Operator = str  # "+" or "-"
Role = int      # 1 or 2

def delta(operator: Operator, role: Role) -> int:
    """
    Δ(O,R) = 0 if O = -
             R if O = +
    """
    return 0 if operator == "-" else role


def apply_delta(exponent: int, operator: Operator, role: Role) -> int:
    return exponent + delta(operator, role)
