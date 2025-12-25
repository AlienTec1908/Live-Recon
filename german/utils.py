import shutil
import sys
import subprocess
import os

def check_dependencies():
    print("[+] Prüfe Werkzeugkasten...")
    
    required_tools = [
        "nmap", "nikto", "feroxbuster", "curl", "wpscan", 
        "joomscan", "hydra", "rpcclient", "enum4linux", "wget"
    ]
    
    missing_tools = []
    
    for tool in required_tools:
        if shutil.which(tool) is None:
            missing_tools.append(tool)
            
    if missing_tools:
        print(f"[FEHLER] Die folgenden Werkzeuge fehlen: {', '.join(missing_tools)}")
        
        answer = input("Soll der Hammer versuchen, sie automatisch zu installieren? (apt-get wird verwendet) [y/N]: ")
        
        if answer.lower() == 'y':
            print("[+] Versuche, fehlende Werkzeuge zu installieren...")
            
            if os.getuid() == 0:
                sudo_prefix = []
            else:
                sudo_prefix = ["sudo"]

            try:
                update_command = sudo_prefix + ["apt-get", "update"]
                subprocess.run(update_command, check=True)
                
                install_command = sudo_prefix + ["apt-get", "install", "-y"] + missing_tools
                subprocess.run(install_command, check=True)
                
                print("[+] Installation erfolgreich! Prüfe erneut...")
                check_dependencies()
            except subprocess.CalledProcessError:
                print("[FEHLER] Automatische Installation fehlgeschlagen. Bitte manuell installieren.")
                sys.exit(1)
            except FileNotFoundError:
                print("[FEHLER] 'sudo' oder 'apt-get' nicht gefunden. Bitte manuell installieren.")
                sys.exit(1)
        else:
            print("[FEHLER] Abbruch durch Benutzer. Bitte fehlende Werkzeuge installieren.")
            sys.exit(1)
    else:
        print("[+] Alle Werkzeuge sind einsatzbereit.")