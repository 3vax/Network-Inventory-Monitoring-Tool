# This module performs network discovery using ARP requests to identify devices
# on the network. It returns a list of NetworkDevice objects representing the
# discovered devices.

from scapy.all import ARP, Ether, srp
from modules.host import NetworkDevice
import socket

def discover(network):
    # Create an ARP request packet
    arp_request = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp_request

    # Send the packet and capture the response
    result = srp(packet, timeout=2, verbose=False)[0]

    # Yield devices one by one
    for _, received in result:
        device = NetworkDevice(received.psrc, received.hwsrc)
        device.is_online = True
        try:
            device.hostname = socket.gethostbyaddr(received.psrc)[0]
        except socket.herror:
            device.hostname = 'N/A'
        yield device

if __name__ == "__main__":
    # Example usage
    network = "192.168.1.0/24"
    discovered_devices = discover(network)
    for device in discovered_devices:
        print(device)