# This class is used to store information about network devices discovered on
# the network.

class NetworkDevice:
    def __init__(self, ip, mac, hostname=None, is_online=False, port=None):
        self.ip = ip
        self.port = port
        self.mac = mac
        self.hostname = hostname
        self.is_online = is_online

    def __str__(self):
        base = f"IP: {self.ip}, MAC: {self.mac}, Hostname: {self.hostname}, Online: {self.is_online}"
        if self.port is not None:
            base += f", Port: {self.port}"
        return base
