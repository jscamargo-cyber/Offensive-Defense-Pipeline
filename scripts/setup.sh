#!/bin/bash
# setup.sh: Automatización del Laboratorio Offensive-Defense (Anti-Infallible)

echo "🚀 Iniciando configuración del laboratorio..."

# 1. Configurar Wazuh Manager
echo "🛡️ Configurando Reglas en Wazuh Manager..."
docker cp local_rules.xml wazuh-manager:/var/ossec/etc/rules/local_rules.xml
docker exec wazuh-manager chown root:wazuh /var/ossec/etc/rules/local_rules.xml
docker exec wazuh-manager chmod 660 /var/ossec/etc/rules/local_rules.xml
docker exec wazuh-manager /var/ossec/bin/wazuh-control restart

# 2. Configurar Víctima
echo "💀 Configurando contenedor Víctima (k-void-victima)..."
docker exec k-void-victima apt update
docker exec k-void-victima apt install -y python3 openssh-server net-tools
docker cp x_filtr.py k-void-victima:/tmp/x_filtr.py

# 3. Preparar SSH vulnerable (para el ejercicio inicial)
docker exec k-void-victima sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
docker exec k-void-victima sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
docker exec k-void-victima service ssh restart
echo "root:password123" | docker exec -i k-void-victima chpasswd

echo "✅ Laboratorio listo. Ejecuta el ataque con: docker exec k-void-victima python3 /tmp/x_filtr.py"
