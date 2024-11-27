#!/bin/bash

# Iniciar el servicio de MariaDB
service mysql start

# Esperar un momento para asegurarse de que MariaDB esté listo
sleep 5

# Iniciar el script de inicialización de la base de datos
/usr/local/bin/init_db.sh || { echo "Error al inicializar la base de datos"; exit 1; }

# Iniciar Apache
apache2ctl -D FOREGROUND || { echo "Error al iniciar Apache"; exit 1; }

