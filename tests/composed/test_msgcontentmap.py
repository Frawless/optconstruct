import pytest
from optconstruct.types.composed.msg_clients.msgcontentmap import MsgContentMap

test_data = [
    # Sample 1
    ({'msg-content-map': {
        '~': {'key1': 'val1'}
    }}, "--msg-content-map \"key1~val1\" "),
    # Sample 2
    ({'msg-content-map': {
        '=': {'key1': 'val1'}
    }}, "--msg-content-map \"key1=val1\" "),
    # Sample 3
    ({'msg-content-map': {
        '~': {'key1': 'val1'},
        '=': {'key2': 'val2'}
    }}, "--msg-content-map \"key1~val1\" --msg-content-map \"key2=val2\" "),
    # Sample 4
    ({'msg-content-map': {
        '~': {'key1': 'val1'},
        '=': {'key2': 'val2'},
        'key3': 'val3'
    }}, "--msg-content-map \"key1~val1\" --msg-content-map \"key2=val2\" --msg-content-map \"key3=val3\" "),
    # Sample 5
    ({'msg-content-map': {
        'key1': 'val1'
    }}, "--msg-content-map \"key1=val1\" "),
    # Sample 6
    ({'msg-content-map': {
        'key1': 1
    }}, "--msg-content-map \"key1~1\" "),
]


@pytest.mark.parametrize("data, expected", test_data)
def test_msg_property(data, expected):
    obj = MsgContentMap('msg-content-map', '--msg-content-map')

    assert obj.generate_options(data) == expected


def test_fail_msg_property_empty():
    obj = MsgContentMap('msg-content-map', '--msg-content-map')

    assert obj.generate_options({'msg-content-map': {}}) == ''


def test_fail_msg_property_none():
    obj = MsgContentMap('msg-content-map', '--msg-content-map')

    assert obj.generate_options({}) == ''
