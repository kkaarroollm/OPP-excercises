class Employee:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self._salary = 0.0

    def ser_salary(self, salary):
        if isinstance(salary,(int, float)) and salary >= 0:
            self._salary += salary
            return f'salary is: {self._salary}'
        else:
            raise ValueError('its not number')


a = Employee(1, 'karol', 'mar')
print(a.ser_salary(-23))
