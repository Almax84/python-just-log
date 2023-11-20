# Dockerfile
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY random_logger.py .

# Command to run the script
CMD ["python", "random_logger.py"]

