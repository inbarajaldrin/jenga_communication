# Jenga Communication ROS2 Package

This ROS2 package interfaces with Isaac Sim to manipulate and observe Jenga blocks via TCP communication. It consists of three main scripts: sending commands, simulating block movements, and receiving block poses.

## Scripts Overview

- **send_jenga_coords.py**: Sends coordinates or commands (like "play" or "reset") to the simulation.
- **simulate_jenga_blocks.py**: Listens for commands to place Jenga blocks, manipulate the simulation, and sends back block poses.
- **receive_jenga_coords.py**: Receives the poses of Jenga blocks and outputs their positions and orientations.

## Getting Started

### Prerequisites

1. Install ROS2 Foxy from [ROS2 Installation Guide](https://docs.ros.org/en/foxy/Installation.html).
2. Ensure Isaac Sim is set up on your system following the instructions from [NVIDIA Omniverse Isaac Sim](https://docs.omniverse.nvidia.com/app_isaacsim/app_isaacsim/installation.html).

### Running the Package

Open three terminals and run the following commands in each:

**Terminal 1: Run the Simulator**
```bash
cd ~/.local/share/ov/pkg/isaac-sim-2023.1.1
./python.sh /home/aaugus11/ros2_ws/src/jenga_communication/scripts/simulate_jenga_blocks.py
```

**Terminal 2: Send Commands**
```bash
ros2 run jenga_communication send_jenga_coords 1 1 0.015
ros2 run jenga_communication send_jenga_coords 1 1 0.045
ros2 run jenga_communication send_jenga_coords 0.9 1 0.075
# With rotation:
ros2 run jenga_communication send_jenga_coords 1 1 0.105 45
ros2 run jenga_communication send_jenga_coords play
ros2 run jenga_communication send_jenga_coords reset
```

**Terminal 3: Receive Poses**
```bash
ros2 run jenga_communication receive_jenga_coords
```

## Notes
- Ensure each script is executable: `chmod +x <script_name.py>`
- Adjust IP addresses and ports in the scripts if your setup differs from the defaults.
- The simulation and command scripts interact over localhost using designated ports (65432 for commands, 65433 for receiving poses).
