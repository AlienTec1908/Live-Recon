import json

class NmapRunner:
    def __init__(self, json_file_path):
        self.nmap_data = self._load_json(json_file_path)
        self.tasks_to_run = []

    def _load_json(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return None

    def run_analysis(self):
        if not self.nmap_data:
            print("[FEHLER] Nmap JSON-Log konnte nicht geladen oder geparst werden.")
            return []

        for host in self.nmap_data.get('hosts', []):
            for port in host.get('ports', []):
                port_id = port.get('portid')
                service = port.get('service', {})
                service_name = service.get('name', 'unknown')
                scripts = port.get('scripts', [])

                if service_name == 'ftp':
                    is_anon = False
                    for script in scripts:
                        if script.get('id') == 'ftp-anon' and 'Anonymous FTP login allowed' in script.get('output'):
                            self.tasks_to_run.append('ftp_anon_get')
                            is_anon = True
                            break
                    if not is_anon:
                        self.tasks_to_run.append('ftp_brute')
                
                if service_name == 'telnet':
                    self.tasks_to_run.append('telnet_brute')

                if service_name == 'domain':
                    self.tasks_to_run.append('dns_axfr')
                    
                if 'netbios-ssn' in service_name or 'microsoft-ds' in service_name:
                    self.tasks_to_run.append('smb_enum')
                    if 'Microsoft Windows' in host.get('osmatch', [{}])[0].get('name', ''):
                        self.tasks_to_run.append('smb_nullsession')

        return list(set(self.tasks_to_run))