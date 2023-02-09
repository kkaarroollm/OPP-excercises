class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


class LoggingCalculator(Calculator):
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = super().add(a, b)
        self.history.append(f'{a} + {b} = {result}')
        return result

    def sub(self, a, b):
        result = super().sub(a, b)
        self.history.append(f'{a} - {b} = {result}')
        return result

    def mul(self, a, b):
        result = super().mul(a, b)
        self.history.append(f'{a} * {b} = {result}')
        return result

    def div(self, a, b):
        result = super().div(a, b)
        self.history.append(f'{a} / {b} = {result}')
        return result