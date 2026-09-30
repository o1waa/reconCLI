# Recon CLI Framework

A modular, CLI-first offensive security reconnaissance framework written in Python. Designed to streamline initial footprinting, service identification, and web application enumeration.

---

## 🛠️ Module Overview

* **Fast Scanner (`fast_scanner.py`)**: Multithreaded TCP port scanner for rapid host reconnaissance.
* **Banner Grabber (`banner_grabber.py`)**: Service and banner identification tool with HTTP and SSL/TLS support.
* **HTTP Directory Scanner (`http_directory.py`)**: Fuzzing and enumeration tool for discovering hidden directories and files.
* **Orchestrator (`recon_cli.py`)**: Unified management interface offering both an interactive terminal menu and direct command-line execution.

---

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/o1waa/reconCLI.git](https://github.com/o1waa/reconCLI.git)
   cd recon


pip install requests urllib3


python recon_cli.py

