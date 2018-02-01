from autologging import logged, traced

from optconstruct.types.composed import BrokerURLnodeJS
from optconstruct.types.prefixed import Prefixed
from optconstruct.types import Toggle

import amom.client
from .client import Client


@logged
@traced
class Connector(Client, amom.client.Connector):
    """
    External NodeJS connector client
    """
    # client is installed from cli-rhea, node_app is there only for backward compatibility
    cli_command = ['cli-rhea-connector']

    cli_params_transformation = [
        Toggle('help', '--help'),
        Prefixed('obj-ctrl', '--obj-ctrl'),
        # Control options
        BrokerURLnodeJS('broker_url', '--broker'),
        Prefixed('address', '--address'),
        Prefixed('count', '--count'),
        Prefixed('close_sleep', '--close-sleep'),
        Prefixed('timeout', '--timeout'),

        # Logging options
        Prefixed('log-lib', '--log-lib'),
        Prefixed('log-stats', '--log-stats'),
        Toggle('link_durable', '--link-durable'),

        # Connection options
        Prefixed('conn_urls', '--conn-urls'),
        Prefixed('conn_reconnect', '--conn-reconnect'),
        Prefixed('conn_reconnect_interval', '--conn-reconnect-interval'),
        Prefixed('conn_reconnect_limit', '--conn-reconnect-limit'),
        Prefixed('conn_reconnect_timeout', '--conn-reconnect-timeout'),
        Prefixed('conn_heartbeat', '--conn-heartbeat'),
        Prefixed('conn_ssl', '--conn-ssl'),
        Prefixed('conn_ssl_certificate', '--conn-ssl-certificate'),
        Prefixed('conn_ssl_private_key', '--conn-ssl-private-key'),
        Prefixed('conn_ssl_password', '--conn-ssl-password'),
        Prefixed('conn_ssl_trust_store', '--conn-ssl-trust-store'),
        Toggle('conn_ssl_verify_peer', '--conn-ssl-verify-peer'),
        Toggle('conn_ssl_verify_peer_name', '--conn-ssl-verify-peer-name'),
        Prefixed('conn_max_frame_size', '--conn-max-frame-size'),
        Prefixed('conn_web_socket', '--conn-web-socket'),

    ]

    def __init__(self):
        """
        Method for init receiver.
        """
        amom.client.Connector.__init__(self)
        Client.__init__(self)
