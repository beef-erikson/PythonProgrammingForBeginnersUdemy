"""Raising an exception and custom exception class example.
"""


class CurrenciesDoNotMatchError(Exception):
    """Custom exception class.
    """
    def __init__(self, message: str):
        super().__init__(message)


class Currency:
    def __init__(self, currency: str, amount: float) -> None:
        """Initialization of class, defines currency and amount.
        """
        self.currency = currency
        self.amount = amount

    def __repr__(self):
        """Representation of class, returns currency and amount.
        """
        return repr((self.currency, self.amount))

    def __add__(self, other):
        """Defines the logic when adding values together.
        """
        # If the currency type doesn't match, throw exception
        if self.currency != other.currency:
            raise CurrenciesDoNotMatchError(self.currency + ' ' + other.currency)

        total_amount = self.amount + other.amount
        return Currency(self.currency, total_amount)


value1 = Currency('USD', 20)
value2 = Currency('USD', 50)
print(value1 + value2)

value3 = Currency('INR', 20)
print(value2 + value3)
