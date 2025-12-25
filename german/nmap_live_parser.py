import re
from nmap_services_loader import NMAP_SPECIALS

def parse_line(tool_name, line, live_findings):
    l = line.lower()
    
    if "nmap" in tool_name.lower():
        match = re.search(r"(\d+)/(tcp|udp)\s+open\s+([\w\-\?]+)", l)
        
        if match:
            service_name = match.group(3)
            ignore_list = ["unknown", "tcpwrapped", "service"]
            
            if service_name not in ignore_list:
                live_findings["nmap"].add(service_name)
        
        for pattern, label in NMAP_SPECIALS.items():
            if pattern in l:
                live_findings["nmap"].add(label)

    if "ferox" in tool_name.lower() or "gobuster" in tool_name.lower():
        if " 200 " in line or " 301 " in line:
            ext_match = re.search(r"\.(\w{2,4})$", line.strip())
            if ext_match:
                ext = ext_match.group(1)
                if ext not in ["com", "net", "org", "edu", "de"]:
                    live_findings["ferox"].add(ext)

    if "ipv6" in l or "aaaa" in l:
        if "address" in l or "addr" in l:
             live_findings["ipv6"].add("ipv6")

    if "nikto" in tool_name.lower():
        if "wp-config" in l:
            live_findings["nikto"].add("wpconfig")
        if "admin" in l:
            live_findings["nikto"].add("admin_panel")

    if "curl" in tool_name.lower():
        if "set-cookie" in l:
            live_findings["curl"].add("cookie")