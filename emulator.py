class Currency:
    currencies = {
        'CHF': 0.930023,  # Swiss Franc
        'CAD': 1.264553,  # Canadian Dollar
        'GBP': 0.737414,  # British Pound
        'JPY': 111.019919,  # Japanese Yen
        'EUR': 0.862361,  # Euro
        'USD': 1.0  # US Dollar
    }

    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit

    def __repr__(self):
        return f"{round(self.value, 2)} {self.unit}"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        if isinstance(other, (int, float)):
            converted_value = other * Currency.currencies[self.unit]
        else:
            converted_value = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
        return Currency(self.value + converted_value, self.unit)

    def __iadd__(self, other):
        return self.__add__(other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            converted_value = other * Currency.currencies[self.unit]
        else:
            converted_value = other.value / Currency.currencies[other.unit] * Currency.currencies[self.unit]
        return Currency(self.value - converted_value, self.unit)

    def __isub__(self, other):
        return self.__sub__(other)

    def __rsub__(self, other):
        return Currency(other, "USD") - self

# Test cases
v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")

print(v1 + v2)  # Adding EUR to USD
print(v2 + v1)  # Adding USD to EUR
print(v1 + 3)   # Adding an int (3 USD) to EUR
print(3 + v1)   # Adding EUR to an int (3 USD)
print(v1 - 3)   # Subtracting an int (3 USD) from EUR
print(30 - v2)  # Subtracting USD from an int (30 USD)