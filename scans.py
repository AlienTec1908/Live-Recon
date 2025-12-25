SCANS_TO_RUN = [
    {
        "name": "IPv6 Discovery Scan",
        "command": ["ping6", "-c", "3", "ff02::1"]
    },
    {
        "name": "Curl - HTTP Headers",
        "command": ["curl", "-I", "-L", "-v", "http://{TARGET}", "-s"]
    },
    {
        "name": "Curl - Cookie Jar",
        "command": ["curl", "--head", "-L", "--cookie-jar", "logs/{TARGET}/cookies.txt", "http://{TARGET}", "-s"]
    },
    {
        "name": "Curl - Allowed Methods",
        "command": ["curl", "-X", "OPTIONS", "-I", "-L", "http://{TARGET}", "-s"]
    },
    {
        "name": "Nmap UDP Scan",
        "command": ["nmap", "-sU", "--top-ports", "1000", "-T5", "-n", "-Pn", "--min-rate", "5000", "-oA", "logs/{TARGET}/nmap_udp", "-oJ", "logs/{TARGET}/nmap_udp.json", "{TARGET}"]
    },
    {
        "name": "Nmap SCTP Scan (Hostscan)",
        "command": ["nmap", "-sY", "-n", "-p-", "-Pn", "--min-rate", "5000", "-oA", "logs/{TARGET}/nmap_sctp", "-oJ", "logs/{TARGET}/nmap_sctp.json", "{TARGET}"]
    },
    {
        "name": "Nmap Full Scan",
        "command": ["nmap", "-sS", "-sC", "-sV", "-p-", "-Pn", "--min-rate", "5000", "-oA", "logs/{TARGET}/nmap_full", "-oJ", "logs/{TARGET}/nmap_full.json", "{TARGET}"]
    },
    {
        "name": "Nikto Scan",
        "command": ["nikto", "-h", "{TARGET}", "-nointeractive", "-Format", "json", "-output", "logs/{TARGET}/nikto.json", "-Format", "txt", "-output", "logs/{TARGET}/nikto.txt"]
    },
    {
        "name": "Feroxbuster Scan",
        "command": [
            "feroxbuster", 
            "-u", "http://{TARGET}", 
            "-w", "/usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt", 
            "-x", "txt,php,rar,zip,tar,pub,xls,docx,doc,sql,db,mdb,asp,aspx,accdb,bat,ps1,exe,sh,py,pl,gz,jpeg,jpg,png,html,phtml,xml,csv,dll,pdf,raw,rtf,xlsx,zip,kdbx,bak,svg,pem,crt,json,conf,ELF,elf,c,java,lib,cgi,csh,config,deb,desc,exp,eps,diff,icon,mod,ln,old,rpm,js.map,pHtml", 
            "-C", "503,404,403",
            "-k",
            "--silent",
            "--json", "--output", "logs/{TARGET}/feroxbuster.json"
        ]
    }
]