def is_isogram(string):
    string = string.replace(' ', '').replace('-', '').lower()

    if len(string) != 0:

        for letter in string:
            if string.count(letter) > 1:
                return False

        return True

    else:
        return True
