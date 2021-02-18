class Worker:

    def __init__(self, name, surname, position, **income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_total_income(self):
        return self._income['wage']+self._income['bonus']


p = Position(name='Mark', surname='Zuckerberg', position='developer', wage=5, bonus=5)
print(f'full name is {p.get_full_name()}')
print(f'total income is {p.get_total_income()}')


