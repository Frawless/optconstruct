from autologging import logged, traced

from optconstruct.types.composed import BrokerURLPythonProton
from optconstruct.types.prefixed import Prefixed
from optconstruct.types import Toggle

import amom.client
from .client import Client


@logged
@traced
class Connector(Client, amom.client.Connector):
    """
    External Python-Proton connector client
    """
    # client is installed from cli-rhea, node_app is there only for backward compatibility
    cli_command = ['cli-proton-python-connector']

    cli_params_transformation = [
        Toggle('help', '--help'),
        # Control options
        BrokerURLPythonProton('broker_url', '--broker-url'),
        Prefixed('count', '--count'),
        Prefixed('timeout', '--timeout'),
        Prefixed('close_sleep', '--close-sleep'),
        Prefixed('sync_mode', '--sync-mode'),

        # Logging options
        Prefixed('log-lib', '--log-lib'),
        Prefixed('log-stats', '--log-stats'),

        # Connection options
        Prefixed('conn_urls', '--conn-urls'),
        Prefixed('conn_reconnect', '--conn-reconnect'),
        Prefixed('conn_reconnect_interval', '--conn-reconnect-interval'),
        Prefixed('conn_reconnect_limit', '--conn-reconnect-limit'),
        Prefixed('conn_reconnect_timeout', '--conn-reconnect-timeout'),
        Prefixed('conn_heartbeat', '--conn-heartbeat'),
        Prefixed('conn_ssl_certificate', '--conn-ssl-certificate'),
        Prefixed('conn_ssl_password', '--conn-ssl-password'),
        Prefixed('conn_ssl_trust_store', '--conn-ssl-trust-store'),
        Toggle('conn_ssl_verify_peer', '--conn-ssl-verify-peer'),
        Toggle('conn_ssl_verify_peer_name', '--conn-ssl-verify-peer-name'),
        Prefixed('conn_handler', '--conn-handler'),
        Prefixed('conn_max_frame_size', '--conn-max-frame-size'),

        # Connector options
        Prefixed('obj-ctrl', '--obj-ctrl'),

    ]

    def __init__(self):
        """
        Method for init receiver.
        """
        amom.client.Connector.__init__(self)
        Client.__init__(self)
