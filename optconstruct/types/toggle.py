from optconstruct import BasicOptionAbstract


class Toggle(BasicOptionAbstract):
    """
    Toggle client options parser.
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
        return self.prefix

