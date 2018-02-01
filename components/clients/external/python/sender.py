from autologging import logged, traced

from optconstruct.types.composed import BrokerURLPythonProton
from optconstruct.types.prefixed import Prefixed
from optconstruct.types import Toggle

import amom.client
from .client import Client
from components.nodes.node import Node


@logged
@traced
class Sender(Client, amom.client.Sender):
    """
    External Python-Proton sender client
    """
    # client is installed from cli-rhea, node_app is there only for backward compability
    cli_command = ['cli-proton-python-sender']
    # Client-sender params for build execute command
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
        Prefixed('conn_ssl_certificate', '--conn-ssl-certificate'),
        Prefixed('conn_ssl_private_key', '--conn-ssl-private-key'),
        Prefixed('conn_ssl_password', '--conn-ssl-password'),
        Prefixed('conn_ssl_trust_store', '--conn-ssl-trust-store'),
        Toggle('conn_ssl_verify_peer', '--conn-ssl-verify-peer'),
        Toggle('conn_ssl_verify_peer_name', '--conn-ssl-verify-peer-name'),
        Prefixed('conn_handler', '--conn-handler'),
        Prefixed('conn_max_frame_size', '--conn-max-frame-size'),

        # Link options
        Toggle('link_durable', '--link-durable'),
        Toggle('link_at_least_once', '--link-at-least-once'),
        Toggle('link_at_most_once', '--link-at-most-once'),

        # Message options
        Prefixed('msg_id', '--msg-id'),
        Prefixed('msg_subject', '--msg-subject'),
        Prefixed('msg_reply_to', '--msg-reply-to'),
        Prefixed('msg_durable', '--msg-durable'),
        Prefixed('msg_ttl', '--msg-ttl'),
        Prefixed('msg_priority', '--msg-priority'),
        Prefixed('msg_correlation_id', '--msg-correlation-id'),
        Prefixed('msg_user_id', '--msg-user-id'),
        Prefixed('msg_group-id', '--msg-group-id'),
        Prefixed('msg_property', '--msg-property'),
        Prefixed('msg_content_map_item', '--msg-content-map-item'),
        Prefixed('msg_content_list_item', '--msg-content-list-item'),
        Prefixed('msg_content_from_file', '--msg-content-from-file'),
        Prefixed('msg_content', '--msg-content'),
        Prefixed('msg_content_type', '--msg-content-type'),
        Prefixed('content_type', '--content-type'),

        # Reactor options
        Toggle('reactor_peer_close_is_error', '--reactor-peer-close-is-error'),
        Toggle('reactor_auto_settle_off', '--reactor-auto-settle-off'),

    ]


    def __init__(self, node: Node):
        """
        Methd for init Python sender.
        """
        amom.client.Sender.__init__(self)
        Client.__init__(self, node)

    def _send_message(self, **kwargs):
        """
        Method for send message.
        :return:
        """
        self._set_attr_values(kwargs)
        cmd = self._build_sender_command()
        self._execute(cmd)
