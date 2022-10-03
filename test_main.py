"""Testing file."""
import pytest
from substring_in_string import fifth_task
from check_year import check_date


test_date = [(2000, 2, 29, True), (1900, 2, 29, False), (1900, 2, 28, True)]


@pytest.mark.parametrize('year, month, day, expect', test_date)
def test_data_checker(year, month, day, expect):
    """Test for it. Takes year, month, day and checks does the date exist.

    Args:
        year : int - some year.
        month : int - some month.
        day : int - some day.

    Return:
        expect : bool -  true if the date exist else false.
    """
    assert check_date(year, month, day) == expect


checker_for_strings = [('ABc dbE FRl Ama', 50.0), ('NDp Lka nuR vtE', 25.0), ('AbC AAA', 100.0)]


@pytest.mark.parametrize('string, expect', checker_for_strings)
def test_strings(string, expect):
    """Test for it. Takes string with capitals letter and small letters, counts substrings which are more.

    Args:
        string : str - string with substrings.

    Return:
        expect : float - percentage of substrings with more capitals letter.
    """
    assert fifth_task(string) == expect
