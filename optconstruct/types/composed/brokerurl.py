import copy
import reformat
from optconstruct.types import BasicComposed


class BrokerURLnodeJS(BasicComposed):
    """
    BrokerURL option parser for nodeJS messaging client.
    """

    composed_keys = {'host'}

    def generate(self, data, client=None):
        """
        Generate option brokerURL option.

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

        broker_url = data.get('broker-url', None)

        if broker_url is not None:
            broker_url = self.prefix + " " + broker_url
            return broker_url

        credentials = reformat.reformat("%{user|%s}%{password|:%s}", data)

        if credentials:
            tmp_data = copy.deepcopy(data)
            tmp_data['credentials'] = credentials
        else:
            tmp_data = data

        broker_url = self.prefix + " " + reformat.reformat("%{credentials|%s@}%{host}%{port|:%s}", tmp_data)

        return broker_url


class BrokerURLPythonProton(BasicComposed):
    """
    BrokerURL option parser for Proton-Python messaging client.
    """

    def generate(self, data, client=None):
        """
        Generate option brokerURL option.

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

        broker_url = data.get('broker-url', None)

        if broker_url is not None:
            print(broker_url)
            broker_url = self.prefix + " " + broker_url
            return broker_url

        credentials = reformat.reformat("%{user|%s}%{password|:%s}", data)

        if credentials:
            tmp_data = copy.deepcopy(data)
            tmp_data['credentials'] = credentials
        else:
            tmp_data = data

        broker_url = self.prefix + " " + reformat.reformat("%{credentials|%s@}%{host}%{port|:%s}%{address|/%s}", tmp_data)

        return broker_url
