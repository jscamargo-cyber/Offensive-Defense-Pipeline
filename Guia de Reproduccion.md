🛠️ Guía de Reproducción Paso a Paso

Siga estas instrucciones para desplegar el laboratorio y validar las alertas de seguridad y controles de hardening.
1. Despliegue del Entorno

Clone el repositorio y levante la infraestructura de contenedores:
Bash

# Levantar el stack de Wazuh y la víctima
docker-compose up -d

2. Configuración de Detección (SIEM)

Importe la lógica de detección personalizada en el Manager de Wazuh:

    Copie el archivo rules/local_rules.xml al contenedor del manager:
    docker cp rules/local_rules.xml wazuh-manager:/var/ossec/etc/rules/local_rules.xml.

    Reinicie el servicio para aplicar la Regla 100002:
    docker exec wazuh-manager /var/ossec/bin/wazuh-control restart.

3. Ejecución del Ataque (PoC)

Simule el intento de exfiltración de datos desde la víctima:

    Acceda al contenedor víctima:
    docker exec -it k-void-victima bash.

    Ejecute el script de ataque:
    python3 /tmp/scripts/x_filtr.py.

    Validación: Verifique en el Dashboard de Wazuh la generación de una alerta de Nivel 12.

4. Aplicación de Hardening (CIS)

Transforme el sistema de un estado vulnerable a uno endurecido:

    Ejecute la auditoría inicial con Lynis para obtener el Baseline (Index 52).

    Aplique los cambios de configuración en el servicio SSH:
    Bash

    sed -i 's/PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
    sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
    service ssh restart
    ```.

    Re-ejecute la auditoría y valide el incremento del Hardening Index a 54.

📊 Verificación de Resultados

Para confirmar que el ciclo ha sido exitoso, el analista debe observar los siguientes logs en el Manager:
Bash

# Buscar la alerta de exfiltración en los logs de alertas
grep "100002" /var/ossec/logs/alerts/alerts.json
```.

---

### 💡 Nota de "Líder de Proyecto"
> "Este flujo de trabajo no solo valida la capacidad de respuesta ante incidentes, sino que establece un estándar de configuración mínima segura (Baseline) para cualquier despliegue posterior en la organización".



**¿Te gustaría que te ayude a redactar una sección de "Preguntas Frecuentes" (FAQ)
