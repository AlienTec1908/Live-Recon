import re
import json
from nmap_services_loader import NMAP_SPECIALS

def remove_ansi(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)

def parse_line(tool_name, line, live_findings):
    clean_line = remove_ansi(line).strip()
    l = clean_line.lower()
    
    if "nmap" in tool_name.lower():
        match = re.search(r"(\d+)/(tcp|udp)\s+open\s+(.*)", l)
        
        if match:
            full_service_line = match.group(3)
            service_parts = full_service_line.split()

            if not service_parts:
                return

            base_service = service_parts[0]
            specific_found = False

            if "openssh" in full_service_line:
                live_findings["nmap"].add("openssh")
                live_findings["nmap"].discard("ssh")
                specific_found = True

            if "python" in full_service_line and "http" in base_service:
                live_findings["nmap"].add("python-http")
                live_findings["nmap"].discard("http")
                live_findings["nmap"].discard("http-alt")
                specific_found = True
            
            if "apache" in full_service_line:
                live_findings["nmap"].add("http-apache")
                live_findings["nmap"].discard("http")
                live_findings["nmap"].discard("http-alt")
                specific_found = True
            
            if "nginx" in full_service_line:
                live_findings["nmap"].add("http-nginx")
                live_findings["nmap"].discard("http")
                live_findings["nmap"].discard("http-alt")
                specific_found = True
            
            if "microsoft iis" in full_service_line:
                live_findings["nmap"].add("http-iis")
                live_findings["nmap"].discard("http")
                live_findings["nmap"].discard("http-alt")
                specific_found = True

            ignore_list = ["unknown", "tcpwrapped", "service"]
            if not specific_found and base_service not in ignore_list:
                live_findings["nmap"].add(base_service)

        for pattern, label in NMAP_SPECIALS.items():
            if pattern in l:
                live_findings["nmap"].add(label)

    if "ferox" in tool_name.lower() or "gobuster" in tool_name.lower():
        try:
            if line.strip().startswith("{"):
                data = json.loads(line)
                url = data.get("url", "")
                ext = url.split(".")[-1] if "." in url else ""
                
                if len(ext) > 4 or "/" in ext:
                    ext = ""
                
                if ext and ext not in ["com", "net", "org", "edu", "de"]:
                    live_findings["ferox"].add(ext)
        except json.JSONDecodeError:
            pass

    if "ipv6" in tool_name.lower():
        if "bytes from" in l:
            live_findings["ipv6"].add("ipv6-active")
        if "fe80:" in l:
            live_findings["ipv6"].add("link-local")

    if "nikto" in tool_name.lower():
        if "wp-config" in l:
            live_findings["nikto"].add("wpconfig")
        if "admin" in l:
            live_findings["nikto"].add("admin_panel")

    if "curl" in tool_name.lower():
        if "set-cookie" in l or "set-cookie" in clean_line:
            live_findings["cookie"].add("cookie-found")
        
        if "allow:" in l:
            # extrahiere methoden (alles nach allow:)
            methods = l.split("allow:", 1)[1].strip()
            # splitte bei komma, reinige und fuege hinzu
            for m in methods.split(","):
                m_clean = m.strip().upper()
                if m_clean:
                    live_findings["methods"].add(m_clean)
            
        if "server:" in l:
            parts = l.split("server:")
            if len(parts) > 1:
                srv = parts[1].strip().split("/")[0] # nimm nur den namen vor dem slash
                if srv:
                    live_findings["webserver"].add(srv)
        
        if "x-powered-by:" in l:
            parts = l.split("x-powered-by:")
            if len(parts) > 1:
                tech = parts[1].strip()
                live_findings["webserver"].add(tech)