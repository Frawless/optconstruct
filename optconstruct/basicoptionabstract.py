
class BasicOptionAbstract:
    """

    """

    def __init__(self, key: str, prefix: str):
        """
        Init.
        :param key: key value of attribute in data set
        :param prefix: option prefix
        """
        self.key = key
        self.prefix = prefix

    def satisfied(self, data: dict):
        """

        :param data:
        :return:
        """
        return bool(data.get(self.key, None))
