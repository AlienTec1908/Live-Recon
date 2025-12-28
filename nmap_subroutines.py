def ftp_anon_get(target):
    print(f"\n>>> SUBROUTINE GESTARTET: ftp_anon_get auf {target}")
    print(">>> AKTION: Versuche, den gesamten FTP-Server rekursiv herunterzuladen...")
    # Hier käme der `wget -m ...` Befehl

def ftp_brute(target):
    print(f"\n>>> SUBROUTINE GESTARTET: ftp_brute auf {target}")
    print(">>> AKTION: Starte Hydra Brute-Force gegen den FTP-Dienst...")

def telnet_brute(target):
    print(f"\n>>> SUBROUTINE GESTARTET: telnet_brute auf {target}")
    print(">>> AKTION: Starte Hydra Brute-Force gegen den Telnet-Dienst...")

def dns_axfr(target):
    print(f"\n>>> SUBROUTINE GESTARTET: dns_axfr auf {target}")
    print(">>> AKTION: Versuche einen DNS Zone Transfer...")

def smb_enum(target):
    print(f"\n>>> SUBROUTINE GESTARTET: smb_enum auf {target}")
    print(">>> AKTION: Starte enum4linux für eine umfassende SMB-Enumeration...")

def smb_nullsession(target):
    print(f"\n>>> SUBROUTINE GESTARTET: smb_nullsession auf {target}")
    print(">>> AKTION: Prüfe gezielt auf SMB Null Session mit rpcclient...")