import pytest
from optconstruct.types.toggle import Toggle
from optconstruct.types.dummy import Dummy
from optconstruct.types.prefixed import Prefixed
from optconstruct.basicoptionabstract import BasicOptionAbstract


@pytest.mark.parametrize("data, expected", [
    ({'help': True}, True),
    ({}, False),
])
def test_satisfied(data, expected):
    obj = BasicOptionAbstract('help', '--help')

    assert obj.satisfied(data) is expected


@pytest.mark.parametrize("test_input, expected", [
    ("help", "--help"),
    ("link_durable", "--link-durable"),
])
def test_toggle(test_input, expected):
    obj = Toggle(test_input, expected)

    data = {test_input: True}

    assert obj.generate_options(data) == expected


@pytest.mark.parametrize("test_input,expected", [
    ("dynamic", "--dynamic"),
    ("help", "--help"),
])
def test_dummy(test_input, expected):
    obj = Dummy(test_input, expected)

    data = {test_input: True}

    assert obj.generate_options(data) == test_input


@pytest.mark.parametrize("test_input, prefix, expected", [
    ("duration", "--duration", "--duration 5"),
    ("count", "--count", "--count 5"),
    ("timeout", "--timeout", "--timeout 5"),
])
def test_prefixed(test_input, prefix, expected):
    obj = Prefixed(test_input, prefix)

    data = {test_input: 5}

    assert obj.generate_options(data) == expected
