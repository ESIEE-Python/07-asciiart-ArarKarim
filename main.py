#### Imports et définition des variables globales


#### Fonctions secondaires


"""
Ce module fournit des fonctions pour encoder une chaîne de caractères
en une liste de tuples représentant les caractères consécutifs et leur fréquence.
"""

def artcode_i(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument
    selon un algorithme itératif.

    Args:
        s (str): la chaîne de caractères à encoder.

    Returns:
        list: la liste des tuples (caractère, nombre d'occurrences).
    """
    if not s:  # Gérer le cas où la chaîne est vide
        return []

    characters = [s[0]]  # Liste des caractères rencontrés
    occurrences = [1]    # Liste des occurrences correspondantes

    for k in range(1, len(s)):
        if s[k] == s[k - 1]:
            occurrences[-1] += 1  # Incrémente la dernière occurrence
        else:
            characters.append(s[k])  # Ajoute un nouveau caractère
            occurrences.append(1)    # Initialise son occurrence à 1

    return list(zip(characters, occurrences))  # Combine les deux listes en une liste de tuples


def artcode_r(s):
    """
    Retourne la liste de tuples encodant une chaîne de caractères passée en argument
    selon un algorithme récursif.

    Args:
        s (str): la chaîne de caractères à encoder.

    Returns:
        list: la liste des tuples (caractère, nombre d'occurrences).
    """
    if not s:  # Cas de base : si la chaîne est vide
        return []

    def helper(sub_s):
        """
        Fonction récursive pour encoder la sous-chaîne.

        Args:
            sub_s (str): La sous-chaîne à encoder.

        Returns:
            list: La liste des tuples pour la sous-chaîne.
        """
        if not sub_s:  # Sous-cas de base : si la sous-chaîne est vide
            return []

        char = sub_s[0]  # Premier caractère
        count = 1

        # Compte les occurrences du premier caractère
        while count < len(sub_s) and sub_s[count] == char:
            count += 1

        # Retourne un tuple avec l'appel récursif sur la partie restante
        return [(char, count)] + helper(sub_s[count:])

    return helper(s)


def main():
    """
    Fonction principale pour tester les fonctions d'encodage avec plusieurs chaînes.
    """
    # Chaînes de test
    test_strings = [
        "MMMMaaacXolloMM",
        "aaabbcccc",
        "",
        "a",
        "abc",
        "aaaa",
    ]

    # Affiche les résultats pour chaque chaîne
    for s in test_strings:
        print(f"Chaîne : {s}")
        print(f"Encodage itératif : {artcode_i(s)}")
        print(f"Encodage récursif : {artcode_r(s)}")
        print("-" * 40)


if __name__ == "__main__":
    main()
