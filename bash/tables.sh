#!/bin/bash -x

IPT=$(which iptables)

# Capture listening ports
ss -lnt | awk '{print $4;}' | rev | cut -f 1 -d : | rev | sort | uniq | head -n -1 > /tmp/TCPLIST
ss -lnu | awk '{print $4;}' | rev | cut -f 1 -d : | rev | sort | uniq | head -n -1 > /tmp/UDPLIST

# Functions dynamically allow access on listening ports
function tcplist {
    if [ $# -eq 0 ]
    then
        :
    else
        for i in $@
        do
            $IPT -A INPUT -p tcp --dport $i -j ACCEPT
        done
    fi
}

function udplist {
    if [ $# -eq 0 ]
    then
        :
    else
        for i in $@
        do
            $IPT -A INPUT -p udp --dport $i -j ACCEPT
        done
    fi
}

# Define initial paramiters
$IPT -F

$IPT -P INPUT DROP
$IPT -P FORWARD DROP
$IPT -P OUTPUT ACCEPT

# Define dynamic parameters
tcplist $(cat /tmp/TCPLIST)
udplist $(cat /tmp/UDPLIST)

# Define secondary parameters
$IPT -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Save current configuration
#service iptables save
