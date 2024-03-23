#!/bin/sh

# Wait for Postgres to become available
until PGPASSWORD="$POSTGRES_PASSWORD" psql -h db -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c '\q'; do
    sleep 1
done

# Cambia al directorio de alembic y ejecuta las migraciones
cd /app/applications/SIP_application/databases
alembic upgrade head

# Cambia al directorio de web2py e inicia la aplicación
cd /app
echo "Join app"
exec python web2py.py --nogui -a admin -i 0.0.0.0