import os
import json
import shutil

class LogColors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    TURQ = "\033[96m"
    
    # Lime Background (Bright Green), Black Text
    HEADER_STYLE = "\033[102m\033[30m\033[1m"
    
    # Status Codes
    GREEN = "\033[92m" # 200
    YELLOW = "\033[93m" # 300
    RED = "\033[91m"   # 400/500
    BLUE = "\033[94m"  # Info

def get_terminal_width():
    try:
        return shutil.get_terminal_size().columns
    except OSError:
        return 100

def print_file_header(filename):
    width = get_terminal_width()
    title = f" REPORT: {filename} "
    
    pad_len = width - len(title)
    pad_l = pad_len // 2
    pad_r = pad_len - pad_l
    
    bar_l = f"\033[102m{' ' * pad_l}"
    bar_r = f"\033[102m{' ' * pad_r}"
    
    print(f"\n{LogColors.TURQ}{'═' * width}{LogColors.RESET}")
    print(f"{bar_l}{LogColors.HEADER_STYLE}{title}{bar_r}{LogColors.RESET}")
    print(f"{LogColors.TURQ}{'═' * width}{LogColors.RESET}")

def format_ferox_line(line):
    try:
        data = json.loads(line)
        
        # Nur Responses interessieren uns, keine Heartbeats/Logs
        if data.get("type") != "response":
            return None

        status = data.get("status", 0)
        url = data.get("url", "")
        length = data.get("content_length", 0)
        
        # Farbe basierend auf Status Code
        s_color = LogColors.GREEN
        if 300 <= status < 400: s_color = LogColors.YELLOW
        if status >= 400: s_color = LogColors.RED
        
        # Format: [200]  (1234b)  http://url...
        return f"{s_color}[{status}]{LogColors.RESET}  ({LogColors.BLUE}{length:>6}b{LogColors.RESET})  {url}"
        
    except json.JSONDecodeError:
        return None

def show_detailed_logs(log_directory):
    answer = input("\n[?] Wenn Sie alle Scans detailliert anzeigen lassen wollen, geben Sie 'J' ein und drücken Enter: ")
    
    if answer.lower() == 'j':
        try:
            log_files = sorted(os.listdir(log_directory))
            if not log_files:
                print(f"[INFO] Keine Log-Dateien im Verzeichnis '{log_directory}' gefunden.")
                return

            # Nmap Scans zuerst
            for filename in log_files:
                if filename.endswith(".nmap") or filename.endswith(".txt"):
                    filepath = os.path.join(log_directory, filename)
                    print_file_header(filename)
                    with open(filepath, 'r', errors='ignore') as f:
                        print(f.read().strip())

            # JSON Logs (Feroxbuster & co)
            for filename in log_files:
                if filename.endswith(".json") and "nmap" not in filename:
                    filepath = os.path.join(log_directory, filename)
                    print_file_header(filename)
                    
                    with open(filepath, 'r', errors='ignore') as f:
                        # Header fuer Tabelle
                        print(f"{LogColors.BOLD}STATUS   SIZE      URL{LogColors.RESET}")
                        print(f"{LogColors.TURQ}{'-' * 60}{LogColors.RESET}")
                        
                        for line in f:
                            # Pruefen ob Feroxbuster Format
                            formatted = format_ferox_line(line)
                            if formatted:
                                print(formatted)
                            else:
                                # Fallback fuer normales JSON (z.B. Nikto JSON)
                                if line.strip().startswith("{") and "ferox" not in filename:
                                    try:
                                        # Versuchen wir es schoen zu formatieren
                                        parsed = json.loads(line)
                                        print(json.dumps(parsed, indent=2))
                                    except:
                                        print(line.strip())

        except FileNotFoundError:
            print(f"[FEHLER] Log-Verzeichnis '{log_directory}' nicht gefunden.")