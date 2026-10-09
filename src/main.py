from pairwise_memory.encoding import encode_event, decode_event
from pairwise_memory.operator_role import apply_delta
from pairwise_memory.invariants import validate_invariants

def demo():
    prev = {2: 2, 3: 1}
    new = dict(prev)
    new[3] = apply_delta(prev[3], "+", 1)

    if not validate_invariants(prev, new):
        raise ValueError("Invariant violation")

    encoded = encode_event(new)
    decoded = decode_event(encoded)

    print("Encoded:", encoded)
    print("Decoded:", decoded)

if __name__ == "__main__":
    demo()
