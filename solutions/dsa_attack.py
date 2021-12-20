##############################
########### Task 9 ###########
##############################


def recover_private_key(dsa_params, dsa_sign, H, y) -> int:
    p, q, g = dsa_params
    r, s = dsa_sign
    # s = k^(-1) * (H(m) + xr)   mod q
    # (s * k - H(m)) * r^(-1) = x   mod q
    r_inv = pow(r, -1, q)
    # brute force k (only 2^16 values)
    for k in range(2 ** 16):
        x = ((s * k - H) * r_inv) % q
        if pow(g, x, p) == y:
            return x
