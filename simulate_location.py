import subprocess
import time
from getpass import getpass
import os
from utils.utils import run_command_with_sudo

def set_location(latitude, longitude, rsd_address, rsd_port, password):
    try:
        command_set_location = [
            'pymobiledevice3', 'developer', 'dvt', 'simulate-location', 'set',
            '--rsd', rsd_address, rsd_port, '--', str(latitude), str(longitude)
        ]
        print("\nExecuting command to set location:", " ".join(command_set_location))
        process = subprocess.Popen(['sudo', '-S'] + command_set_location, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.stdin.write(password + '\n')
        process.stdin.flush()

        while True:
            line = process.stdout.readline()
            if not line:
                break
            print(line, end='')

        process.stdout.close()
        process.wait()

        if process.returncode == 0:
            print("\nLocation set successfully")
        else:
            print(f"\nError setting location. Return code: {process.returncode}")
    except Exception as e:
        print(f"\nError executing command: {e}")

def validate_coordinates(lat, lon):
    try:
        lat = float(lat)
        lon = float(lon)
        lat_str = f"{lat:.6f}"
        lon_str = f"{lon:.6f}"
        if len(lat_str.split('.')[1]) != 6 or len(lon_str.split('.')[1]) != 6:
            print("\nInvalid input. Latitude and longitude must have exactly 6 decimal places.")
            return None, None
        if -90 <= lat <= 90 and -180 <= lon <= 180:
            return lat, lon
        else:
            print("\nInvalid coordinates. Latitude must be between -90 and 90 and longitude between -180 and 180.")
            return None, None
    except ValueError:
        print("\nInvalid input. Please enter numeric values for latitude and longitude.")
        return None, None

def main(password):
    rsd_address = input("\nEnter RSD address (tunnel): ").strip()
    rsd_port = input("\nEnter RSD port (tunnel): ").strip()

    locations = {
        '1': ('Times Square, New York', 40.758000, -73.985500),
        '2': ('Eiffel Tower, Paris', 48.858400, 2.294500),
        '3': ('Great Wall of China', 40.431900, 116.570400),
        '4': ('Sydney Opera House, Sydney', -33.856800, 151.215300),
        '5': ('Statue of Liberty, New York', 40.689200, -74.044500),
        '6': ('Colosseum, Rome', 41.890200, 12.492200),
        '7': ('Christ the Redeemer, Rio de Janeiro', -22.951900, -43.210500),
        '8': ('Taj Mahal, India', 27.175100, 78.042100),
        '9': ('Mount Fuji, Japan', 35.360600, 138.727400),
        '10': ('Santorini, Greece', 36.393200, 25.461500)
    }

    while True:
        print('\n')
        print('1- Times Square, New York')
        print('2- Eiffel Tower, Paris')
        print('3- Great Wall of China')
        print('4- Sydney Opera House, Sydney')
        print('5- Statue of Liberty, New York')
        print('6- Colosseum, Rome')
        print('7- Christ the Redeemer, Rio de Janeiro')
        print('8- Taj Mahal, India')
        print('9- Mount Fuji, Japan')
        print('10- Santorini, Greece')
        print('11- Enter coordinates manually')
        print('12- Exit')

        option = input('\nSelect location: ')

        if option in locations:
            name, latitude, longitude = locations[option]
            print(f"\nYou selected: {name} ({latitude}, {longitude})")
        elif option == '11':
            lat = input("\nEnter latitude (-90.000000 to 90.000000): ").strip()
            lon = input("\nEnter longitude (-180.000000 to 180.000000): ").strip()
            latitude, longitude = validate_coordinates(lat, lon)
            if latitude is None or longitude is None:
                continue
            print(f"\nYou entered coordinates: ({latitude}, {longitude})")
        elif option == '12':
            print("\nExiting...")
            break
        else:
            print("\nInvalid option, please try again.")
            continue

        set_location(latitude, longitude, rsd_address, rsd_port, password)

if __name__ == "__main__":
    password = getpass('\nEnter the sudo password: ')
    main(password)
