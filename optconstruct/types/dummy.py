from optconstruct import BasicOptionAbstract


class Dummy(BasicOptionAbstract):
    """

    """

    def generate_options(self, data, client=None):
        """
        Generate dummy options only with value without prefix.

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
        return self.key
