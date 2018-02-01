from optconstruct import BasicOptionAbstract


class Dummy(BasicOptionAbstract):
    """

    """

    def generate_options(self, data, client=None):
        """
        Method for generate toggle options.
        :param data:
        :param client:
        :return:
        """
        _ = client
        _ = data
        return self.key
