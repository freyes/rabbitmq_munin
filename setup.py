import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "rabbitmq-munin",
    version = "0.2",
    author = "Felipe Reyes",
    author_email = "freyes@tty.cl",
    description = "A munin plugin to monitor rabbitmq queues.",
    license = "BSD",
    keywords = "rabbitmq munin plugin",
    url = "https://github.com/freyes/rabbitmq_munin",
    py_modules=["rabbitmq_munin", ],
    install_requires=["pyrabbit", ],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Environment :: Plugins",
        "Intended Audience :: System Administrators",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.4",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: System :: Monitoring",
    ],
    entry_points="""
    [console_scripts]
    rabbitmq_munin = rabbitmq_munin:main
    """,
)
