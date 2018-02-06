import pytest
from optconstruct.types.composed.msg_clients.brokerurl import BrokerURLnodeJS
from optconstruct.types.composed.msg_clients.brokerurl import BrokerURLPythonProton


@pytest.mark.parametrize("data, expected", [
    # Sample 1
    ({
        'host': '10.0.0.1',
        'port': '5672',
        'address': 'testQueue',
    }, '--broker-url 10.0.0.1:5672/testQueue'),
    # Sample 2
    ({
        'host': '10.0.0.1',
        'port': '5672',
        'address': 'testQueue',
        'user': 'user',
        'password': 'password',
    }, '--broker-url user:password@10.0.0.1:5672/testQueue'),
    # Sample 3
    ({
        'broker-url': '10.0.0.1/5672'
    }, '--broker-url 10.0.0.1/5672')
])
def test_proton_python(data, expected):
    obj = BrokerURLPythonProton('broker-url', '--broker-url')

    assert obj.generate_options(data) == expected


@pytest.mark.parametrize("data, expected", [
    # Sample 1
    ({
        'host': '10.0.0.1',
        'port': '5672',
        'address': 'testQueue',
    }, '--broker 10.0.0.1:5672'),
    # Sample 2
    ({
         'host': '10.0.0.1',
         'port': '5672',
         'address': 'testQueue',
         'user': 'user',
         'password': 'password',
     }, '--broker user:password@10.0.0.1:5672'),
    # Sample 3
    ({
         'broker-url': '10.0.0.1/5672'
     }, '--broker 10.0.0.1/5672')
])
def test_nodejs(data, expected):
    obj = BrokerURLnodeJS('broker-url', '--broker')

    assert obj.generate_options(data) == expected

