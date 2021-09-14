#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_even_len(string: str) -> bool:
    if len(string)%2 == 0 :
        return string


def remove_third_char(string: str) -> str:
    nouvelle_chaine = ""
    for lettre in string :
        if lettre != string[2] :
            nouvelle_chaine += lettre
    return nouvelle_chaine


def replace_char(string: str, old_char: str, new_char: str) -> str:
    nouvelle_chaine = ""
    for lettre in string :
        if lettre != old_char :
            nouvelle_chaine += lettre
        else :
            nouvelle_chaine += new_char
    return nouvelle_chaine


def get_number_of_char(string: str, char: str) -> int:
    c = 0
    for lettre in string :
        if lettre == char :
            c += 1
    return c


def get_number_of_words(sentence: str, word: str) -> int:
    c1 = 0
    for i in range(len(sentence)):
        if sentence[i] == word[0] :
            if sentence[i+1] == word[1] :
                if sentence[i+2] == word[2] :
                    c1 += 1
    return c1


def main() -> None:
    chaine = "Bonjour!"
    if is_even_len(chaine):
        print(f"Le nombre de caractère dans la chaine {chaine} est pair")
    else:
        print(f"Le nombre de caractère dans la chaine {chaine} est impair")

    chaine = "salut monde!"
    print(f"On supprime le 3e caratère dans la chaine: {chaine}. Résultat : {remove_third_char(chaine)}")

    chaine = "hello world!"
    print(f"On remplace le caratère w par le caractère z dans la chaine: {chaine}. Résultat : {replace_char(chaine, 'w', 'z')}")

    print(f"Le nombre d'occurrence de l dans hello world! est : {get_number_of_char(chaine, 'l')}")
    
    chaine = "Baby shark doo doo doo doo doo doo"
    print(f"L'occurence du mot doo dans la chaine {chaine} est: {get_number_of_words(chaine, 'doo')}")


if __name__ == '__main__':
    main()
