# 🚀 Guía de Reproducción Rápida (Foolproof)

Esta guía permite desplegar el laboratorio completo en menos de 5 minutos, garantizando que todos los servicios y telemetría funcionen correctamente.

## 📋 Requisitos Previos
- Docker y Docker-Compose instalados.
- Clonar el repositorio.

---

## 🛠️ Paso 1: Levantar la Infraestructura
```bash
docker-compose up -d
```
*Espera 2 minutos a que el SIEM esté totalmente inicializado.*

## ⚙️ Paso 2: Configuración Automática
Para resolver dependencias e inyectar las reglas de detección, simplemente ejecuta:
```bash
chmod +x setup.sh && ./setup.sh
```
**Impacto Técnico:**
- Inyecta la Regla 100002 (SID 1002) en el Manager.
- Instala `python3` y `ssh` en la víctima.
- Prepara la telemetría de Syslog para detección en tiempo real.

---

## 💀 Paso 3: Simulación de Exfiltración (Demo)
Ejecuta el ataque:
```bash
docker exec k-void-victima python3 /tmp/x_filtr.py
```
**Resultado en el SIEM:** Verás una alerta de **Nivel 12** mapeada a **MITRE T1041**.

---

## 🛡️ Paso 4: Hardening (Remediación)
Aplica los controles CIS para cerrar el vector inicial:
```bash
docker exec k-void-victima sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
docker exec k-void-victima sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
docker exec k-void-victima service ssh restart
```

---
**Validado para Entrevistas Técnicas - J. Camargo**
