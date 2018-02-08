import pytest
from optconstruct.types.listoptions.msgcontentlist import MsgContentList

test_data = [
    # Sample 1
    ({'msg-content-list-item': ['val1', 10]}, "--msg-content-list-item \"val1\" --msg-content-list-item \"~10\" "),
    # Sample 2
    ({'msg-content-list-item': 'val1'}, "--msg-content-list-item \"val1\" "),
    # Sample 3
    ({'msg-content-list-item': 10}, "--msg-content-list-item \"~10\" "),
    # Sample 4
    ({'msg-content-list-item': (10, 5)}, "--msg-content-list-item \"~10\" --msg-content-list-item \"~5\" "),
    # Sample 5
    ({'msg-content-list-item': '~10'}, "--msg-content-list-item \"~10\" "),
]


@pytest.mark.parametrize("data, expected", test_data)
def test_msg_content_list(data, expected):
    obj = MsgContentList('msg-content-list-item', '--msg-content-list-item')
    assert obj.generate(data) == expected


def test_fail_msg_content_list_empty():
    obj = MsgContentList('msg-content-map', '--msg-content-list-item')
    assert obj.generate({'msg-content-list-item': {}}) == ''


def test_fail_msg_content_list_none():
    obj = MsgContentList('msg-content-list-item', '--msg-content-list-item')
    assert obj.generate({}) == ''
