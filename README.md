<p align="center">
  <img src="assets/recon_monster_banner.png" alt="Recon Monster Banner" width="80%">
</p>

<p align="center">
  <b>Autonomous Recon Framework for Offensive Security</b><br>
  Hands-off scanning · Live findings · Senior-grade workflows
</p>

<p align="center">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows-lightgrey.svg">
  <img src="https://img.shields.io/badge/Shell-Bash%20%7C%20PowerShell-green.svg">
  <img src="https://img.shields.io/badge/Status-Active%20Development-orange.svg">
  <img src="https://img.shields.io/github/stars/yourname/recon-monster?style=social">
</p>

---

# 🧊 Recon Monster – Winter Tool


Autonomous recon framework for real-world offensive security workflows.  
Built for **hands-off scanning**, **real-time live findings**, and **maximum control without micromanagement**.

Recon Monster runs independently through all recon phases, evaluates results live, and allows targeted intervention — without breaking the scan flow.

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

Recon Monster executes scans **sequentially and independently**:

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

## 📡 Live Finding System (Real Time)

The **Live Finding Banner** is the core of the tool.

- Updates **after every scan**
- Displays **immediately discovered results**
- Consistently labeled
- Color-highlighted
- No end-of-run parsing required

### Example (internal)


INTERNAL
════════════════════════════════════════════════════════
Live - Finding - System
════════════════════════════════════════════════════════
ipv6 : [x][x][x]
ports : openssh python-http
webserver : simplehttp
methods : [x][x][x]
cookie : [x][x][x]
nikto : wpconfig
dirscan : css html js png py
════════════════════════════════════════════════════════


➡️ **Relevant data visible instantly**, without reading logs.

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

## 🧠 Why Recon Monster?

- No tool spamming
- No blind scan flooding
- No waiting for final reports
- Built from **real recon sessions**
- Designed for **senior-level workflows**

Recon Monster is not a toy.  
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




