from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    mynumbers = (1.0,2.0)
    subtraction = Subtraction(mynumbers)
    assert subtraction.get_result() == -3
