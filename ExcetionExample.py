class Amount:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def add(self, that):
        if self.currency == that.currency:
            self.amount += that.amount
        else:
            raise CurrencyDoNotMatchException(self.currency + ' ' + that.currency)

    def __repr__(self):
        return repr((self.currency, self.amount))


class CurrencyDoNotMatchException(Exception):
    def __init__(self, message):
        super().__init__(message)


amount1 = Amount('INR', 100)
amount2 = Amount('USD', 200)

amount2.add(amount1)

print(amount2)
