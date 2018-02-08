import pytest

from optconstruct.types.argument import Argument
from optconstruct.types.toggle import Toggle
from optconstruct.types.dummy import Dummy
from optconstruct.types.prefixed import Prefixed
from optconstruct.optionabstract import OptionAbstract


def test_abstract_generate():
    obj = OptionAbstract('', '')
    with pytest.raises(NotImplementedError):
        obj.generate({'': ''})


@pytest.mark.parametrize("data, expected", [
    ({'help': True}, True),
    ({}, False),
])
def test_abstract_satisfied(data, expected):
    obj = OptionAbstract('help', '--help')
    assert obj.satisfied(data) is expected


@pytest.mark.parametrize("test_input, expected", [
    ("help", "--help"),
    ("link_durable", "--link-durable"),
])
def test_toggle(test_input, expected):
    obj = Toggle(test_input, expected)
    data = {test_input: True}
    assert obj.generate(data) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("dynamic", ""),
    ("help", ""),
])
def test_dummy(test_input, expected):
    obj = Dummy(test_input)
    data = {test_input: True}
    assert obj.generate(data) == expected


def test_dummy_satisfied():
    obj = Dummy("test")
    assert obj.satisfied() is False


@pytest.mark.parametrize("test_input, prefix, expected", [
    ("dynamic", "--dynamic", "False"),
    ("help", "--help", "True"),
])
def test_argument(test_input, prefix, expected):
    obj = Argument(test_input, prefix)
    data = {test_input: expected}
    assert obj.generate(data) == expected


@pytest.mark.parametrize("test_input, prefix, expected", [
    ("duration", "--duration", "--duration 5"),
    ("count", "--count", "--count 5"),
    ("timeout", "--timeout", "--timeout 5"),
])
def test_prefixed(test_input, prefix, expected):
    obj = Prefixed(test_input, prefix)
    data = {test_input: 5}
    assert obj.generate(data) == expected
