##############################
########### Task 7 ###########
##############################

import json
from functools import reduce

from solutions.rsa import int2bytes


def invpow(x, n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    Taken from https://stackoverflow.com/questions/55436001/cube-root-of-a-very-large-number-using-only-math-library
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid ** n < x:
            low = mid
        elif high > mid and mid ** n > x:
            high = mid
        else:
            return mid
    return mid + 1


if __name__ == "__main__":
    with open("../message_captured", "r") as f:
        messages = [json.loads(line) for line in f]

    e = messages[0]["e"]  # expected to be identical for all the messages

    # Chinese remainder theorem:
    # in Z_n, where n = n_1 * n_2 * n_3
    # m^3 = c_1 * g_(n_1) + c_2 * g_(n_2) + c_3 * g_(n_3)
    #   g_(n_1) = n_2 * n_3 * t, where t = (n_1 * n_2)^(-1) mod n_1
    #   ...

    # debugging example from MKR lecture
    # messages = [{"n": 87, "data": 63}, {"n": 115, "data": 56}, {"n": 187, "data": 68}]

    n = 1
    m_to_e = 0
    for msg in messages:
        n_i = msg["n"]
        n *= n_i
        c_i = msg["data"]
        copy = list(messages)
        copy.remove(msg)
        other_n = reduce(lambda a, b: a["n"] * b["n"], copy)
        t = pow(other_n, -1, n_i)
        g_n_i = other_n * t
        m_to_e += c_i * g_n_i

    m_to_e = m_to_e % n
    m = invpow(m_to_e, e)
    message = int2bytes(m).decode()
    print(f"The cracked message is: {message!r}")
