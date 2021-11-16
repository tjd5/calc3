from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
class Calculations:
    history = []
    @staticmethod
    def clear_history():
        Calculations.history.clear()
        return True
    @staticmethod
    def count_history():
        return len(Calculations.history)
    @staticmethod
    def get_last_calculation_object():
        return Calculations.history[-1]
    @staticmethod
    def get_last_calculation_result_value():
        calculation = Calculations.get_last_calculation_object()
        return calculation.get_result()
    @staticmethod
    def get_first_calculation():
        return Calculations.history[0]
    @staticmethod
    def get_calculation(num):
        return Calculations.history[num]
    @staticmethod
    def add_calculation(calculation):
        return Calculations.history.append(calculation)
    @staticmethod
    def add_addition_calculation(values):
        Calculations.add_calculation(Addition.create(values))
        #Get the result of the calculation
        return True
    @staticmethod
    def add_subtraction_calculation(values):
        Calculations.add_calculation(Subtraction.create(values))
        return True
    @staticmethod
    def add_multiplication_calculation(values):
        Calculations.add_calculation(Multiplication.create(values))
        return True
