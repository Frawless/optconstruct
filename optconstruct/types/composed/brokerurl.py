import copy
import reformat
from optconstruct.types import BasicComposed


class BrokerURLnodeJS(BasicComposed):
    """

    """

    def generate_options(self, data, client=None):
        """

        :param data:
        :param client:
        :return:
        """
        _ = client

        broker_url = data.get('broker_url', None)

        if broker_url is not None:
            broker_url = self.prefix + " " + broker_url
            return broker_url

        credentials = reformat.reformat("%{user|%s}%{password|:%s}", data)

        if credentials:
            tmp_data = copy.deepcopy(data)
            tmp_data['credentials'] = credentials
        else:
            tmp_data = data

        broker_url = reformat.reformat("%{credentials|%s@}%{host}%{port|:%s}", tmp_data)

        return broker_url


class BrokerURLPythonProton(BasicComposed):
    """

    """

    def generate_options(self, data, client=None):
        """

        :param data:
        :param client:
        :return:
        """
        _ = client

        broker_url = data.get('broker_url', None)

        if broker_url is not None:
            broker_url = self.prefix + " " + broker_url
            return broker_url

        credentials = reformat.reformat("%{user|%s}%{password|:%s}", data)

        if credentials:
            tmp_data = copy.deepcopy(data)
            tmp_data['credentials'] = credentials
        else:
            tmp_data = data

        broker_url = reformat.reformat("%{credentials|%s@}%{host}%{port|:%s}%{address|/%s}", tmp_data)

        return broker_url
