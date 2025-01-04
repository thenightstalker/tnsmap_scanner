![Description](https://github.com/thenightstalker/tnsmap_scanner/blob/main/nmap.png)

TNSMAP Scanner - Network Scanning Tool with Proxychains and Tor (Linux Only)

TNSMAP is a Linux-only network scanning tool that demonstrates penetration testing techniques using Nmap, Proxychains, and Tor for enhanced anonymity. The tool allows users to perform network scans on remote systems while hiding their IP address, providing a secure and private scanning process.
Key Features:

    Network Scanning: Uses Nmap for detailed network scanning.
    Anonymity: Routes scans through Proxychains and Tor to hide your IP address, providing anonymity during the scan.
    Graphical Interface: Easy-to-use Tkinter GUI for controlling and viewing scan results.
    Real-Time Output: View live results of the network scan in the GUI.
    Scan Cancellation: Ability to stop ongoing scans with a single click.

Disclaimer

This tool is for educational purposes only. Unauthorized network scanning is illegal and unethical. You are solely responsible for obtaining proper authorization before scanning any network or system. Ensure compliance with all applicable local, state, national, and international laws before using this software
Requirements:

    Linux OS (Tested on Ubuntu-based distributions)
    Python 3.x
    Nmap: Required for network scanning.
    Proxychains: Configured to work with Tor.
    Tor: The Tor service must be installed and running for anonymity.

Installation (Linux)

Clone the repository
    
    git clone https://github.com/yourusername/tnsmap-scanner.git

Install the necessary dependencies

    sudo apt-get install nmap proxychains tor python3-tk

Ensure that Proxychains is configured to use Tor

    Edit /etc/proxychains4.conf to set Tor as the proxy

Usage:

    sudo service tor start
    Run the Python script
    python3 tnsmap_scanner.py

Open the tool.
Enter the target IP address or hostname you want to scan
Click the "Start Scanning" button to begin the scan
View the scan results in the GUI output window
If needed, click "Cancel Scan" to abort the scan

Important Notes:

    This tool is Linux-only and may not work on other operating systems.
    Ensure Proxychains and Tor are running before using the tool.
    You must have explicit permission to scan any network or system to avoid legal and ethical issues.

Contributing:

Contributions are welcome! Fork the repository, make improvements, and submit pull requests. Please follow the contribution guidelines provided in the repository
