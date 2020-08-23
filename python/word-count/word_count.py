"""
Retorna um dicionário onde
as chaves são as palavras da sentença
e os valores são a quantidade de vezes
que ela se repete
"""

import re


def count_words(sentence):
    """ Recebe uma frase e retorna a quantidade de cada palavra  """

    new_sentence = sentence.lower()
    new_sentence = remove_special_characters(sentence)
    list_words = new_sentence.split()
    dictionary = {}

    for word in list_words:
        dictionary[word] = list_words.count(word)

    return dictionary


def remove_special_characters(sentence):
    """ Remove todos os caracteres especíais de uma sentença """

    characters = [';', ':', '?', '!', '@', '#', '%', '*', '\n', ',', '&',
                  '@', '$', '^', '&', '_', '.']

    sentence = re.sub(r"'[^a-z]|'$|[^a-z]'|^'", " ", sentence)

    for char in characters:
        sentence = sentence.replace(char, ' ')

    return sentence.lower()
