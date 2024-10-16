# Jenga Communication ROS2 Package

This ROS2 package interfaces with Isaac Sim to manipulate and observe Jenga blocks via TCP communication. It consists of three main scripts: sending commands, simulating block movements, and receiving block poses.

## Scripts Overview

- **send_jenga_coords.py**: Sends coordinates or commands (like "play" or "reset") to the simulation.
- **simulate_jenga_blocks.py**: Listens for commands to place Jenga blocks, manipulate the simulation, and sends back block poses.
- **receive_jenga_coords.py**: Receives the poses of Jenga blocks and outputs their positions and orientations.

## Getting Started

### Prerequisites

1. Install ROS2 Foxy from [ROS2 Installation Guide](https://docs.ros.org/en/foxy/Installation.html).
2. **Download and Set Up Omniverse Isaac Sim**:
   - Visit the [NVIDIA Omniverse Download Page](https://developer.nvidia.com/omniverse).
   - Search for **Omniverse SDK Download** and fill out the required information to access the downloads.
   - Download **Omniverse Launcher** for Linux.
   - Once the file is downloaded, make it executable by running:
     ```bash
     chmod +x <FILENAME>
     ```
   - Launch Omniverse Launcher.
   - Go to the **Nucleus** section, create a new server, and set up the details. Most settings can be left as default.
   - In the **Exchange** section, download the **Isaac Sim** app.
   - After the download, you can find the Isaac Sim app in the **Library** section, ready to be launched.

### Package Installation Steps

1. **Source ROS 2 Foxy and Workspace**:
   ```bash
   source /opt/ros/foxy/setup.bash
   source ~/ros2_ws/install/setup.bash
   ```

2. **Clone the Jenga Communication Repository**:
   ```bash
   cd ~/ros2_ws/src/
   git clone https://github.com/inbarajaldrin/jenga_communication.git
   ```

3. **Build the Workspace**:
   ```bash
   cd ~/ros2_ws
   colcon build
   ```

### Running the Package

Open **three terminals** and run the following commands in each:

#### Terminal 1: Run the Simulator
Navigate to the Isaac Sim installation directory and start the simulation with the `simulate_jenga_blocks.py` script:
```bash
cd ~/.local/share/ov/pkg/isaac-sim-2023.1.1
./python.sh /home/aaugus11/ros2_ws/src/jenga_communication/scripts/simulate_jenga_blocks.py
```

#### Terminal 2: Send Commands
In this terminal, use the `send_jenga_coords` node to send block placement and control commands:
```bash
ros2 run jenga_communication send_jenga_coords 1 1 0.015
ros2 run jenga_communication send_jenga_coords 1 1 0.045
ros2 run jenga_communication send_jenga_coords 0.9 1 0.075
# With rotation:
ros2 run jenga_communication send_jenga_coords 1 1 0.105 45
ros2 run jenga_communication send_jenga_coords play
ros2 run jenga_communication send_jenga_coords reset
```

#### Terminal 3: Receive Poses
Use the following command to receive block poses after the simulation has been manipulated:
```bash
ros2 run jenga_communication receive_jenga_coords
```

## Notes
- Adjust IP addresses and ports in the scripts if your setup differs from the defaults.
- The simulation and command scripts interact over localhost using designated ports (65432 for commands, 65433 for receiving poses).
