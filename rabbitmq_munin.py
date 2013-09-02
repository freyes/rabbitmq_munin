import sys
import argparse
from os import environ
from pyrabbit.api import Client


TPL_STATS = """graph_title Rabbit stats
graph_category rabbitmq
graph_vlabel Queued Messages
messages.label queue size (depth)
message_stats_publish_rate.label published messages rate
total_channels.label channels
total_connections.label connections
total_consumers.label consumers
total_exchanges.label exchanges
total_queues.label queues
"""
TPL_PUBLISHED_MESSAGES = """graph_title RabbitMQ / Published Messages Volume
graph_category rabbitmq
graph_vlabel Published Messages
message_stats_publish.label published messages
message_stats_publish.draw AREA
"""


def config(options, template):
    print template


def connect(options):
    server = environ.get("server", "localhost:15672")
    client = Client(server,
                    environ.get("username", "guest"),
                    environ.get("password", "guest"))

    client.is_admin = True
    return client


def print_object_totals(options):
    client = connect(options)

    try:
        overview = client.get_overview()
        print "total_channels.value", overview["object_totals"]["channels"]
        print "total_connections.value", overview["object_totals"]["connections"]
        print "total_consumers.value", overview["object_totals"]["consumers"]
        print "total_exchanges.value", overview["object_totals"]["consumers"]
        print "total_queues.value", overview["object_totals"]["queues"]
    except:
        pass


def print_num_messages(options):
    """
    Print number of messages

    :param options: connection options and threshold params
    """
    client = connect(options)
    depth = client.get_queue_depth(environ.get("vhost", "/"),
                                   environ.get("queue", "celery"))
    print "messages.value", depth


def print_message_stats(options):
    client = connect(options)
    try:
        overview = client.get_overview()
        stats = overview["message_stats"]
    except:
        return
    try:
        print "message_stats_publish.value ",
        print  stats["publish"]
    except:
        print ""


def print_message_stats_rate(options):
    client = connect(options)
    try:
        overview = client.get_overview()
        stats = overview["message_stats"]
    except:
        return
    try:
        print "message_stats_publish_rate.value ",
        print stats["publish_details"]["rate"]
    except:
        print ""


def setup_options(argv=None):
    parser = argparse.ArgumentParser(description='Status of rabbmitmq queues.')
    parser.add_argument('config', nargs="?")
    args = parser.parse_args()

    return args


def main():
    options = setup_options()
    if options.config == "debug":
        import ipdb; ipdb.set_trace()
    if options.config == "config":
        config(options, TPL_STATS)
    else:
        try:
            print_num_messages(options)
        except Exception as ex:
            print ex
            print "messages.value"

        print_message_stats_rate(options)
        print_object_totals(options)


def main_published_messages():
    options = setup_options()
    if options.config == "config":
        config(options, TPL_PUBLISHED_MESSAGES)
    else:
        print_message_stats(options)
