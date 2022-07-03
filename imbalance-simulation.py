from numpy.random import randint, shuffle
import numpy as np
import time
# Checks for imbalances by simulating dice rolls using rng's for random dice
# and modified "dice decks" for balanced dice following Colonist.io.


def balanced_rolls(turns: int) -> list:
    """
    Partially simulates the balanced dice from Colonist.io and produces a list of
    balanced rolls in a game. Unlike the Colonist.io algorithm, does not avoid
    repeated numbers in sequence, ie rolling streaks.
    :param turns: the number of turns in a game.
    :return: sample of balanced rolls.
    """
    outcomes = [i+j for i in range(1, 7) for j in range(1, 7)]
    shuffles = turns // 24
    left_overs = turns % 24
    rolls = []
    for _ in range(shuffles):
        deck = outcomes.copy()
        shuffle(deck)
        rolls += deck[0:24]
    if left_overs > 0:
        deck = outcomes.copy()
        shuffle(deck)
        rolls += deck[0:left_overs]
    return rolls


def unbalanced(val1: int, val2: int, seq: list) -> bool:
    """
    Given two values and a sequence of integers, checks if one value occurs
    at least twice as many times than the other in the sequence.
    """
    c1 = float(seq.count(val1))
    c2 = float(seq.count(val2))
    if c1 == c2:
        return False
    elif c1*c2 == 0:
        return True
    else:
        return bool(c1/c2 >= 2 or c2/c1 >= 2)


def check_random_dice(turns_per_game: int, trials: int) -> None:
    # values with 5 pips:
    v1 = 6
    v2 = 8

    # values with 4 pips:
    v3 = 5
    v4 = 9

    # List for checking imbalance in 5 pips and list for checking imbalance in both 5 and 4 pips:
    results_one = []
    results_two = []

    for i in range(trials):
        d1 = randint(low=1, high=7, size=turns_per_game)
        d2 = randint(low=1, high=7, size=turns_per_game)
        rolls = list(np.array(d1) + np.array(d2))
        result1 = unbalanced(val1=v1, val2=v2, seq=rolls)
        result2 = unbalanced(val1=v3, val2=v4, seq=rolls)
        results_one.append(result1)
        results_two.append((result1 or result2))

    print('Random dice results:')
    print('Imbalance prob between 6 and 8 in {} turns: {}'.format(turns_per_game,
                                                                  results_one.count(True) / trials))
    print('Imbalance prob between 6 and 8 or 5 and 9 in {} turns: {}'.format(turns_per_game,
                                                                             results_two.count(True) / trials))
    return None


def check_balanced_dice(turns_per_game: int, trials: int) -> None:
    # values with 5 pips:
    v1 = 6
    v2 = 8
    # values with 4 pips:
    v3 = 5
    v4 = 9
    # List for checking imbalance in 5 pips and list for checking imbalance in both 5 and 4 pips:
    results_one = []
    results_two = []

    for i in range(trials):
        rolls = balanced_rolls(70)
        result1 = unbalanced(val1=v1, val2=v2, seq=rolls)
        result2 = unbalanced(val1=v3, val2=v4, seq=rolls)
        results_one.append(result1)
        results_two.append((result1 or result2))

    print('Balanced dice results:')
    print('Imbalance prob between 6 and 8 in {} turns: {}'.format(turns_per_game, results_one.count(True) / trials))
    print('Imbalance prob between 6 and 8 or 5 and 9 in {} turns: {}'.format(turns_per_game,
                                                                             results_two.count(True) / trials))

    return None


def main():
    turns = 35
    trials = 1000000
    print('Number of turns: ', turns)
    print('Number of trials: ', trials, '\n')

    start = time.time()
    check_balanced_dice(turns_per_game=turns, trials=trials)
    end = time.time()
    elapsed = time.strftime("%Hh%Mm%Ss", time.gmtime(end - start))
    print('Elapsed time: {}'.format(elapsed), '\n')

    start = time.time()
    check_random_dice(turns_per_game=turns, trials=trials)
    end = time.time()
    elapsed = time.strftime("%Hh%Mm%Ss", time.gmtime(end - start))
    print('Elapsed time: {}'.format(elapsed))


if __name__ == '__main__':
    main()


