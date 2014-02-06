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
    know = {}
    while True:
        try:
            dev,ts,packet = net.recv_packet(timeout=1.0)
        except SrpyNoPackets:
            # timeout waiting for packet arrival
            
            continue
        except SrpyShutdown:
            # we're done; bail out of while loop
            break 
        myint_names = [intf.name for intf in  net.interfaces()]#names of my interfaces(aka ports)
        myint_addr = [intf.ethaddr for intf in  net.interfaces()]#names of my interfaces(ethernet adresses)
        dest = packet.dst
        src = packet.src
        know [src] = dev #JUST LEARNED SOMETHING 
        if dest in myint_addr:
            #then the packet was for us so we drop it like its ...hot
            continue 
        else:#check if its broadcast or don't know where to send it
            if dest == ETHER_BROADCAST or not(dest in know):
                [net.send_packet(name,packet) for name in myint_names if name!= dev]
            else: #not broadcast and know where to send it 
                net.send_packet(know[dest],packet)

                



    # before exiting our main function,
    # perform shutdown on network
    net.shutdown()
