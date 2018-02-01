from optconstruct import BasicOptionAbstract


class BasicComposed(BasicOptionAbstract):
    """
    Toggle client options parser.
    """

    composed_keys = {'host'}

    def satisfied(self, data: dict):
        """

        :param data:
        :return:
        """
        self.composed_keys.add(self.key)

        return bool(set(data.keys()).intersection(self.composed_keys))

