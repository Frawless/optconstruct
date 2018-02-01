from components.clients.external import nodejs, python
from amom.node import Node

if __name__ == "__main__":

    node = Node('Test', '10.0.0.1')
    nodejsRcv = nodejs.Receiver(node)
    pythonRcv = python.Receiver(node)

    nodejsRcv.data = {
        'help': False,
        'dynamic': True,
        'link_durable': True,
        'capacity': 5,
        'address': 'test',
        'host': '0.0.0.0',
        'port': '5672',
        'user': 'pepa',
        'password': 'zdepa',
    }

    pythonRcv.data = {
        'count': 5,
        'address': 'test',
        'host': '0.0.0.0',
        'port': '5672',
    }

    print("NodeJS: " + nodejsRcv.build_command())

    print("Python: " + pythonRcv.build_command())

