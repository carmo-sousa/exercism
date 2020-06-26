def convert(number):
    three = 'Pling'
    five = 'Plang'
    seven = 'Plong'

    string = []

    if number % 3 == 0:
        string.append(three)

    if number % 5 == 0:
        string.append(five)

    if number % 7 == 0:
        string.append(seven)

    if len(string) == 0:
        return str(number)

    else:
        return ''.join(string)
