import pytest
from optconstruct.types.composed.msg_clients.msgproperty import MsgProperty

test_data = [
    # Sample 1
    ({'msg-property': {
        '~': {'key1': 'val1'}
    }}, "--msg-property \"key1~val1\" "),
    # Sample 2
    ({'msg-property': {
        '=': {'key1': 'val1'}
    }}, "--msg-property \"key1=val1\" "),
    # Sample 3
    ({'msg-property': {
        '~': {'key1': 'val1'},
        '=': {'key2': 'val2'}
    }}, "--msg-property \"key1~val1\" --msg-property \"key2=val2\" "),
    # Sample 4
    ({'msg-property': {
        '~': {'key1': 'val1'},
        '=': {'key2': 'val2'},
        'key3': 'val3'
    }}, "--msg-property \"key1~val1\" --msg-property \"key2=val2\" --msg-property \"key3=val3\" "),
    # Sample 5
    ({'msg-property': {
        'key1': 'val1'
    }}, "--msg-property \"key1=val1\" "),
    # Sample 6
    ({'msg-property': {
        'key1': 1
    }}, "--msg-property \"key1~1\" "),
]


@pytest.mark.parametrize("data, expected", test_data)
def test_msg_property(data, expected):
    obj = MsgProperty('msg-property', '--msg-property')

    assert obj.generate_options(data) == expected


def test_fail_msg_property_empty():
    obj = MsgProperty('msg-property', '--msg-property')

    assert obj.generate_options({'msg-property': {}}) == ''


def test_fail_msg_property_none():
    obj = MsgProperty('msg-property', '--msg-property')

    assert obj.generate_options({}) == ''
