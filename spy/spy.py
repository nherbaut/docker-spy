import docker
import yaml
import sys
import netifaces as ni

def get_network_info(iface):
    client = docker.from_env()
    ip = ni.ifaddresses(iface)[ni.AF_INET][0]['addr']
    mapping = {c["Names"][0][1:]: {"ip": ip, "ports": [port["PublicPort"] for port in c["Ports"]]} for c in
           client.containers()}
    return yaml.dump(mapping)
