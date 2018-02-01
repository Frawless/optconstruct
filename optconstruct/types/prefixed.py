from optconstruct import BasicOptionAbstract


class Prefixed(BasicOptionAbstract):
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
        option = "%s %s" % (self.prefix, data.get(self.key))
        return option
