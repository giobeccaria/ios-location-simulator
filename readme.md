# iOS Location Simulator

This project consists of two Python scripts designed to simulate the geographic location of connected iOS mobile devices. It uses the 'pymobiledevice3' library, a Python implementation of 'libimobiledevice', which allows communication with iOS devices without the need for jailbreaking.

This tool is particularly useful for developers and testers of mobile applications who need to test location-based features, such as maps and location services, without physically moving to different locations.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Start Tunnels](#start-tunnels)
   - [Simulate Location](#simulate-location)
4. [Scripts Explanation](#scripts-explanation)
   - [start_tunnels.py](#start_tunnelspy)
   - [simulate_location.py](#simulate_locationpy)
5. [Troubleshooting](#troubleshooting)
6. [Contributing](#contributing)
7. [License](#license)

## Requirements
- Python 3.x
- `sudo` privileges

## Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ios-location-simulator.git
    cd ios-location-simulator
    ```

2. **Install required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Ensure `/sbin` is in your system PATH:**
    ```bash
    export PATH=$PATH:/sbin
    ```

## Usage

### Start Tunnels
The first step is to set up the necessary tunneling service to enable communication between your computer and the connected iOS device.

1. **Run the `start_tunnels.py` script:**
    ```bash
    python start_tunnels.py
    ```

2. **Enter your `sudo` password when prompted.**

3. **List connected devices and select one by entering its UDID.**

### Simulate Location
Once the tunneling service is set up, you can simulate a new geographical location on the connected iOS device.

1. **Run the `simulate_location.py` script:**
    ```bash
    python simulate_location.py
    ```

2. **Enter your `sudo` password when prompted.**

3. **Provide the RSD address and port displayed by the `start_tunnels.py` script.**

4. **Select a predefined location or enter latitude and longitude values manually.**

5. **The script will simulate the selected location on your iOS device.**

## Scripts Explanation

### start_tunnels.py
This script is responsible for setting up the tunneling service to enable communication between your computer and the connected iOS device.

- **List connected devices:** The script lists all iOS devices connected to your computer to help you identify the device you want to work with.
- **Start tunneling service:** The script starts a tunneling service called `tunneld`, which sets up the environment to allow communication with the iOS device.
- **Open specific tunnel:** The script opens a specific tunnel for the selected device, establishing a secure and functional communication channel needed to simulate the device's location.

### simulate_location.py
This script is used to simulate a new geographical location on the connected iOS device.

- **RSD address and port:** The user enters the RSD address and port displayed by the `start_tunnels.py` script.
- **Select location:** The user selects a location from a predefined list or enters latitude and longitude values manually.
- **Simulate location:** The script sends the location simulation command to the iOS device through the tunnel, changing its reported geographical location to the selected coordinates.

## Troubleshooting
- **No devices found:** Ensure your iOS device is connected and recognized by your computer.
- **Permission denied:** Make sure you have `sudo` privileges and have entered the correct password.
- **Tunneling service not starting:** Verify that `/sbin` is in your system PATH and all required Python packages are installed.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with any improvements or fixes.

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit/).
