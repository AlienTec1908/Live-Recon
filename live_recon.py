import argparse
import subprocess
import ipaddress
import os
import time
import json

from scans import SCANS_TO_RUN
from utils import check_dependencies
from detailed_logs import show_detailed_logs
from banner import (
    print_mega_banner,
    print_live_banner,
    print_scan_title,
    print_scan_end
)
from nmap_runner import NmapRunner
from live_parser import parse_line
import nmap_subroutines


def diff_intern_extern(target):
    try:
        ip = ipaddress.ip_address(target)
        return "internal" if ip.is_private or ip.is_loopback else "external"
    except ValueError:
        return "external"


if __name__ == "__main__":
    os.system("clear")
    print_mega_banner()
    check_dependencies()
    time.sleep(1)

    parser = argparse.ArgumentParser(description="Recon Monster – Autonomous Recon Framework")
    parser.add_argument("--ip", required=True, help="Target IP address or hostname")
    args = parser.parse_args()
    target = args.ip

    sudo = [] if os.getuid() == 0 else ["sudo"]
    scan_mode = diff_intern_extern(target)

    log_dir = f"logs/{target}"
    os.makedirs(log_dir, exist_ok=True)

    # Fixed categories for the live finding banner
    live_findings = {
        "ipv6": set(),
        "nmap": set(),
        "webserver": set(),
        "methods": set(),
        "cookie": set(),
        "nikto": set(),
        "ferox": set(),
    }

    for scan in SCANS_TO_RUN:
        proc = None
        try:
            print_live_banner(scan_mode, live_findings)
            print_scan_title(scan["name"])

            cmd = [p.replace("{TARGET}", target) for p in scan["command"]]
            if cmd[0] not in ["curl", "ping6"]:
                cmd = sudo + cmd

            proc = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                errors="ignore"
            )

            for line in proc.stdout:
                is_ferox = "ferox" in scan["name"].lower()

                if is_ferox:
                    try:
                        if line.strip().startswith("{"):
                            data = json.loads(line)
                            url = data.get("url", "")
                            status = data.get("status", 200)

                            lime_color = "\033[92m"
                            reset_color = "\033[0m"

                            print(f"{lime_color}[+] Found: {url} (Status: {status}){reset_color}")
                        else:
                            print(line.rstrip())
                    except json.JSONDecodeError:
                        print(line.rstrip())
                else:
                    print(line.rstrip())

                parse_line(scan["name"], line, live_findings)

            proc.wait()
            print_scan_end()

            if "Nmap" in scan["name"]:
                jf = f"{log_dir}/nmap_full.json"
                if os.path.exists(jf):
                    tasks = NmapRunner(jf).run_analysis()
                    for t in tasks:
                        live_findings["nmap"].add(t)

        except KeyboardInterrupt:
            print(f"\n\n[!] SCAN SKIPPED: {scan['name']} interrupted by user.")
            if proc:
                proc.terminate()
                try:
                    proc.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    proc.kill()
            print_scan_end()
            time.sleep(1)
            continue

    print_live_banner(scan_mode, live_findings)

    for task in live_findings["nmap"]:
        fn = getattr(nmap_subroutines, task, None)
        if fn:
            fn(target)

    show_detailed_logs(log_dir)
