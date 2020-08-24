list_of_all_letters: str = 'abcdefghijklmnopqrstuvwxyz'


def is_pangram(sentence: str) -> bool:
    for letter in list_of_all_letters:
        if letter not in sentence.lower():
            return False
    return True
