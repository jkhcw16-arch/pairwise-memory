from .operator_role import apply_delta, Operator, Role

def correct_anomaly(exponents: dict[int, int],
                    prime: int,
                    operator: Operator,
                    role: Role) -> dict[int, int]:
    """
    M_corrected = M' · p^{Δ(O,R)}
    """
    new_exps = dict(exponents)
    new_exps[prime] = apply_delta(new_exps.get(prime, 0), operator, role)
    return new_exps
