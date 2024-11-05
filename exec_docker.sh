#!/bin/bash

# Start Docker services and build if necessary
docker-compose up -d

# Wait a few seconds to ensure services are up
sleep 10

# Execute commands inside the Airflow container
docker-compose exec airflow bash -c "
  # Reset the password for the 'admin' user
  airflow users reset-password -u admin -p admin
"

# Restart the Airflow container
docker-compose restart airflow

sleep 10

echo "Airflow setup complete. Admin password has been reset to 'admin'."