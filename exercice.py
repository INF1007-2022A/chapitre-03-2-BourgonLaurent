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


def format_base(value: int, base: int, digit_letters: str):
    """
    Formater un nombre dans une base donnée en utilisant les lettres fournies pour les chiffres <
    `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
    """
    result = ""
    abs_value = abs(value)

    # Calculer quelle est la première base
    # pour laquelle value est plus petite
    max_exponent = 0
    while abs_value >= base**max_exponent:
        max_exponent += 1

    # value ne va jamais dépasser base ** max_exponent
    # alors on commence à celle en-dessous
    curr_exp = max_exponent - 1

    # Nombre de fois qu'on pourra soustraire
    # la base actuelle
    coeff = 0

    while True:
        if abs_value >= base**curr_exp:
            coeff += 1
            abs_value -= base**curr_exp
        else:
            # Ajouter le coefficient à la prochaine position
            result += digit_letters[coeff]

            # Puisque abs_value est toujours positif,
            # une valeur nulle signifie que la
            # valeur est totalement convertie
            if abs_value == 0 and curr_exp == 0:
                break

            # Réinitialiser le compteur de base
            coeff = 0
            # Passer à la base inférieure
            curr_exp -= 1

    # Ajouter '-' devant pour les nombres négatifs.
    if value < 0:
        result = "-" + result
    return result


if __name__ == "__main__":
    print(dissipated_power(69, 420))
    print(orthogonal((1, 1), (-1, 1)))
    print(average([1, 4, -2, 10]))
    print(bills(137))
    print(format_base(-42, 16, "0123456789ABCDEF"))
