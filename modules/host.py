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
        return (
            f"{self.ip:<15} | {self.mac:<17} | "
            f"{(self.hostname or 'N/A'):<25}"
            + (f" | Port: {self.port}" if self.port else "")
        )

    def to_dict(self):
        return {
            "ip": self.ip,
            "mac": self.mac,
            "hostname": self.hostname,
            "is_online": self.is_online,
            "port": self.port
        }