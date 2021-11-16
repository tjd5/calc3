import pytest
from calc.history.calculations import Calculations
from calc.calculations.addition import Addition

@pytest.fixture
def clear_history_fixture():
    Calculations.clear_history()
@pytest.fixture
def setup_addition_calculation_fixture():
    values = (1, 2)
    addition = Addition(values)
    Calculations.add_calculation(addition)

def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    assert Calculations.count_history() == 1

def test_clear_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    assert Calculations.count_history() == 1
    Calculations.clear_history()
    assert Calculations.count_history() == 0
    assert Calculations.clear_history() == True

def test_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    assert Calculations.get_calculation(0).get_result() == 3

def test_get_calc_last_result_value(clear_history_fixture, setup_addition_calculation_fixture):
    assert Calculations.get_last_calculation_result_value() == 3

def test_get_calculation_first(clear_history_fixture, setup_addition_calculation_fixture):
    assert Calculations.get_first_calculation().get_result() == 3
def test_history_count(clear_history_fixture, setup_addition_calculation_fixture):
    assert Calculations.count_history() == 1
def test_get_calc_last_result_object(clear_history_fixture, setup_addition_calculation_fixture):
    assert isinstance(Calculations.get_last_calculation_object(), Addition)
