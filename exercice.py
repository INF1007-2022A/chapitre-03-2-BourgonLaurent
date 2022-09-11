#!/usr/bin/env python


from typing import List, Tuple


def dissipated_power(voltage: float, resistance: float) -> float:
    """Calculer la puissance dissipée par la résistance (P = V^2 / R)."""
    return voltage**2 / resistance


def orthogonal(v1: Tuple[int, int], v2: Tuple[int, int]) -> bool:
    """Retourner vrai si les vecteurs sont orthogonaux, faux sinon."""
    return (v1[0] * v2[0] + v1[1] * v2[1]) == 0


def average(values: List[int]) -> float:
    """Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives)."""
    pos_values = [v for v in values if not v < 0]
    return sum(pos_values) / len(pos_values)


def bills(value):
    """Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur."""
    twenties = 0
    tens = 0
    fives = 0
    ones = 0
    while value != 0:
        if value >= 20:
            value -= 20
            twenties += 1
        elif value >= 10:
            value -= 10
            tens += 1
        elif value >= 5:
            value -= 5
            fives += 1
        elif value >= 1:
            value -= 1
            ones += 1

    return (twenties, tens, fives, ones)


def format_base(value, base, digit_letters):
    # Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
    # `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
    result = ""
    abs_value = abs(value)
    while abs_value != 0:
        pass
    if value < 0:
        # TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
        pass
    return result


if __name__ == "__main__":
    print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(average([1, 4, -2, 10]))
    print(bills(137))
    print(format_base(-42, 16, "0123456789ABCDEF"))
