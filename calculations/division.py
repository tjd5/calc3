from calc.calculations.calculation import Calculation

class Divison(Calculation):
    def getresult(self):
        result = 1.0
        for value in self.values:
            result = result // value
        return result
