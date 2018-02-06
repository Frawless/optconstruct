import pytest

from optconstruct.types.composed import BasicComposed


@pytest.mark.parametrize("data, expected", [
    ({'msg-property': ''}, True),
    ({}, False),
])
def test_satisfied(data, expected):
    obj = BasicComposed('msg-property', '--msg-property')

    assert obj.satisfied(data) is expected
