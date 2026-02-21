🛡️ Hardened-Detection-Lab: Wazuh SIEM & CIS Hardening


1. Project Overview

Este proyecto implementa un stack de seguridad integral en entornos contenedorizados (Docker), fusionando la Ingeniería de Detección con el Endurecimiento de Sistemas (Hardening) bajo el estándar CIS (Center for Internet Security). El objetivo principal es establecer una línea base de seguridad monitoreada por Wazuh SIEM, capaz de detectar intentos de exfiltración de datos y ataques de fuerza bruta en tiempo real.

2. Detection Engineering (X-FILTR)

Se ha diseñado e implementado una lógica de detección personalizada para identificar IoCs (Indicadores de Compromiso) asociados a la exfiltración de datos por puertos no estándar.
Regla 100002: Alerta Crítica de Exfiltración

    ID: 100002

    Nivel: 12 (Critical Alert)

    Mapeo MITRE ATT&CK: T1041 - Exfiltration Over C2 Channel

    Validación: Confirmada mediante wazuh-logtest con el siguiente vector de ataque:
    Bash

    Feb 21 13:30:00 wazuh-agent: X-FILTR attack detected on port 4444
    **Phase 3: Completed filtering (rules). id: '100002', Level: '12'
    **Alert to be generated.

3. Vulnerability & Hardening Report

Target: 172.17.0.2 (k-void-victima) | Auditor: Senior Security Engineer
Phase 1: Exploitation & Discovery

Mediante el uso de nmap -sV --script vuln, se identificó el vector de ataque CVE-2023-48795 (Terrapin) en el servicio SSH (Puerto 22), junto con una política de autenticación débil.
Phase 2: Proceso de Hardening (Step-by-Step)

Para mitigar el riesgo de compromiso inicial, se aplicaron las siguientes remediaciones basadas en CIS Control 4.3:

    Deshabilitar Root Login: sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

    Forzar Autenticación por Llave: sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

    Reinicio de Servicio: service ssh restart

Phase 3: Validación con Lynis

El endurecimiento fue auditado mediante Lynis, logrando una mejora tangible en la postura de seguridad:

    Baseline (Pre-Hardening): 52

    Post-Hardening: 54

    Control Transitions: Los controles SSH-7408 (Root Login) y SSH-7412 (Password Auth) pasaron de FAIL a SUCCESS.

    4. Security Persistence & Immutability

En arquitecturas de microservicios, la persistencia de seguridad debe ser nativa. Se recomienda asegurar que estos controles no sean volátiles mediante la integración en el Dockerfile:
Dockerfile

# Implementación de Hardening Inmutable
COPY hardened_sshd_config /etc/ssh/sshd_config
RUN chmod 644 /etc/ssh/sshd_config && \
    chown root:root /etc/ssh/sshd_config
