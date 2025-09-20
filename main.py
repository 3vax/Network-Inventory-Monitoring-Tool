from modules.discover import discover
from modules.host import NetworkDevice
from modules.monitor import monitor_network


if __name__ == "__main__":
    print("""
________________________________________________________________________________
Welcome to the Network Inventory Monitoring Tool!
This tool will discover devices on your network and monitor them for changes.
        1. Discover devices
        2. Monitor network
        3. Exit
Please select an option (1-3):
________________________________________________________________________________"""          
          )
    


    option = input()
    if option == "1":
        network = input("Enter the network to discover (e.g., '192.168.1.0/24'): ")
        print("Starting network discovery...")
        devices = discover(network)
        device_list = []
        for device in devices:
            print(f'\nDevice found:\nIP: {device.ip}\nMAC: {device.mac}\nHostname: {device.hostname}\nOnline: {device.is_online}')
            device_list.append(device)
        print(f'Discovered {len(device_list)} devices.')
    
    elif option == "2":
        network = input("Enter the network to monitor (e.g., '192.168.1.0/24'): ")
        print("Starting network monitoring...")
        try:
            for status, device in monitor_network(network):
                print(f"[{status.upper()}] {device}")
        except KeyboardInterrupt:
            print("\nMonitoring stopped by user.")

    elif option == "3":
        print("Exiting the program...")
        exit()