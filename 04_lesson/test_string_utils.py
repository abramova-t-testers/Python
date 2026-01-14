import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("солнце", "Солнце")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("-test", "-test")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("  Hello world", "Hello world"),
    (" 123", "123")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("\tskypro", "\tskypro"),
    ("skypro", "skypro")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol", [
    ("skypro", "s"),
    ("Hello world", "w"),
    ("123", "3")
])
def test_contains_positive(string, symbol):
    assert string_utils.contains(string, symbol) is True


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol", [
    ("skypro", "h"),
    ("Hello world", "я"),
    ("123", "589"),
    ([], [])
])
def test_contains_negative(string, symbol):
    assert string_utils.contains(string, symbol) is False


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("skypro", "s", "kypro"),
    ("Hello world", "world", "Hello "),
    ("123", "2", "13")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("", "h", ""),
    ("Hello world", "y", "Hello world"),
    ("123", "589", "123")
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected
