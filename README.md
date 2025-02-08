# VMCommander

*The ultimate tool to automate and control your virtual machines from the command line.*

---

## Overview
VMCommander is a CLI tool designed for Windows users who need an efficient and programmable way to manage their virtual machines. With VMCommander, you can start, stop, pause, or restart virtual machines manually, on a schedule, or automatically during system startup or shutdown.

---

## Features
- **Simple Management**: Quickly start, stop, pause, or restart your VMs with easy commands.
- **Task Scheduling**: Automate actions at specific times for hands-free management.
- **System Integration**: Execute actions automatically during Windows startup or shutdown.
- **Centralized Configuration**: Manage all VMs through a single, unified configuration file.
- **Status Overview**: View the current state and scheduled tasks for all VMs in an organized table.
- **Export & Import Configurations**: Save and share your VM setups easily.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/VMCommander.git
   ```
2. Navigate to the project directory:
   ```bash
   cd VMCommander
   ```
3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the program:
   ```bash
   python vmcommander.py
   ```

---

## Usage

### Basic Commands
- **Start a VM:**
  ```bash
  python vmcommander.py start <vm_name>
  ```
- **Stop a VM:**
  ```bash
  python vmcommander.py stop <vm_name>
  ```
- **Pause a VM:**
  ```bash
  python vmcommander.py pause <vm_name>
  ```
- **Restart a VM:**
  ```bash
  python vmcommander.py restart <vm_name>
  ```

### Scheduling Tasks
- **Schedule a task:**
  ```bash
  python vmcommander.py schedule <start|stop|pause|restart> <vm_name> --time "HH:MM"
  ```
- **View scheduled tasks:**
  ```bash
  python vmcommander.py list
  ```

### Automating Startup/Shutdown
- **Add VM actions on startup:**
  ```bash
  python vmcommander.py startup add <start|pause> <vm_name>
  ```
- **Add VM actions on shutdown:**
  ```bash
  python vmcommander.py shutdown add <stop> <vm_name>
  ```
- **List all startup/shutdown configurations:**
  ```bash
  python vmcommander.py startup list
  python vmcommander.py shutdown list
  ```

---

## Configuration File
All configurations are stored in a centralized file called `vmcommander_config.json`. You can manually edit this file to fine-tune your settings.

---

## Support This Project

If you find this project helpful and want to support its development, consider donating to the following Bitcoin wallet:

**BTC Wallet:** `1YourBitcoinWalletAddressHere`

Thank you for your support! 🚀

---

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your feature description here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a Pull Request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

If you have any questions, feel free to reach out via the Issues section of this repository. We’d love to hear from you!

