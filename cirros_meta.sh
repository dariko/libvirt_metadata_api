#!/bin/bash

BIND_ADDR=127.0.0.1:1024
VM_IPADDR=192.168.122.19

echo "URL START: index"
curl -H "X-Forwarded-For: $VM_IPADDR" http://$BIND_ADDR/
echo
echo "URL END: index"
echo
echo "URL START: /latest/meta-data/"
curl -H "X-Forwarded-For: $VM_IPADDR" http://$BIND_ADDR/latest/meta-data/
echo
echo "URL END: /latest/meta-data/"
echo
echo "URL START: /latest/meta-data/instance-id"
curl -H "X-Forwarded-For: $VM_IPADDR" http://$BIND_ADDR/latest/meta-data/instance-id
echo
echo "URL END: /latest/meta-data/instance-id"
echo
echo "URL START: /latest/meta-data/public-ipv4"
curl -H "X-Forwarded-For: $VM_IPADDR" http://$BIND_ADDR/latest/meta-data/public-ipv4
echo
echo "URL END: /latest/meta-data/public-ipv4"
echo
echo "URL START: /latest/meta-data/local-ipv4"
curl -H "X-Forwarded-For: $VM_IPADDR" http://$BIND_ADDR/latest/meta-data/local-ipv4
echo
echo "URL END: /latest/meta-data/local-ipv4"
echo
echo "URL START: /latest/meta-data/public-keys"
curl -H "X-Forwarded-For: $VM_IPADDR" http://$BIND_ADDR/latest/meta-data/public-keys
echo
echo "URL END: /latest/meta-data/public-keys"
echo
echo "URL START: /latest/meta-data/public-keys/0/openssh-key"
curl -H "X-Forwarded-For: $VM_IPADDR" http://$BIND_ADDR/latest/meta-data/public-keys/0/openssh-key
echo
echo "URL END: /latest/meta-data/public-keys/0/openssh-key"
echo
echo "URL START: /latest/user-data/"
curl -H "X-Forwarded-For: $VM_IPADDR" http://$BIND_ADDR/latest/user-data/
echo
echo "URL END: /latest/user-data/"
echo
