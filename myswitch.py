#!/usr/bin/env python

'''
Ethernet learning switch in Python.
'''

import sys
import os
import os.path
sys.path.append(os.path.join(os.environ['HOME'],'pox'))
sys.path.append(os.path.join(os.getcwd(),'pox'))
import pox.lib.packet as pkt
from pox.lib.packet.ethernet import ETHER_BROADCAST
from pox.lib.addresses import EthAddr
from srpy_common import log_info, log_debug, SrpyShutdown, SrpyNoPackets

def srpy_main(net):

    # any setup/initialization code

    while True:
        try:
            dev,ts,packet = net.recv_packet(timeout=1.0)
        except SrpyNoPackets:
            # timeout waiting for packet arrival
            continue
        except SrpyShutdown:
            # we're done; bail out of while loop
            return





    # before exiting our main function,
    # perform shutdown on network
    net.shutdown()
