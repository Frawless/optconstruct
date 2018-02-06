import copy

from optconstruct import BasicOptionAbstract


class BasicComposed(BasicOptionAbstract):
    """
    Composed options parser.
    """

    composed_keys = set()

    def satisfied(self, data: dict):
        """
        Check if client's option should be generated.

        Parameters
        ----------
        :param data: data with specified option's values
        :type data: dict
        :return: True or False
        :rtype bool
        """
        self.composed_keys.add(self.key)

        return bool(set(data.keys()).intersection(self.composed_keys))

    def _msg_hash_parse(self, data, client=None):
        """
        Dictionary transformation to consecutive parameters with prefix, separator and value.

        Parameters
        ----------
        :param data: data: data with specified option's values
        :type data: dict
        :param client: client's label
        :type client: str
        :return: options
        :rtype str
        """
        _ = client



        option = copy.deepcopy(data.get(self.key, None))

        if option is None:
            return ''

        output = ""

        for separator in ['~', '=']:
            item = option.get(separator, None)
            if item:
                del option[separator]
                for key, value in item.items():
                    output += "%s \"%s%s%s\" " % (self.prefix, key, separator, value)

        for key, value in option.items():
            separator = '='
            if not isinstance(value, str):
                separator = '~'
            output += "%s \"%s%s%s\" " % (self.prefix, key, separator, value)

        return output

    def _msg_value_retype(self, data, client=None):
        """
        List or tuple transformation to consecutive parameters with prefix, separator and value.

        Parameters
        ----------
        :param data: data: data with specified option's values
        :type data: dict
        :param client: client's label
        :type client: str
        :return: options
        :rtype str
        """
        _ = client

        option = data.get(self.key, None)

        if option is None:
            return ''

        output = ""
        separator = '~'

        if not isinstance(option, (list, tuple)):
            option = [option]

        for value in option:
            if isinstance(value, int):
                output += "%s \"%s%s\" " % (self.prefix, separator, value)
            else:
                output += "%s \"%s\" " % (self.prefix, value)

        return output
