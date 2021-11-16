from calc.calculations.addition import Addition

def test_calculation_addition():
    mynumbers = (1.0,2.0)
    addition = Addition(mynumbers)
    assert addition.get_result() == 3.0
