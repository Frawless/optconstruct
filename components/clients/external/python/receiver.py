from autologging import logged, traced

from optconstruct.types.composed import BrokerURLPythonProton
from optconstruct.types.prefixed import Prefixed
from optconstruct.types import Toggle

import amom.client
from .client import Client
from components.nodes.node import Node

@logged
@traced
class Receiver(Client, amom.client.Receiver):
    """
    External Python-Proton receiver client
    """
    # client is installed from cli-rhea
    cli_command = ['cli-proton-python-receiver']

    cli_params_transformation = [
        Toggle('help', '--help'),
        # Control options
        BrokerURLPythonProton('broker_url', '--broker-url'),
        Prefixed('count', '--count'),
        Prefixed('timeout', '--timeout'),
        Prefixed('close_sleep', '--close-sleep'),
        Prefixed('sync_mode', '--sync-mode'),
        Prefixed('duration', '--duration'),
        Prefixed('duration_mode', '--duration-mode'),
        Prefixed('capacity', '--capacity'),
        Toggle('dynamic', '--dynamic'),

        # Logging options
        Prefixed('log_lib', '--log-lib'),
        Prefixed('log_stats', '--log-stats'),
        Prefixed('log_msgs', '--log-msgs'),

        # Transaction options
        Prefixed('tx_size', '--tx-size'),
        Prefixed('tx_action', '--tx-action'),
        Prefixed('tx_endloop_action', '--tx-endloop-action'),

        # Connection options
        Prefixed('conn_urls', '--conn-urls'),
        Prefixed('conn_reconnect', '--conn-reconnect'),
        Prefixed('conn_reconnect_interval', '--conn-reconnect-interval'),
        Prefixed('conn_reconnect_limit', '--conn-reconnect-limit'),
        Prefixed('conn_reconnect_timeout', '--conn-reconnect-timeout'),
        Prefixed('conn_heartbeat', '--conn-heartbeat'),
        Prefixed('conn_ssl_domain_certificate', '--conn-ssl-certificate'),
        Prefixed('conn_ssl_domain_private_key', '--conn-ssl-private-key'),
        Prefixed('conn_ssl_domain_password', '--conn-ssl-password'),
        Prefixed('conn_ssl_domain_trust_store', '--conn-ssl-trust-store'),
        Prefixed('conn_ssl_domain_verify_peer', '--conn-ssl-verify-peer'),
        Prefixed('conn_ssl_domain_verify_peer_name', '--conn-ssl-verify-peer-name'),
        Prefixed('conn_handler', '--conn-handler'),
        Prefixed('conn_max_frame_size', '--conn-max-frame-size'),

        # Link options
        Toggle('link_durable', '--link-durable'),
        Toggle('link_at_least_once', '--link-at-least-once'),
        Toggle('link_at_most_once', '--link-at-most-once'),
        Prefixed('link_dynamic_node_properties', '--link-dynamic-node-properties'),

        # Receiver options
        Prefixed('process_reply_to', '--process-reply-to'),
        Prefixed('action', '--action'),
        Prefixed('action_size', '--action-size'),
        Prefixed('recv_selector', '--recv-selector'),
        Toggle('recv_browse', '--recv-browse'),
        Toggle('recv_consume', '--recv-consume'),
        Prefixed('recv_filter', '--recv-filter'),
        Toggle('recv_listen', '--recv-listen'),

        # Reactor options
        Prefixed('reactor_prefetch', '--reactor-prefetch'),
        Toggle('reactor_auto_accept', '--reactor-auto-accept'),
        Toggle('reactor_peer_close_is_error', '--reactor-peer-close-is-error'),
        Toggle('reactor_auto_settle_off', '--reactor-auto-settle-off'),

    ]

    def __init__(self, node: Node):
        """
        Method for init receiver.
        """
        amom.client.Receiver.__init__(self)
        Client.__init__(self, node)
