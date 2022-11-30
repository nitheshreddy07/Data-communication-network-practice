#!/usr/bin/python

"""
linuxrouter.py: Example network with Linux IP router

This example converts a Node into a router using IP forwarding
already built into Linux.

The example topology creates a router and three IP subnets:

    - 192.168.1.0/24 (r0-eth1, IP: 192.168.1.1)
    - 172.16.0.0/12 (r0-eth2, IP: 172.16.0.1)
    - 10.0.0.0/8 (r0-eth3, IP: 10.0.0.1)

Each subnet consists of a single host connected to
a single switch:

    r0-eth1 - s1-eth1 - h1-eth0 (IP: 192.168.1.100)
    r0-eth2 - s2-eth1 - h2-eth0 (IP: 172.16.0.100)
    r0-eth3 - s3-eth1 - h3-eth0 (IP: 10.0.0.100)

The example relies on default routing entries that are
automatically created for each router interface, as well
as 'defaultRoute' parameters for the host interfaces.

Additional routes may be added to the router or hosts by
executing 'ip route' or 'route' commands on the router or hosts.
"""

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import Node
from mininet.log import setLogLevel, info
from mininet.cli import CLI

class LinuxRouter( Node ):
    "A Node with IP forwarding enabled."

    def config( self, **params ):
        super( LinuxRouter, self).config( **params )
        # Enable forwarding on the router
        self.cmd( 'sysctl net.ipv4.ip_forward=1' )

    def terminate( self ):
        self.cmd( 'sysctl net.ipv4.ip_forward=0' )
        super( LinuxRouter, self ).terminate()


class NetworkTopo( Topo ):
    "A LinuxRouter connecting three IP subnets"

    def build( self, **_opts ):

        defaultIP = '192.168.1.1/24'  # IP address for r0-eth1
        router = self.addNode( 'r0', cls=LinuxRouter, ip=defaultIP )

        s1, s2, s3, s4, s5, s6, s7 = [ self.addSwitch( s ) for s in 's1', 's2', 's3', 's4', 's5', 's6', 's7' ]

        self.addLink( s1, router, intfName2='r0-eth1',
                      params2={ 'ip' : defaultIP } )  # for clarity
        self.addLink( s2, router, intfName2='r0-eth2',
                      params2={ 'ip' : '192.168.1.64/26' } )
        self.addLink( s3, router, intfName2='r0-eth3',
                      params2={ 'ip' : '192.168.1.128/26' } )
        self.addLink( s4, router, intfName2='r0-eth4',
                      params2={ 'ip' : '192.168.1.80/28' } )  
        self.addLink( s5, router, intfName2='r0-eth5',
                      params2={ 'ip' : '192.168.1.96/28' } )
        self.addLink( s6, router, intfName2='r0-eth6',
                      params2={ 'ip' : '192.168.1.144/28' } )    
        self.addLink( s7, router, intfName2='r0-eth7',
                      params2={ 'ip' : '192.168.1.160/28' } )                                       

        h1 = self.addHost( 'h1', ip='192.168.1.81',
                           defaultRoute='via 192.168.1.80' )
        h2 = self.addHost( 'h2', ip='192.168.1.82',
                           defaultRoute='via 192.168.1.80' )
        h3 = self.addHost( 'h3', ip='192.168.1.97',
                           defaultRoute='via 192.168.1.96' )
        h4 = self.addHost( 'h4', ip='192.168.1.98',
                           defaultRoute='via 192.168.1.96' ) 
        h5 = self.addHost( 'h5', ip='192.168.1.145',
                           defaultRoute='via 192.168.1.144' ) 
        h6 = self.addHost( 'h6', ip='192.168.1.146',
                           defaultRoute='via 192.168.1.144' ) 
        h7 = self.addHost( 'h7', ip='192.168.1.161',
                           defaultRoute='via 192.168.1.160' ) 
        h8 = self.addHost( 'h8', ip='192.168.1.162',
                           defaultRoute='via 192.168.1.160' ) 
                                                      

        for h, s in [ (h1, s4), (h2, s4), (h3, s5), (h4, s5), (h5, s6), (h6, s6), (h7, s7), (h8, s7), (s4, s2), (s5, s2), (s2, s1), (s6, s3), (s7, s3), (s3, s1) ]:
            self.addLink( h, s )


def run():
    "Test linux router"
    topo = NetworkTopo()
    net = Mininet( topo=topo )  # controller is used by s1-s3
    net.start()
    info( '*** Routing Table on Router:\n' )
    print net[ 'r0' ].cmd( 'route' )
    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    run()
