"""
    # TODO jstejska: Package description
"""


class Protocol(object):
    """# TODO jstejska: class descritpion
    """

    def __init__(self, default_port=None):
        self.name = type(self).__name__
        self.default_port = default_port
