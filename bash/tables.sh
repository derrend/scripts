#!/bin/bash -x

IPT=$(which iptables)

TCPLIST=/tmp/TCPLIST
UDPLIST=/tmp/UDPLIST

# Capture listening ports
ss -lnt | awk '{print $4;}' | rev | cut -f 1 -d : | rev | sort | uniq | head -n -1 > $TCPLIST
ss -lnu | awk '{print $4;}' | rev | cut -f 1 -d : | rev | sort | uniq | head -n -1 > $UDPLIST

# Functions dynamically allow access on listening ports
function tcplist {
    if [ $# -ne 0 ]; then
        for i in $@; do
            $IPT -A INPUT -p tcp --dport $i -j ACCEPT
        done
    fi
}

function udplist {
    if [ $# -ne 0 ]; then
        for i in $@; do
            $IPT -A INPUT -p udp --dport $i -j ACCEPT
        done
    fi
}

# Set initial conditions
$IPT -F
$IPT -t nat -F

$IPT -P INPUT DROP
$IPT -P FORWARD DROP
$IPT -P OUTPUT ACCEPT

# Define primary parameters
tcplist $(cat $TCPLIST)
udplist $(cat $UDPLIST)

# Define secondary parameters
$IPT -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Host as router
#$IPT -t nat -A POSTROUTING -o eth0 -j MASQUERADE
#$IPT -A FORWARD -i eth0 -o eth1 -m state --state RELATED,ESTABLISHED -j ACCEPT
#$IPT -A FORWARD -i eth1 -o eth0 -j ACCEPT

# Save configuration
#service iptables save
