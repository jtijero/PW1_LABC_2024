#!/bin/bash
set -e

# Iniciar MariaDB directamente
mysqld_safe --skip-grant-tables &

# Esperar a que MariaDB esté completamente iniciado
until mysqladmin ping --silent; do
    echo "Esperando a que MariaDB inicie..."
    sleep 1
done

# Crear la base de datos y ejecutar el script SQL
mysql < /docker-entrypoint-initdb.d/prueba.sql || { echo "Error al ejecutar el script SQL"; exit 1; }

# No detener MariaDB, ya que debe seguir corriendo

