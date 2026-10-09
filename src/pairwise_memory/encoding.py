from .primes import PRIMES

def encode_event(exponents: dict[int, int]) -> int:
    """
    Encode event as composite integer M = ∏ p^{r_p}
    """
    value = 1
    for p in PRIMES:
        r = exponents.get(p, 0)
        if r:
            value *= p ** r
    return value


def decode_event(value: int) -> dict[int, int]:
    """
    Factor composite integer back into prime exponents.
    """
    exps = {}
    for p in PRIMES:
        r = 0
        while value % p == 0:
            value //= p
            r += 1
        if r > 0:
            exps[p] = r
    return exps
