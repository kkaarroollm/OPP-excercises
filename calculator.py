class Calculator:
    def __init__(self):
        self.ls = []

    def add(self, num1, num2):
        result = num1 + num2
        self.ls.append(f'added {num1} to {num2} got {result}')
        return print(result)

    def multiply(self, num1, num2):
        result = num1 * num2
        self.ls.append(f'multiplied {num1} and {num2} got {result}')
        return print(result)

    def print_operations(self):
        for x in self.ls:
            print(x)
        return


a = Calculator()
a.add(34, 4564)
a.multiply(32, 45)
a.add(23, 45)
a.print_operations()

