import subprocess
import time
from pymobiledevice3.usbmux import list_devices
from getpass import getpass
import os
from utils.utils import run_command_with_sudo

def list_connected_devices():
    devices = []
    try:
        devices = list_devices()
        print(f"\nConnected devices: \n")
        for device in devices:
            if hasattr(device, 'serial'):
                print(f"UDID: {device.serial}")
            if hasattr(device, 'connection_type'):
                print(f"Connection: {device.connection_type}\n")
    except Exception as e:
        print(f"\nError listing devices: {e}")
    return devices

def start_tunneld(password):
    command_start_tunneld = ['python3', '-m', 'pymobiledevice3', 'remote', 'tunneld']
    print("\nStarting Tunneld...")
    process = subprocess.Popen(['sudo', '-S'] + command_start_tunneld, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.stdin.write(password + '\n')
    process.stdin.flush()
    time.sleep(5)
    print("\nTunneld started.")
    return process

def start_tunnel(udid, password):
    command_start_tunnel = ['pymobiledevice3', 'remote', 'start-tunnel', '--udid', udid]
    print("\nStarting tunnel...\n")
    process = subprocess.Popen(['sudo', '-S'] + command_start_tunnel, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    process.stdin.write(password + '\n')
    process.stdin.flush()
    
    while True:
        line = process.stdout.readline()
        if not line:
            break
        print(line, end='')

    process.stdout.close()
    process.wait()

    if process.returncode != 0:
        print("\nFailed to start tunnel")
        return None, None

    return process

def main(password):
    devices = list_connected_devices()
    if not devices:
        print("\nNo devices connected.")
        return

    udid = input("Enter the UDID of a device to continue: ").strip()

    tunneld_process = start_tunneld(password)
    time.sleep(5)

    start_tunnel(udid, password)

    print("\nTunnels started. Run the second script to continue.")

if __name__ == "__main__":
    password = getpass('\nEnter the sudo password: ')
    main(password)
