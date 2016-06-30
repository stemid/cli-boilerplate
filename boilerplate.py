#!/usr/bin/env python
# coding: utf-8
#
# Boilerplate code to create CLI utilities

from __future__ import print_function

try:
    from configparser import RawConfigParser
except ImportError:
    from ConfigParser import ConfigParser
from argparse import ArgumentParser, FileType
from pprint import pprint
from sys import exit, stderr

config = ConfigParser()
config.readfp(open('boilerplate_defaults.cfg'))
config.read(['/etc/boilerplate.cfg', './boilerplate_local.cfg'])

parser = ArgumentParser(
    description='Boilerplate code',
    epilog='Example: ./boilerplate.py'
)

parser.add_argument(
    '-v', '--verbose',
    action='count',
    default=False,
    dest='verbose',
    help='Verbose output, use more v\'s to increase level'
)

# If you want to supply an optional configuration file
#parser.add_argument(
#    '-c', '--configuration',
#    type=FileType('r'),
#    help='Configuration with siptrack connection credentials'
#)

def main():
    print('Boilerplate')

if __name__ == '__main__':
    main()
