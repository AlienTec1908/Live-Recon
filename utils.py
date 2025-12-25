import shutil
import sys
import subprocess
import os

def check_dependencies():
    print("[+] Checking toolchain...")

    required_tools = [
        "nmap", "nikto", "feroxbuster", "curl", "wpscan",
        "joomscan", "hydra", "rpcclient", "enum4linux", "wget"
    ]

    missing_tools = []

    for tool in required_tools:
        if shutil.which(tool) is None:
            missing_tools.append(tool)

    if missing_tools:
        print(f"[ERROR] The following tools are missing: {', '.join(missing_tools)}")

        answer = input(
            "Should Recon Monster attempt to install them automatically? "
            "(apt-get will be used) [y/N]: "
        )

        if answer.lower() == 'y':
            print("[+] Attempting to install missing tools...")

            sudo_prefix = [] if os.getuid() == 0 else ["sudo"]

            try:
                update_command = sudo_prefix + ["apt-get", "update"]
                subprocess.run(update_command, check=True)

                install_command = sudo_prefix + ["apt-get", "install", "-y"] + missing_tools
                subprocess.run(install_command, check=True)

                print("[+] Installation successful! Re-checking dependencies...")
                check_dependencies()

            except subprocess.CalledProcessError:
                print("[ERROR] Automatic installation failed. Please install the tools manually.")
                sys.exit(1)

            except FileNotFoundError:
                print("[ERROR] 'sudo' or 'apt-get' not found. Please install dependencies manually.")
                sys.exit(1)
        else:
            print("[ERROR] Aborted by user. Please install the missing tools manually.")
            sys.exit(1)
    else:
        print("[+] All required tools are installed and ready.")
