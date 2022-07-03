import numpy as np
from math import factorial as fac
from numpy import power as pow


def f(successes: list, probabilities: list, trials: int) -> float:
    ks = np.array([fac(k) for k in successes])
    pks = np.array([pow(p, k) for (p, k) in zip(probabilities, successes)])
    x = np.prod(pks/ks)

    fails = trials - sum(successes)
    q = 1 - sum(probabilities)

    a = fac(trials)*pow(q, fails)
    b = fac(fails)
    return x*(a/b)


def sum_range_1(n):
    return [(a, b)
            for a in range(n+1)
            for b in range(n+1)
            if ((a + b <= n)
                and (2*a <= b)
                and a != b)]


def sum_range_2(n):
    return [(a, b, c, d)
            for a in range(n+1)
            for b in range(n+1)
            for c in range(n+1)
            for d in range(n+1)
            if ((a + b + c + d <= n)
                and (2*a <= b)
                and (2*c <= d)
                and a != b
                and c != d)]


def F(k_range, probabilities, trials):
    x = [f(ks, probabilities, trials) for ks in k_range]
    return sum(x)


def unbalance_prob(turns: int) -> None:
    k_range_1 = sum_range_1(turns)
    k_range_2 = sum_range_2(turns)
    probabilities_2 = [5.0/36, 5.0/36, 4.0/36, 4.0/36]
    probabilities_1_1 = [5.0/36, 5.0/36]
    probabilities_1_2 = [4.0/36, 4.0/36]

    results_1_1 = 2*F(k_range_1, probabilities_1_1, turns)
    results_1_2 = 2*F(k_range_1, probabilities_1_2, turns)
    results_2 = 4*F(k_range_2, probabilities_2, turns)
    results = results_1_1 + results_1_2 - results_2
    print('Imbalance prob between 6 and 8 in {} turns: {}'.format(turns,
                                                                  results_1_1))
    print('Imbalance prob between 5 and 9 in {} turns: {}'.format(turns,
                                                                  results_1_2))
    print('Imbalance prob between 6 and 8, and 5 and 9 in {} turns: {}'.format(turns, results_2))
    print('Imbalance prob between 6 and 8 or 5 and 9 in {} turns: {}'.format(turns, results))
    return None


if __name__ == '__main__':
    unbalance_prob(70)
