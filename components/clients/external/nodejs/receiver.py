from autologging import logged, traced

from optconstruct.types.composed import BrokerURLnodeJS
from optconstruct.types.prefixed import Prefixed
from optconstruct.types import Toggle

import amom.client
from components.nodes.node import Node
from .client import Client


@logged
@traced
class Receiver(Client, amom.client.Receiver):
    """
    External NodeJS receiver client
    """
    # client is installed from cli-rhea, node_app is there only for backward compatibility
    cli_command = ['cli-rhea-receiver']

    # Client-sender params for build execute command
    cli_params_transformation = [
        Toggle('help', '--help'),
        # Control options
        Prefixed('recv_msg_selector', '--recv-selector'),
        Toggle('recv_browse', '--recv-browse'),
        Prefixed('action', '--action'),
        Prefixed('capacity', '--capacity'),
        Toggle('process_reply_to', '--process-reply-to'),
        Prefixed('recv_listen', '--recv-listen'),
        Prefixed('recv_listen_port', '--recv-listen-port'),
        Prefixed('duration', '--duration'),

        BrokerURLnodeJS('broker_url', '--broker'),
        Prefixed('address', '--address'),
        Prefixed('count', '--count'),
        Prefixed('close_sleep', '--close-sleep'),
        Prefixed('timeout', '--timeout'),

        # Logging options
        Prefixed('log_msgs', '--log-msgs'),
        Prefixed('log_lib', '--log-lib'),
        Prefixed('log_stats', '--log-stats'),

        # Link options
        Toggle('link_at_most_once', '--link-at-most-once'),
        Toggle('link_at_least_once', '--link-at-least-once'),
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
        Prefixed('conn_ssl_password', '--conn-ssl-password'),
        Prefixed('conn_ssl_trust_store', '--conn-ssl-trust-store'),
        Prefixed('conn_ssl_verify_peer', '--conn-ssl-verify-peer'),
        Prefixed('conn_ssl_verify-peer-name', '--conn-ssl-verify-peer-name'),
        Prefixed('conn_max_frame_size', '--conn-max-frame-size'),
        Prefixed('conn_web_socket', '--conn-web-socket'),

    ]

    def __init__(self, node: Node):
        """
        Method for init receiver.
        """
        amom.client.Receiver.__init__(self)
        Client.__init__(self, node)
