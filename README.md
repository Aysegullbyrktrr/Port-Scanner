# 🔍 PortSleuth

## 📖 About
PortSleuth is a fast and efficient port scanning tool designed to provide clear and structured output. It allows users to scan a given IP address or subnet for open ports, retrieve banner information, and display results in an easy-to-read format. This tool is designed to be quick, customizable, and user-friendly, making it ideal for both security professionals and enthusiasts.

## ⚙️ Installation
```bash
# Clone the repository
git clone https://github.com/Aysegullbyrktrr/PortSleuth.git
cd PortSleuth

# Make it executable
chmod +x portsleuth.py
```

## 🚀 Usage
```bash
python portsleuth.py <IP or Subnet> [options]
```

### 🔹 Basic Scan
```bash
python portsleuth.py 192.168.1.0/24
```
Scans a subnet using the default port list.

### 🔹 Scan with Custom Ports
```bash
python portsleuth.py 192.168.1.1 -p 22,80,443
```
Scans only the specified ports on the target IP.

### 🔹 Detailed Scan (Banner Grabbing)
```bash
python portsleuth.py 192.168.1.1 -p 22,80,443 -d
```
Retrieves banner information from open ports.

### 🔹 Multi-Threaded Scan
```bash
python portsleuth.py 192.168.1.0/24 -T 200
```
Uses 200 threads for faster scanning.

### 🔹 Set Timeout
```bash
python portsleuth.py 192.168.1.1 -t 3
```
Sets socket timeout to 3 seconds.

## 🛠 Features
✅ Multi-threaded scanning to improve scan speed  
✅ Banner grabbing to identify services running on open ports  
✅ Option to select custom ports for targeted scanning  
✅ Automatic subnet scanning for network-wide coverage  
✅ Adjustable timeout for fine-tuning scan performance  

## 📌 Example Output
```
Starting scan on 192.168.1.0/24 using fast mode...

--- SCAN RESULTS ---

Host: 192.168.1.1 (Online)
  - 22/tcp   OPEN  OpenSSH 7.4
  - 80/tcp   OPEN  Apache 2.4.41
  - 443/tcp  OPEN  nginx 1.18.0

Host: 192.168.1.2 (Online)
  - 3389/tcp OPEN  Microsoft RDP Service

Scan completed in 9.87 seconds.
```

## 🏗 Contributing
Pull requests are welcome! If you'd like to contribute, please fork the repository and submit a PR.

## 📜 License
This project is licensed under the **MIT License**.

