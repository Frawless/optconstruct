"""
    # TODO jstejska: Package description
"""

# coding=utf-8
from autologging import logged, traced
from .nodes.node import Node
from .nodes.executions.ansible import AnsibleCMD


@logged
@traced
class IQAInstance:
    """IQA helper class

    Store variables, nodes and related things
    """
    def __init__(self, inventory=''):
        self.inventory = inventory
        self.nodes = []
        self.components = []
        self.ansible = AnsibleCMD(inventory)

    def new_node(self, hostname, ip=None):
        """Create new node under iQA instance

        @TODO dlenoch Pass inventory by true way for Ansible
        # TODO jstejska: Description

        :param hostname:
        :type hostname:
        :param ip:
        :type ip:

        :return:
        :rtype:
        """
        node = Node(hostname=hostname, ip=ip, ansible=self.ansible)
        self.nodes.append(node)
        return node

    def new_component(self, node: Node, component, *args):
        """Create new node under iQA instance

        @TODO Pass inventory by true way for Ansible
        # TODO jstejska: Description

        :param node:
        :type node:
        :param component:
        :type component:

        :return:
        :rtype:
        """
        component = component(node=node, *args)
        self.components.append(node)
        return component
