from components.clients.external import nodejs, python
from amom.node import Node

if __name__ == "__main__":
    node = Node('Test', '10.0.0.1')
    nodejsRcv = nodejs.Sender(node)
    pythonRcv = python.Receiver(node)

    nodejsRcv.data = {
        'help': False,
        'dynamic': True,
        'link-durable': True,
        'capacity': 5,
        'address': 'test',
        'host': '0.0.0.0',
        'port': '5672',
        'user': 'pepa',
        'password': None,
        'msg-content-list-item': ['val1', 10],
        'msg-property': {
            '~': {
                'key4': '1',
                'key3': '1',
                'key1': '1'
            },
            '=': {
                'key2': 2,
                'test': 4
            }
        },
        'broker-url': 'test'
    }

    pythonRcv.data = {
        'count': 5,
        'address': 'test',
        'host': '0.0.0.0',
        'port': '5672',
        'broker-url': 'test'
    }

    print("NodeJS: " + nodejsRcv.build_command())

    print("Python: " + pythonRcv.build_command())
