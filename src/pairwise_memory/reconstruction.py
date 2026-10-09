from .operator_role import Operator, Role

def rollback_exponent(exponent: int, operator: Operator, role: Role) -> int:
    delta = -(0 if operator == "-" else role)
    return exponent + delta


def rollback_event(exponents: dict[int, int],
                   prime: int,
                   operator: Operator,
                   role: Role) -> dict[int, int]:
    new_exps = dict(exponents)
    new_exps[prime] = rollback_exponent(new_exps.get(prime, 0), operator, role)
    return new_exps
