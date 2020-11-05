class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if not self.card_num.isdigit():
            return False

        if len(self.card_num) <= 1:
            return False

        number = int(self.card_num[:-1])
        length = len(self.card_num)
        parity = length % 2

        for i in range(length - 1):
            digit = int(self.card_num[i])

            if i % 2 == parity:
                digit = digit * 2

            if digit >= 9:
                digit = digit - 9

            number = number + digit

        print(number % 10)

        return number % 10 == 0
