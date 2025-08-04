from modules.discover import discover


if __name__ == "__main__":
    devices = []
    for device in discover("192.168.1.0/24"):
        devices.append(device)
        print(f'Device found: {device.ip} with MAC {device.mac} and hostname {device.hostname}')
    print(f'Discovered {len(devices)} devices.')