from optconstruct import BasicOptionAbstract


class Prefixed(BasicOptionAbstract):
    """
    Prefixed client options parser.
    """

    def generate_options(self, data, client=None):
        """
        Generate options with prefix and value.

        Parameters
        ----------
        :param data: data with specified option's values
        :type data: dict
        :param client: client's label
        :type client: str
        :return: option
        :rtype: str
        """
        _ = client
        _ = data
        option = "%s %s" % (self.prefix, data.get(self.key))
        return option
