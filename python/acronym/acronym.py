import re


def abbreviate(words):
    words = re.sub('-|_', ' ', words)
    words = words.replace("'", '')
    words = words.title()

    sigla = re.findall('[A-Z]', words)

    return ''.join(sigla)
