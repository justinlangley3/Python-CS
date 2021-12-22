import random
import signal
import sys

# Baillie-PSW primality test
def is_prime(p: int, depth: int=3):
    # small prime divisors
    small_primes = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                    107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
                    167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
                    229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
                    283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
                    359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421,
                    431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
                    491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
                    571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631,
                    641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                    709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
                    787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857,
                    859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937,
                    941, 947, 953, 967, 971, 977, 983, 991, 997}
    # 0 and 1 are not prime, nor any even number
    if p in [0, 1] or (p % 2) == 0 and p != 2:
        return False
    # 2 is the first prime value
    if p == 2:
        return True
    # for larger values, we can quickly check if they're composites of smaller primes
    if p > 997:
        if len([0 for i in small_primes if (p % i) == 0]) > 0:
            return False
    for i in range(depth):
        r = int(random.uniform(sys.float_info.min, sys.float_info.max))
        a = r % (p - 1) + 1
        if mod_pow(a, p - 1, p) != 1:
            return False
    return True


# mod_pow function for BPSW primality test
def mod_pow(a: int, b: int, c: int):
    res = 1
    for i in range(b):
        res *= a
        res %= c
    return res % c

def signal_handler(signal, frame):
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    print("BPSW Primality Test --- CTRL-C to Exit ---")

    while True:
        p = int(input('Enter a value:'))
        d = int(input('Enter iteration depth:'))
        if is_prime(p, d):
            print('%s is prime' % p)
        else:
            print('%s is composite' % p)
