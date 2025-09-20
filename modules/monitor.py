# This module does an initial network discovery, after which it monitors the
# network for changes.
from modules.discover import discover
import time

def monitor_network(network, interval=10):
    known_devices = {}

    # Run an intitial discovery
    print(f"Initial host discovery on {network}...")
    current_devices = list(discover(network))
    for device in current_devices:
        # device.is_online = True
        known_devices[device.mac] = device
        yield "online", device

    print(f"Initial discovery found {len(known_devices)} devices.")

    # Monitor the network for changes
    while True:
        print(f'\nMonitoring network for changes...')
        time.sleep(interval)

        new_devices = list(discover(network))
        new_devices_dict = {device.mac: device for device in new_devices}

        # Update status for known devices
        for mac, known in known_devices.items():
            if mac in new_devices_dict:
                updated = new_devices_dict[mac]

                known.ip = updated.ip
                known.hostname = updated.hostname

                # Status change: offline -> online
                if not known.is_online:
                    known.is_online = True
                    yield "online", known
            else:
                # Status change: online -> offline
                if known.is_online:
                    known.is_online = False
                    yield "offline", known

        # Detect new devices
        for mac, dev in new_devices_dict.items():
            if mac not in known_devices:
                dev.is_online = True
                known_devices[mac] = dev
                yield "new", dev

        print(f'Devices currently online: {
            len([device for device in known_devices.values() if device.is_online])
            }')

if __name__ == "__main__":
    network = "192.168.1.0/24"
    for status, device in monitor_network(network):
        print(f"[{status.upper()}] {device}")