# 🚀 Guía de Reproducción Rápida (Foolproof)

Esta guía permite desplegar el laboratorio completo de Seguridad Ofensiva y Defensiva en menos de 5 minutos, incluso sin conocimientos previos de Wazuh o Docker.

## 📋 Requisitos Previos
- Docker y Docker-Compose instalados.
- Clonar este repositorio: `git clone https://github.com/jscamargo-cyber/Offensive-Defense-Pipeline`.

---

## 🛠️ Paso 1: Levantar la Infraestructura
Desde la raíz del proyecto, ejecuta:
```bash
docker-compose up -d
```
> [!NOTE]
> Esto iniciará el SIEM Wazuh y el contenedor víctima (k-void-victima). Espera ~2 minutos a que el Dashboard de Wazuh esté listo.

## ⚙️ Paso 2: Automatización "One-Click"
Para evitar configuraciones manuales complejas, ejecuta el script de automatización:
```bash
chmod +x setup.sh && ./setup.sh
```
**¿Qué hace este script?**
1. Instala automáticamente Python y SSH en la víctima.
2. Despliega las reglas de detección personalizadas en Wazuh.
3. Configura el escenario vulnerable inicial.

---

## 💀 Paso 3: Simular el Ataque (Exfiltración)
Ejecuta el script de ataque para disparar la alerta en el SIEM:
```bash
docker exec k-void-victima python3 /tmp/x_filtr.py
```
> [!TIP]
> Verás un mensaje confirmando que la telemetría ha sido enviada a los logs del sistema.

---

## 🛡️ Paso 4: Validación y Hardening (Defensa)
1. **Ver Alerta**: Entra al Dashboard de Wazuh (localhost) y verás una **Alerta de Nivel 12 (Crítica)** con el título `X-FILTR: EXFILTRACION DE DATOS`.
2. **Aplicar Hardening**: Cierra la vulnerabilidad detectada ejecutando:
```bash
# Bloquear acceso ROOT y Password en SSH
docker exec k-void-victima sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
docker exec k-void-victima sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
docker exec k-void-victima service ssh restart
```


---
**Desarrollado por John Camargo - Estrategia Ofensiva-Defensiva.**
