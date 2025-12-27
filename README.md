<p align="center">
  <img src="Liverecon.png" alt="agent-image-ripper cover" width="50%" style="height: 20rem;">
</p>
 
 
<p align="center">
  <b>Autonomous Recon Framework for Offensive Security</b><br>
  Hands-off scanning · Live findings · Senior-grade workflows
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
  <img src="https://img.shields.io/badge/Platform-Linux-lightgrey.svg" alt="Platform">
  <img src="https://img.shields.io/badge/Shell-Bash-green.svg" alt="Shell">
  <img src="https://img.shields.io/badge/Status-Active%20Development-orange.svg" alt="Status">
  <img src="https://img.shields.io/github/stars/AlienTec1908/Live-Recon?style=social" alt="GitHub Stars">
</p>


---

# 🧊 Live Recon – Winter Edition


Autonomous recon framework for real-world offensive security workflows.  
Built for **hands-off scanning**, **real-time live findings**, and **maximum control without micromanagement**.

Live Recon runs independently through all recon phases, evaluates results live, and allows targeted intervention — without breaking the scan flow.

---

## 🔥 Core Idea

**Start → observe → intervene only when necessary**

- Fully **autonomous recon pipeline**
- **Live finding system** with instant classification
- **No waiting for reports** — findings appear during the scan
- **Skippable scans** without breaking the pipeline
- **On-demand deep analysis**, not forced

---

## ⚙️ Autonomous Scan Workflow

Live Recon executes scans **sequentially and independently**:

1. HTTP / method analysis (curl)
2. Nmap TCP full scan
3. Nmap UDP scan
4. Nmap SCTP host scan
5. Web server identification
6. Nikto web scan
7. Feroxbuster directory scan
8. Live aggregation of all findings
9. Optional detailed view

No manual triggering of individual modules required.

---
<img src="banner-terminal.jpg" alt="agent-image-ripper cover" width="100%" style="height: 20rem;">


## 🚀 Usage

Run Live Recon by specifying a target IP address or hostname:

```bash
/bin/python3 /root/recontool_project/live_recon.py --ip <ip>
```

---

## ⚙️ Parameters

### `--ip <TARGET>`

Target IP address or hostname to scan.

**Example:**

```bash
/bin/python3 live_recon.py --ip example.com

```
---
 



## 📡 Live Finding System (Real Time)

The **Live Finding Banner** is the core of the tool.

- Updates **after every scan**
- Displays **immediately discovered results**
- Consistently labeled
- Color-highlighted
- No end-of-run parsing required

### Example (internal)
```text
INTERNAL
════════════════════════════════════════════════════════
Live - Finding - System
════════════════════════════════════════════════════════
ipv6       : [x][x][x]
ports      : openssh python-http
webserver  : simplehttp
methods    : [x][x][x]
cookie     : [x][x][x]
nikto      : wpconfig
dirscan    : css html js png py
════════════════════════════════════════════════════════
```
<br><br>
---

---

## 🌐 Automatic Internal vs External Target Detection

Live Recon automatically detects whether the provided target is an **internal** or **external** address — no manual mode selection required.

### 🔍 How it works

When you start a scan with `--ip`, Live Recon evaluates the target:

- **Internal targets**
  - Private IPv4 ranges (RFC1918)
    - `10.0.0.0/8`
    - `172.16.0.0/12`
    - `192.168.0.0/16`
  - Loopback (`127.0.0.1`)
  - Link-local addresses

- **External targets**
  - Public IPv4 / IPv6 addresses
  - Internet-facing hostnames and domains

The detection happens **automatically at runtime**.

---

### 🧠 Why this matters

Based on the detected target type, Live Recon:

- Adjusts scan behavior and expectations
- Applies the correct threat model
- Clearly separates **internal recon** from **external recon**
- Prevents confusion in mixed environments

No flags. No config switches. No user error.

---

### 📡 Live Banner Integration

The detected mode is shown **directly in the Live Finding Banner**:

- 🟢 **INTERNAL** — green banner  
- 🔴 **EXTERNAL** — red banner  

This status remains visible throughout the entire scan and updates live with findings.

Example (conceptual):



---

➡️ **Relevant data visible instantly**, without reading logs.

<img src="live-banner-terminal.jpg" alt="agent-image-ripper cover" width="100%" style="height: 20rem;">

---

## 🎨 Color & Label Logic

- Services, ports, web servers → clearly named
- Web findings (e.g. `wp-config.php`) → instantly flagged
- Dirscan results → grouped by file extensions
- Consistent status across all scans

No noise. No duplicates.

---

## ⏭️ Skip Scans (CTRL + C)

Any running scan can be **selectively skipped**:

CTRL + C


Result:

- Current scan exits cleanly
- Tool **automatically continues with the next module**
- Live finding system remains active
- No full recon interruption

Example:

[!] SCAN ABORTED: Feroxbuster scan skipped.


Ideal for long scans or clear prioritization.

---

## 🔍 On-Demand Detail View (`J` Key)

At the end of the autonomous run:

[?] If you want to display all scans in detail, press 'J':



Pressing `J` provides:

- Full Nikto reports
- Cookie dumps
- Feroxbuster JSON & text output
- Structured per-module results
- Reproducible findings

➡️ **Details only when you want them.**

---

## 📁 Output & Reports

Automatically generated:

- `cookies.txt`
- `nikto.txt`
- `nikto.json`
- `feroxbuster.json`
- `nmap_*.json`
- Structured log directories per target

Suitable for reporting, post-analysis, and tool chaining.

---

## 🧠 Why Live Recon?

- No tool spamming
- No blind scan flooding
- No waiting for final reports
- Built from **real recon sessions**
- Designed for **senior-level workflows**

Live Recon is not a toy.  
It is a **recon operator** that works for you.

---

## ❄️ Winter Edition – Focus

- Stability
- Readability
- Live feedback
- Autonomy
- Control without overhead

---

## 🚀 Use Cases

- CTF recon
- Initial access reconnaissance
- Lab enumeration
- Pre-exploitation mapping
- Red team preparation

---

## 📖 Code Architecture & Documentation

Want to understand how this tool works under the hood? I've written a detailed, line-by-line documentation for students and developers who want to learn from the source code.

This is not just a tool, it's a playbook.
 
**[➡️ Dive into the Full Code Documentation](docs/recon-doku-eng.html)**
---

## ⚠️ Security & Legal Disclaimer

This tool is intended **exclusively for authorized security testing**.

- Use **only** on systems you own or have **explicit written permission** to test
- Designed for **professional recon**, **labs**, **CTFs**, and **internal assessments**
- The author assumes **no responsibility** for misuse or damage caused by this tool
- You are solely responsible for complying with **local laws and regulations**

Live Recon was built to support **real-world offensive security workflows**,  
**not** for illegal or unethical activity.

**Use responsibly.**


