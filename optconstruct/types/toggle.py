from optconstruct import BasicOptionAbstract


class Toggle(BasicOptionAbstract):
    """
    Toggle client options parser.
    """

    def generate_options(self, data, client=None):
        """
        Generate toggle options with prefix only.

        Parameters
        ----------
        :param data: data with specified option's values
        :type: dict
        :param client: client's label
        :type client: str
        :return: option
        :rtype: str
        """
        _ = client
        _ = data
        return self.prefix

