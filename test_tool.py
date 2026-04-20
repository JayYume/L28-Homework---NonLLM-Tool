# test_tool.py
import pytest
from tool import calculate_password_entropy

def test_happy_path():
    result = calculate_password_entropy("P@ssw0rd123!")
    assert result["result"] > 40
    assert result["unit"] == "bits"
    assert "strength" in result["detail"]

def test_edge_case():
    result = calculate_password_entropy("a")
    assert result["result"] == 4.7  # log2(26) rounded
    assert "Very Weak" in result["detail"]

def test_invalid_input_raises():
    with pytest.raises(ValueError):
        calculate_password_entropy("")
    
    with pytest.raises(ValueError):
        calculate_password_entropy(12345)