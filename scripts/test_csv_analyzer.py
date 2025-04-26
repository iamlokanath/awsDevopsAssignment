#!/usr/bin/env python3
"""
Test file for csv_analyzer.py
"""

import os
import sys

# Add the parent directory to sys.path so we can import the module
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from csv_analyzer import process_row, is_numeric  # pylint: disable=C0413

def test_is_numeric():
    """Test the is_numeric function"""
    assert is_numeric("123") is True
    assert is_numeric("123.45") is True
    assert is_numeric("-123.45") is True
    assert is_numeric("abc") is False
    assert is_numeric("") is False

def test_process_row():
    """Test the process_row function"""
    # Test valid row
    row = ["John Smith", "18", "85.5"]
    result = process_row(row)
    assert result["name"] == "John Smith"
    assert result["age"] == 18
    assert result["grade"] == 85.5
    
    # Test row with spaces
    row = [" Emily Johnson ", " 17 ", " 92.0 "]
    result = process_row(row)
    assert result["name"] == "Emily Johnson"
    assert result["age"] == 17
    assert result["grade"] == 92.0

def test_process_row_with_invalid_data():
    """Test process_row with invalid data"""
    # Test row with invalid age
    row = ["Jane Doe", "invalid", "75.0"]
    result = process_row(row)
    assert result["name"] == "Jane Doe"
    assert result["age"] == 0  # Should default to 0
    assert result["grade"] == 75.0
    
    # Test row with invalid grade
    row = ["Bob Smith", "20", "invalid"]
    result = process_row(row)
    assert result["name"] == "Bob Smith"
    assert result["age"] == 20
    assert result["grade"] == 0.0  # Should default to 0.0   
