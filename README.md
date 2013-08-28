RabbitMQ Munin Plugin
=====================

A simple plugin for munin to monitor the number of messages in a queue.

By default monitors the celery queue for the user 'guest'

Installation
------------

The easiest way to install the code is to use [pip](http://www.pip-installer.org/).

Install the newest version from [PyPI](http://pypi.python.org/pypi/rabbitmq-munin):

        pip install rabbitmq-munin

Install the latest development version:

        pip install git+https://github.com/freyes/rabbitmq_munin.git#egg=rabbitmq-munin

The other option is to download and uncompress the code manually and execute the
included _setup.py_ script for installation:

        ./setup.py install

To make the plugin available to the munin-node you can run the following commands:

    cat > /etc/munin/plugins/rabbitmq_munin <<EOF
    #!/bin/bash
    rabbitmq_munin "$@"
    EOF
    chmod +x /etc/munin/plugins/rabbitmq_munin

Once munin can run the plugin, you can configure it as any other munin plugin 
(in /etc/munin/plugin-conf.d/munin-node) and the config will look like this:

    [rabbitmq_munin]
    env.username guest
    env.password guest
    env.server localhost:15672
    env.vhost /
    env.queue celery

The config above is using the default values of the plugin, your environment may require different values.

Dependencies
------------

Python packages:

* [pyrabbit](https://pypi.python.org/pypi/pyrabbit)

Rabbitmq plugins:

* [Management Plugin](http://www.rabbitmq.com/management.html), you can install it with the following command:

    rabbitmq-plugins enable rabbitmq_management
