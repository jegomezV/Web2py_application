#!/bin/sh

# Wait for Postgres to become available
until PGPASSWORD="$POSTGRES_PASSWORD" psql -h "192.168.1.17" -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
    echo "Postgres is unavailable - sleeping"
    sleep 1
done

# Cambia al directorio de alembic y ejecuta las migraciones
cd /app/applications/SIP_application/databases
alembic upgrade head

# Cambia al directorio de web2py e inicia la aplicación
cd /app
exec python3 web2py.py -a "root"