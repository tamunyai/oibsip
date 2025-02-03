from math import isclose

import pytest
from bmi_calculator import calculate_bmi, classify_bmi


def test_calculate_bmi():
    """Test the BMI calculation with various inputs."""
    assert isclose(calculate_bmi(70, 1.75), 22.86, rel_tol=0.01)
    assert isclose(calculate_bmi(50, 1.6), 19.53, rel_tol=0.01)
    assert isclose(calculate_bmi(90, 1.8), 27.78, rel_tol=0.01)
    assert isclose(calculate_bmi(110, 1.7), 38.06, rel_tol=0.01)


def test_classify_bmi():
    """Test BMI classification based on BMI values."""
    assert classify_bmi(17) == "Underweight"
    assert classify_bmi(22) == "Normal weight"
    assert classify_bmi(27) == "Overweight"
    assert classify_bmi(32) == "Obesity Class I"
    assert classify_bmi(37) == "Obesity Class II"
    assert classify_bmi(42) == "Obesity Class III"

    # Edge cases
    assert classify_bmi(-5) == "Invalid BMI"  
    assert classify_bmi(0) == "Underweight"  
    assert classify_bmi(100) == "Obesity Class III"  
    assert classify_bmi(18.5) == "Normal weight"  
    assert classify_bmi(25.0) == "Overweight"  


if __name__ == "__main__":
    pytest.main()
