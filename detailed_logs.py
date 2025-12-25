import os
import json
import shutil

class LogColors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    TURQ = "\033[96m"

    # Lime background 
    HEADER_STYLE = "\033[102m\033[30m\033[1m"

    # Status colors
    GREEN = "\033[92m"   # 200
    YELLOW = "\033[93m"  # 300
    RED = "\033[91m"     # 400/500
    BLUE = "\033[94m"    # Info


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

        if data.get("type") != "response":
            return None

        status = data.get("status", 0)
        url = data.get("url", "")
        length = data.get("content_length", 0)

        
        s_color = LogColors.GREEN
        if 300 <= status < 400:
            s_color = LogColors.YELLOW
        if status >= 400:
            s_color = LogColors.RED

        
        return (
            f"{s_color}[{status}]{LogColors.RESET}  "
            f"({LogColors.BLUE}{length:>6}b{LogColors.RESET})  {url}"
        )

    except json.JSONDecodeError:
        return None


def show_detailed_logs(log_directory):
    answer = input(
        "\n[?] If you want to display all scan results in detail, "
        "press 'J' and hit Enter: "
    )

    if answer.lower() == 'j':
        try:
            log_files = sorted(os.listdir(log_directory))
            if not log_files:
                print(f"[INFO] No log files found in directory '{log_directory}'.")
                return

            
            for filename in log_files:
                if filename.endswith(".nmap") or filename.endswith(".txt"):
                    filepath = os.path.join(log_directory, filename)
                    print_file_header(filename)
                    with open(filepath, 'r', errors='ignore') as f:
                        print(f.read().strip())

            
            for filename in log_files:
                if filename.endswith(".json") and "nmap" not in filename:
                    filepath = os.path.join(log_directory, filename)
                    print_file_header(filename)

                    with open(filepath, 'r', errors='ignore') as f:
                        
                        print(f"{LogColors.BOLD}STATUS   SIZE      URL{LogColors.RESET}")
                        print(f"{LogColors.TURQ}{'-' * 60}{LogColors.RESET}")

                        for line in f:
                            formatted = format_ferox_line(line)
                            if formatted:
                                print(formatted)
                            else:
                                
                                if line.strip().startswith("{") and "ferox" not in filename:
                                    try:
                                        parsed = json.loads(line)
                                        print(json.dumps(parsed, indent=2))
                                    except Exception:
                                        print(line.strip())

        except FileNotFoundError:
            print(f"[ERROR] Log directory '{log_directory}' not found.")
