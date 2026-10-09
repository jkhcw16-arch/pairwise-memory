def parity_invariant(exponents: dict[int, int]) -> bool:
    # Example: enforce even parity on prime 2
    return exponents.get(2, 0) % 2 == 0


def growth_invariant(prev: dict[int, int], new: dict[int, int]) -> bool:
    # Example: monotonic growth on prime 3
    return new.get(3, 0) >= prev.get(3, 0)


def validate_invariants(prev: dict[int, int], new: dict[int, int]) -> bool:
    return parity_invariant(new) and growth_invariant(prev, new)
