from optconstruct.types import BasicComposed


class MsgContentMap(BasicComposed):
    """
    Basic MsgContentMap option parser for messaging clients.
    """

    def generate_options(self, data, client=None):
        """
        Generate option MsgContentMap option.

        Parameters
        ----------
        :param data: data with specified option's values
        :type data: dict
        :param client: client's label
        :type client: str
        :return: option
        :rtype: str
        """

        return self._msg_hash_parse(data, client)
