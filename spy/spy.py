# -*- coding: utf-8 -*-
import docker
import netifaces as ni
import logging


def get_network_info(iface):
    client = docker.APIClient()
    ip = ni.ifaddresses(iface)[ni.AF_INET][0]['addr']

    mapping = {}

    for c in client.containers():
        try:
            mapping[c["Names"][0][1:]] = {"ip": ip,
                                          "private_ip": c["NetworkSettings"]["Networks"]["bridge"]["IPAddress"],
                                          "ports": [port["PrivatePort"] for port in c["Ports"] if
                                                    port.get("IP", "0.0.0.0") in ["0.0.0.0", ip]]}
        except:
            logging.warning("failed to get data for container %s" % c["Names"][0][1:])

    return mapping
