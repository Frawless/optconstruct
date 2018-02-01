from autologging import logged, traced

from optconstruct.types.composed import BrokerURLnodeJS
from optconstruct.types.prefixed import Prefixed
from optconstruct.types import Toggle

import amom.client
from components.nodes.node import Node
from .client import Client


@logged
@traced
class Sender(Client, amom.client.Sender):
    """
    External NodeJS sender client
    """
    # client is installed from cli-rhea, node_app is there only for backward compatibility
    cli_command = ['cli-rhea-sender']

    # Client-receiver params for build execute command
    cli_params_transformation = [
        Toggle('help', '--help'),

        # Message options
        Prefixed('msg_id', '--msg-id'),
        Prefixed('msg_subject', '--msg-subject'),
        Prefixed('msg_reply_to', '--msg-reply-to'),
        Prefixed('msg_reply_to_group_id', '--msg-reply-to-group-id'),
        Prefixed('msg_durable', '--msg-durable'),
        Prefixed('msg_ttl', '--msg-ttl'),
        Prefixed('msg_priority', '--msg-priority'),
        Prefixed('msg_correlation_id', '--msg-correlation-id'),
        Prefixed('msg_user_id', '--msg-user-id'),
        Prefixed('msg_group-id', '--msg-group-id'),
        Prefixed('msg_group-seq', '--msg-group-seq'),
        Prefixed('msg_property', '--msg-property'),
        Prefixed('property_type', '--property-type'),
        Prefixed('msg_content_map_item', '--msg-content-map-item'),
        Prefixed('msg_content_list_item', '--msg-content-list-item'),
        Prefixed('msg_content_from_file', '--msg-content-from-file'),
        Prefixed('msg_content', '--msg-content'),
        Prefixed('msg_anotation', '--msg-anotation'),
        Prefixed('msg_content_type', '--msg-content-type'),
        Prefixed('content_type', '--content-type'),

        # Control options
        Prefixed('capacity', '--capacity'),
        Prefixed('reactor_auto_settle_off', '--reactor-auto-settle-off'),
        Prefixed('anonymous', '--anonymous'),
        Prefixed('duration', '--duration'),
        Prefixed('log_msgs', '--log-msgs'),

        Toggle('link_at_most_once', '--link-at-most-once'),
        Toggle('link_at_least_once', '--link-at-least-once'),

        BrokerURLnodeJS('broker_url', '--broker'),
        Prefixed('address', '--address'),
        Prefixed('count', '--count'),
        Prefixed('close_sleep', '--close-sleep'),
        Prefixed('timeout', '--timeout'),
        Prefixed('log_lib', '--log-lib'),
        Prefixed('log_stats', '--log-stats'),
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
        Method for init NodeJS sender.
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
