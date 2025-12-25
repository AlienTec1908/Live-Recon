import os
import shutil

class Colors:
    # Banner Farben
    ICE_BLUE = '\033[96m'
    RESET = "\033[0m"
    
    # UI Farben
    BOLD = "\033[1m"
    MAGENTA = '\033[35m'
    WHITE_TXT = "\033[97m"
    BLACK_TXT = "\033[30m"
    SEPARATOR = "\033[96m"
    TURQ_BG = "\033[46m"
    HEADER_TEXT_STYLE = "\033[46m\033[1;37m"
    PLACEHOLDER = "\033[100m\033[91m" 

    COLOR_PAIRS = [
        ("\033[44m", WHITE_TXT),
        ("\033[103m", BLACK_TXT),
        ("\033[41m", WHITE_TXT),
        ("\033[106m", BLACK_TXT),
        ("\033[45m", WHITE_TXT),
        ("\033[102m", BLACK_TXT),
        ("\033[104m", WHITE_TXT),
        ("\033[43m", BLACK_TXT),
        ("\033[101m", WHITE_TXT),
        ("\033[42m", BLACK_TXT),
        ("\033[105m", WHITE_TXT),
        ("\033[46m", BLACK_TXT),
        ("\033[100m", WHITE_TXT),
    ]

LABEL_INDEX = {
    "ipv6-active": 5, "link-local": 5, "cookie-found": 4,
    "GET": 9, "POST": 9, "OPTIONS": 9, "HEAD": 9,
    "ssh": 0, "http": 3, "https": 3, "python-http": 9,
    "wpconfig": 8, "admin_panel": 8,
}

def pill(label):
    if label in LABEL_INDEX:
        idx = LABEL_INDEX[label]
    else:
        idx = (sum(ord(c) for c in label) + len(label))
    pair = Colors.COLOR_PAIRS[idx % len(Colors.COLOR_PAIRS)]
    return f"{pair[0]}{pair[1]} {label} {Colors.RESET}"

def print_mega_banner():
    banner = r"""
 ██╗      ██╗██╗   ██╗███████╗    ██████╗ ███████╗ ██████╗  ██████╗  ███╗   ██╗
 ██║      ╚═╝██║   ██║██╔════╝    ██╔══██╗██╔════╝██╔════╝ ██╔═████╗ ████╗  ██║
 ██║      ██╗██║   ██║█████╗      ██████╔╝█████╗  ██║      ██║██╔██║ ██╔██╗ ██║
 ██║      ██║╚██╗ ██╔╝██╔══╝      ██╔══██╗██╔══╝  ██║      ████╔╝██║ ██║╚██╗██║
 ███████╗ ██║ ╚████╔╝ ███████╗    ██║  ██║███████╗╚██████╗ ╚██████╔╝ ██║ ╚████║
 ╚══════╝ ╚═╝  ╚═══╝  ╚══════╝    ╚═╝  ╚═╝╚══════╝ ╚═════╝  ╚═════╝  ╚═╝  ╚═══╝
                      AlienTec Live Winter Recon Tool
"""          
    print(f"{Colors.ICE_BLUE}{banner}{Colors.RESET}")

def print_live_banner(scan_mode, findings):
    try:
        width = shutil.get_terminal_size().columns
    except OSError:
        width = 100

    mode_bg = "\033[42m" if scan_mode == "internal" else "\033[41m"
    mode_fg = Colors.BLACK_TXT if scan_mode == "internal" else Colors.WHITE_TXT

    print(f"\n{mode_bg}{mode_fg} {scan_mode.upper()} {Colors.RESET}")
    print(f"{Colors.SEPARATOR}{'═' * width}{Colors.RESET}")
    
    title = " Live - Finding - System "
    total_padding = width - len(title)
    pad_left = total_padding // 2
    pad_right = total_padding - pad_left
    
    print(f"{Colors.TURQ_BG}{' ' * pad_left}{Colors.HEADER_TEXT_STYLE}{title}{Colors.TURQ_BG}{' ' * pad_right}{Colors.RESET}")
    print(f"{Colors.SEPARATOR}{'═' * width}{Colors.RESET}")

    display_order = ["ipv6", "nmap", "webserver", "methods", "cookie", "nikto", "ferox"]
    for category in display_order:
        labels = findings.get(category, set())
        display_name = "dirscan" if category == "ferox" else ("ports" if category == "nmap" else category)
        
        prefix = f"{display_name:<10}: "
        print(prefix, end="")
        line_len = len(prefix)

        if not labels:
            print(f"{Colors.PLACEHOLDER} [x][x][x] {Colors.RESET}")
        else:
            for label in sorted(labels):
                p = pill(label)
                p_len = len(label) + 2 
                if line_len + p_len >= width:
                    print("\n" + " " * len(prefix), end="")
                    line_len = len(prefix)
                print(p, end=" ")
                line_len += p_len
            print()
    print(f"{Colors.SEPARATOR}{'═' * width}{Colors.RESET}")

def print_scan_title(name):
    print(f"\n>>> SCAN: {name.upper()}")

def print_scan_end():
    try:
        width = shutil.get_terminal_size().columns
    except OSError:
        width = 100
    print(f"{Colors.SEPARATOR}{'─' * width}{Colors.RESET}")

if __name__ == "__main__":
    if os.name == 'nt':
        os.system('color')
    print_mega_banner()

 # success bonus marker
def print_success(message):
    print(f"{Colors.ICE_BLUE}[+]{Colors.RESET} {Colors.WHITE_TXT}{message}{Colors.RESET}")